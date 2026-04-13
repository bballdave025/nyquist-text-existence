#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file: classes_module.py
@author: David Black   GitHub @bballdave025
@since: 2026-02-25

Two primary classes and a frozen dataclass. 

SpatialSignalSampler
class CropFinalizer
@dataclass CropSpec

Dependencies:
  - numpy
  - opencv-python (cv2)
'''

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Sequence

import numpy as np
import cv2


AggMode = Literal["mean", "sum"]


@dataclass(frozen=True)
class CropSpec:
  x: int
  y: int
  w: int
  h: int



class SpatialSignalSampler:
  """Minimal resampling + FFT utilities."""

  @staticmethod
  def load_gray_u8(path: str | Path) -> np.ndarray:
    p = str(path)
    img = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
    if img is None: raise FileNotFoundError(f"Could not read: {p}")
    return img.astype(np.uint8, copy=False)

  @staticmethod
  def resample_flexible(
      gray_u8: np.ndarray,
      factor: Optional[float] = None,
      target_w: Optional[int] = None,
      target_h: Optional[int] = None,
      interp: Literal["area", "nearest", "cubic"] = "area"
  ) -> np.ndarray:
    """
    Enforces NTEC linear reduction logic: new_dim = orig_dim // factor.
    Only one of {factor, target_w, target_h} allowed.
    """
    provided = [x is not None for x in [factor, target_w, target_h]]
    if sum(provided) != 1:
      raise ValueError("Provide exactly ONE of: factor, target_w, or target_h.")

    H, W = gray_u8.shape[:2]
    interp_map = {"area": cv2.INTER_AREA, "nearest": cv2.INTER_NEAREST, "cubic": cv2.INTER_CUBIC}
        
    if factor is not None:
      if factor <= 0: raise ValueError("factor must be positive.")
      newW, newH = max(1, int(W // factor)), max(1, int(H // factor))
    elif target_w is not None:
      newW, newH = target_w, max(1, int(H * (target_w / W)))
    else: # target_h
      newH, newW = target_h, max(1, int(W * (target_h / H)))

      return cv2.resize(gray_u8, (newW, newH), interpolation=interp_map[interp])

  @staticmethod
  def save_gray_u8(path: str | Path, img_u8: np.ndarray) -> None:
    if img_u8.ndim != 2:
      raise ValueError("Expected grayscale image (H, W).")
    if img_u8.dtype != np.uint8:
      img_u8 = img_u8.astype(np.uint8, copy=False)
    p = str(path)
    ok = cv2.imwrite(p, img_u8)
    if not ok:
      raise IOError(f"Failed to write image: {p}")

  @staticmethod
  def to_float01(gray_u8: np.ndarray) -> np.ndarray:
    if gray_u8.ndim != 2:
      raise ValueError("Expected grayscale image (H, W).")
    if gray_u8.dtype != np.uint8:
      raise ValueError("to_float01 expects uint8 input.")
    return (gray_u8.astype(np.float32) / 255.0)

  @staticmethod
  def save_float_image(path: str | Path, img_float01: np.ndarray) -> None:
    """
    Save float image (any finite range) as uint8 safely:
    - If data already in [0,1], preserve that scale.
    - Otherwise min-max normalize (finite values).
    """
    if img_float01.ndim != 2:
      raise ValueError("Expected grayscale image (H, W).")
    x = img_float01.astype(np.float32, copy=False)

    finite = np.isfinite(x)
    if not np.any(finite):
      out = np.zeros_like(x, dtype=np.uint8)
      SpatialSignalSampler.save_gray_u8(path, out)
      return

    mn = float(np.min(x[finite]))
    mx = float(np.max(x[finite]))

    # If it already looks like [0,1] (with small tolerance), keep that.
    if mn >= -1e-6 and mx <= 1.0 + 1e-6:
      y = np.clip(x, 0.0, 1.0)
      out = (y * 255.0 + 0.5).astype(np.uint8)
      SpatialSignalSampler.save_gray_u8(path, out)
      return

    # Otherwise min-max normalize.
    if mx - mn < 1e-12:
      out = np.zeros_like(x, dtype=np.uint8)
      SpatialSignalSampler.save_gray_u8(path, out)
      return

    y = (x - mn) / (mx - mn)
    y = np.clip(y, 0.0, 1.0)
    out = (y * 255.0 + 0.5).astype(np.uint8)
    SpatialSignalSampler.save_gray_u8(path, out)

  # ---------- cropping ----------

  @staticmethod
  def crop_gray_u8(gray_u8: np.ndarray, crop: CropSpec | None) -> np.ndarray:
    if gray_u8.ndim != 2:
      raise ValueError("Expected grayscale image (H, W).")
    if crop is None:
      return gray_u8
    if crop.w <= 0 or crop.h <= 0:
      raise ValueError("Crop w/h must be positive.")
    H, W = gray_u8.shape[:2]
    x = max(0, min(int(crop.x), max(0, W - int(crop.w))))
    y = max(0, min(int(crop.y), max(0, H - int(crop.h))))
    w = int(crop.w)
    h = int(crop.h)
    return gray_u8[y:y + h, x:x + w]

  # ---------- resampling ----------

  @staticmethod
  def resample_gray_u8(
    gray_u8: np.ndarray,
    mode: Literal["down", "up"],
    factor: int,
    interp: Literal["area", "nearest", "cubic"] = "area",
  ) -> np.ndarray:
    if gray_u8.ndim != 2:
      raise ValueError("Expected grayscale image (H, W).")
    if gray_u8.dtype != np.uint8:
      raise ValueError("Expected uint8 image for resample_gray_u8.")
    if factor <= 0:
      raise ValueError("factor must be positive.")

    interp_map = {
      "area": cv2.INTER_AREA,
      "nearest": cv2.INTER_NEAREST,
      "cubic": cv2.INTER_CUBIC,
    }
    if interp not in interp_map:
      raise ValueError(f"Unknown interp={interp!r}")

    H, W = gray_u8.shape[:2]
    if mode == "down":
      newW, newH = max(1, W // factor), max(1, H // factor)
    elif mode == "up":
      newW, newH = W * factor, H * factor
    else:
      raise ValueError("mode must be 'down' or 'up'.")

    return cv2.resize(gray_u8, (newW, newH), interpolation=interp_map[interp])

  @staticmethod
  def resize_to(gray_u8: np.ndarray, out_w: int, out_h: int,
                interp: Literal["area", "nearest", "cubic"] = "nearest") -> np.ndarray:
    if gray_u8.ndim != 2:
      raise ValueError("Expected grayscale image (H, W).")
    if gray_u8.dtype != np.uint8:
      raise ValueError("Expected uint8 image for resize_to.")
    if out_w <= 0 or out_h <= 0:
      raise ValueError("out_w/out_h must be positive.")

    interp_map = {
      "area": cv2.INTER_AREA,
      "nearest": cv2.INTER_NEAREST,
      "cubic": cv2.INTER_CUBIC,
    }
    if interp not in interp_map:
      raise ValueError(f"Unknown interp={interp!r}")

    return cv2.resize(gray_u8, (int(out_w), int(out_h)), interpolation=interp_map[interp])

  # ---------- FFT + magnitude ----------

  @staticmethod
  def fft2(gray_float01: np.ndarray) -> np.ndarray:
    if gray_float01.ndim != 2:
      raise ValueError("Expected grayscale image (H, W).")
    g = gray_float01.astype(np.float32, copy=False)
    return np.fft.fft2(g)

  @staticmethod
  def fft_mag(
    fft: np.ndarray,
    shift: bool = True,
    log1p: bool = True,
    normalize: bool = True,
  ) -> np.ndarray:
    """
    Returns float32 magnitude image, optionally:
      - shift DC to center
      - log1p compress
      - normalize to [0,1] (finite range)
    """
    z = fft
    if shift:
      z = np.fft.fftshift(z)

    mag = np.abs(z).astype(np.float32, copy=False)

    if log1p:
      mag = np.log1p(mag)

    if not normalize:
      return mag.astype(np.float32, copy=False)

    finite = np.isfinite(mag)
    if not np.any(finite):
      return np.zeros_like(mag, dtype=np.float32)

    mn = float(np.min(mag[finite]))
    mx = float(np.max(mag[finite]))
    if mx - mn < 1e-12:
      return np.zeros_like(mag, dtype=np.float32)

    out = (mag - mn) / (mx - mn)
    out = np.clip(out, 0.0, 1.0).astype(np.float32)
    return out



class CropFinalizer:
  """
  Deterministic crop selection via Sobel-energy ranking + phase sweep.
  """

  @staticmethod
  def load_gray_u8(path: str | Path) -> np.ndarray:
    p = str(path)
    img = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
    if img is None:
      raise FileNotFoundError(f"Could not read image: {p}")
    if img.dtype != np.uint8:
      img = img.astype(np.uint8, copy=False)
    return img

  @staticmethod
  def sobel_mag(gray_u8: np.ndarray, ksize: int = 3) -> np.ndarray:
    if gray_u8.ndim != 2:
      raise ValueError("Expected grayscale image (H, W).")
    g = gray_u8.astype(np.float32, copy=False)
    gx = cv2.Sobel(g, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
    gy = cv2.Sobel(g, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)
    return cv2.magnitude(gx, gy)

  @staticmethod
  def _clip_crop_to_image(crop: CropSpec, H: int, W: int) -> CropSpec:
    if crop.w <= 0 or crop.h <= 0:
      return crop
    x = max(0, min(crop.x, max(0, W - crop.w)))
    y = max(0, min(crop.y, max(0, H - crop.h)))
    return CropSpec(x=x, y=y, w=crop.w, h=crop.h)

  @staticmethod
  def generate_unbiased_mcc(
    initial_spec: CropSpec, 
    img_shape: tuple[int, int],
    seed: int = 137,
    coord_sigma_pct: float = 0.10,
    dim_jitter_pct: float = 0.05
  ) -> CropSpec:
    """The Physics-Seeded Shaker for Addendum 1."""
    rng = np.random.default_rng(seed)
    H_max, W_max = img_shape
    
    w_jitter = rng.uniform(1.0 - dim_jitter_pct, 1.0 + dim_jitter_pct)
    h_jitter = rng.uniform(1.0 - dim_jitter_pct, 1.0 + dim_jitter_pct)
    new_w, new_h = int(initial_spec.w * w_jitter), int(initial_spec.h * h_jitter)
    
    new_x = int(rng.normal(initial_spec.x, initial_spec.w * coord_sigma_pct))
    new_y = int(rng.normal(initial_spec.y, initial_spec.h * coord_sigma_pct))
    
    # Clip to image boundaries
    final_x = max(0, min(new_x, W_max - new_w))
    final_y = max(0, min(new_y, H_max - new_h))
    return CropSpec(x=final_x, y=final_y, w=new_w, h=new_h)

  @classmethod
  def crop_score(cls, edge_mag: np.ndarray, crop: CropSpec, agg: AggMode = "mean") -> float:
    H, W = edge_mag.shape[:2]
    crop = cls._clip_crop_to_image(crop, H, W)
    patch = edge_mag[crop.y:crop.y + crop.h, crop.x:crop.x + crop.w]
    if patch.size == 0:
      return float("nan")

    if agg == "sum":
      return float(np.sum(patch, dtype=np.float64))
    if agg == "mean":
      return float(np.mean(patch, dtype=np.float64))

    raise ValueError(f"Unknown agg={agg!r}; use 'mean' or 'sum'.")

  @classmethod
  def sliding_window_scores(
    cls,
    edge_mag: np.ndarray,
    w: int,
    h: int,
    step: int = 8,
    agg: AggMode = "mean",
  ) -> tuple[np.ndarray, list[int], list[int]]:
    H, W = edge_mag.shape[:2]
    if w <= 0 or h <= 0:
      raise ValueError("w and h must be positive.")
    if step <= 0:
      raise ValueError("step must be positive.")

    xs = list(range(0, max(1, W - w + 1), step))
    ys = list(range(0, max(1, H - h + 1), step))

    scores = np.empty((len(ys), len(xs)), dtype=np.float32)
    for j, y in enumerate(ys):
      for i, x in enumerate(xs):
        scores[j, i] = cls.crop_score(edge_mag, CropSpec(x, y, w, h), agg=agg)
    return scores, xs, ys

  @classmethod
  def best_crop_on_grid(
    cls,
    edge_mag: np.ndarray,
    w: int,
    h: int,
    step: int = 8,
    agg: AggMode = "mean",
  ) -> tuple[CropSpec, float]:
    scores, xs, ys = cls.sliding_window_scores(edge_mag, w=w, h=h, step=step, agg=agg)
    if scores.size == 0:
      return CropSpec(0, 0, w, h), float("nan")

    # Tie-break parity: np.nanargmax returns first max in row-major order.
    idx = int(np.nanargmax(scores))
    j, i = np.unravel_index(idx, scores.shape)
    best = CropSpec(x=xs[i], y=ys[j], w=w, h=h)
    return best, float(scores[j, i])

  @classmethod
  def rank_crops(
    cls,
    edge_mag: np.ndarray,
    w: int,
    h: int,
    step: int = 8,
    agg: AggMode = "mean",
    top_k: int = 5,
  ) -> list[tuple[CropSpec, float]]:
    """
    Return top_k crops in descending score order.
    Deterministic tie-break: earlier in scan order wins.
    """
    if top_k <= 0:
      return []

    scores, xs, ys = cls.sliding_window_scores(edge_mag, w=w, h=h, step=step, agg=agg)
    if scores.size == 0:
      return []

    # Flatten in row-major order to preserve scan-order tie-breaking.
    flat = scores.ravel()
    finite_mask = np.isfinite(flat)
    if not np.any(finite_mask):
      return []

    idxs = np.nonzero(finite_mask)[0]
    vals = flat[finite_mask]

    # Stable sort: score desc, then original order (scan order) asc.
    order = np.argsort(-vals, kind="stable")
    top = idxs[order[:top_k]]

    out: list[tuple[CropSpec, float]] = []
    for flat_idx in top:
      j, i = np.unravel_index(int(flat_idx), scores.shape)
      c = CropSpec(x=xs[i], y=ys[j], w=w, h=h)
      out.append((c, float(scores[j, i])))
    return out

  @classmethod
  def phase_sweep_sanity(
    cls,
    edge_mag: np.ndarray,
    crop: CropSpec,
    agg: AggMode = "mean",
    phase_span: int = 9,
  ) -> tuple[np.ndarray, float]:
    if phase_span <= 0:
      raise ValueError("phase_span must be positive.")

    H, W = edge_mag.shape[:2]
    crop0 = cls._clip_crop_to_image(crop, H, W)

    scores = np.full((phase_span, phase_span), np.nan, dtype=np.float32)
    for dy in range(phase_span):
      for dx in range(phase_span):
        c = CropSpec(crop0.x + dx, crop0.y + dy, crop0.w, crop0.h)
        c = cls._clip_crop_to_image(c, H, W)
        scores[dy, dx] = cls.crop_score(edge_mag, c, agg=agg)

    finite = scores[np.isfinite(scores)]
    if finite.size == 0:
      return scores, float("nan")

    rel_amp = float((finite.max() - finite.min()) / (float(finite.mean()) + 1e-9))
    return scores, rel_amp

