#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file: classes_module.py
@author: David Black   GitHub @bballdave025
@since: 2026-02-25

Two primary classes and a frozen dataclass. I'll list
them later.

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
  pass



class CropFinalizer:
  """
  Deterministic crop selection via Sobel-energy ranking + optional phase sweep.

  Sprint 2 contract:
  - Parity with _crop_sobel_energy.py (same tie-break, same scoring).
  - No slide-artifact outputs yet (those are parked).
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








