#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file: _crop_sobel_energy.py
@author: David Black   GitHub @bballdave025
@since: 2026-02-25
cv2-first crop scoring + optional phase-sweep sensitivity check.

Dependencies:
  - numpy
  - opencv-python (cv2)

Here to quickly script-test what will eventually go in a class.
'''

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse
import sys

import numpy as np
import cv2


@dataclass(frozen=True)
class CropSpec:
  x: int
  y: int
  w: int
  h: int


def load_gray_u8(path: str | Path) -> np.ndarray:
  """Load image as grayscale uint8 array of shape (H, W)."""
  p = str(path)
  img = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
  if img is None:
    raise FileNotFoundError(f"Could not read image: {p}")
  if img.dtype != np.uint8:
    img = img.astype(np.uint8, copy=False)
  return img


def sobel_mag(gray_u8: np.ndarray, ksize: int = 3) -> np.ndarray:
  """
  Sobel gradient magnitude as float32 array (H, W).

  No blur. Just edges.
  """
  if gray_u8.ndim != 2:
    raise ValueError("Expected grayscale image (H, W).")

  g = gray_u8.astype(np.float32, copy=False)
  gx = cv2.Sobel(g, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
  gy = cv2.Sobel(g, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)
  mag = cv2.magnitude(gx, gy)  # sqrt(gx^2 + gy^2)
  return mag


def _clip_crop_to_image(crop: CropSpec, H: int, W: int) -> CropSpec:
  """Clip crop to image bounds; keep w,h fixed, shift x,y if needed."""
  if crop.w <= 0 or crop.h <= 0:
    return crop
  x = max(0, min(crop.x, max(0, W - crop.w)))
  y = max(0, min(crop.y, max(0, H - crop.h)))
  return CropSpec(x=x, y=y, w=crop.w, h=crop.h)


def crop_score(edge_mag: np.ndarray, crop: CropSpec, agg: str = "mean") -> float:
  """Score a crop on edge magnitude using mean or sum."""
  H, W = edge_mag.shape[:2]
  crop = _clip_crop_to_image(crop, H, W)
  patch = edge_mag[crop.y:crop.y + crop.h, crop.x:crop.x + crop.w]
  if patch.size == 0:
    return float("nan")

  if agg == "sum":
    return float(np.sum(patch, dtype=np.float64))
  if agg == "mean":
    return float(np.mean(patch, dtype=np.float64))

  raise ValueError(f"Unknown agg={agg!r}; use 'mean' or 'sum'.")


def sliding_window_scores(
  edge_mag: np.ndarray,
  w: int,
  h: int,
  step: int = 8,
  agg: str = "mean",
) -> tuple[np.ndarray, list[int], list[int]]:
  """
  Score crops on a grid.

  Returns:
    scores: float32 array (len(ys), len(xs))
    xs: list of x positions
    ys: list of y positions
  """
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
      scores[j, i] = crop_score(edge_mag, CropSpec(x, y, w, h), agg=agg)
  return scores, xs, ys


def best_crop_on_grid(
  edge_mag: np.ndarray,
  w: int,
  h: int,
  step: int = 8,
  agg: str = "mean",
) -> tuple[CropSpec, float]:
  """
  Return the best crop on the step grid (argmax score).

  Tie-break behavior:
    - np.nanargmax returns the first max in row-major order.
    - With scores indexed [y_index, x_index], that means:
      smallest y first, then smallest x (your “sequentially first”).
  """
  scores, xs, ys = sliding_window_scores(edge_mag, w=w, h=h, step=step, agg=agg)
  if scores.size == 0:
    return CropSpec(0, 0, w, h), float("nan")

  idx = int(np.nanargmax(scores))
  j, i = np.unravel_index(idx, scores.shape)
  best = CropSpec(x=xs[i], y=ys[j], w=w, h=h)
  return best, float(scores[j, i])


def phase_sweep_sanity(
  edge_mag: np.ndarray,
  crop: CropSpec,
  agg: str = "mean",
  phase_span: int = 9,
) -> tuple[np.ndarray, float]:
  """
  Score sensitivity to shifting by dx,dy in [0..phase_span-1].

  Returns:
    scores: (phase_span, phase_span) float32 array [dy, dx]
    rel_amp: (max-min)/mean over finite scores
  """
  if phase_span <= 0:
    raise ValueError("phase_span must be positive.")

  H, W = edge_mag.shape[:2]
  crop0 = _clip_crop_to_image(crop, H, W)

  scores = np.full((phase_span, phase_span), np.nan, dtype=np.float32)
  for dy in range(phase_span):
    for dx in range(phase_span):
      c = CropSpec(crop0.x + dx, crop0.y + dy, crop0.w, crop0.h)
      c = _clip_crop_to_image(c, H, W)
      scores[dy, dx] = crop_score(edge_mag, c, agg=agg)

  finite = scores[np.isfinite(scores)]
  if finite.size == 0:
    return scores, float("nan")

  rel_amp = float((finite.max() - finite.min()) / (float(finite.mean()) + 1e-9))
  return scores, rel_amp


def save_crop_preview(gray_u8: np.ndarray, crop: CropSpec, out_path: str | Path) -> None:
  """Save the cropped grayscale region for sanity checking."""
  H, W = gray_u8.shape[:2]
  crop = _clip_crop_to_image(crop, H, W)
  patch = gray_u8[crop.y:crop.y + crop.h, crop.x:crop.x + crop.w]
  ok = cv2.imwrite(str(out_path), patch)
  if not ok:
    raise IOError(f"Failed to write: {out_path}")


def parse_args(argv: list[str]) -> argparse.Namespace:
  p = argparse.ArgumentParser(
    description="Sobel-energy crop selection + optional phase-sweep sensitivity (cv2-only)."
  )
  p.add_argument("--img", required=True, help="Path to input image.")
  p.add_argument("--crop-w", type=int, default=256, help="Crop width.")
  p.add_argument("--crop-h", type=int, default=256, help="Crop height.")
  p.add_argument("--step", type=int, default=8, help="Sliding window step.")
  p.add_argument("--agg", choices=["mean", "sum"], default="mean", help="Aggregation.")
  p.add_argument("--sobel-ksize", type=int, default=3, help="Sobel kernel size (odd).")

  # Either user-provided crop OR auto-best
  p.add_argument("--x", type=int, default=None, help="Crop x (top-left).")
  p.add_argument("--y", type=int, default=None, help="Crop y (top-left).")
  p.add_argument("--auto-best", action="store_true", help="Pick best crop on grid.")

  # Phase sweep (opt-in)
  p.add_argument(
    "--phase-sweep",
    action="store_true",
    help="Run phase-sweep sensitivity check (dx,dy offsets on a grid).",
  )
  p.add_argument(
    "--phase-span",
    type=int,
    default=9,
    help="Phase-sweep grid size per axis (e.g., 9 -> offsets 0..8). Used only with --phase-sweep. Number of offsets to test per axis.",
  )

  p.add_argument("--save-preview", default=None, help="Optional: save crop preview PNG.")
  
  # -------------------------------------------------------------------------
  # ## USEFUL FUTURE ADDITIONS (for prettifying slides)
  # ## post-2026-02-26 sprint 1
  #
  # These flags are intentionally commented out for now.
  # They are reserved for slide artifact generation after parity is achieved
  # in the class-based refactor (CropFinalizer).
  #
  # p.add_argument(
  #   "--save-overlay",
  #   default=None,
  #   help="Optional: save original image with selected crop outlined (green box)."
  # )
  #
  # p.add_argument(
  #   "--save-sobel-mag",
  #   default=None,
  #   help="Optional: save raw Sobel magnitude image (grayscale float32 scaled)."
  # )
  #
  # p.add_argument(
  #   "--save-sobel-binary",
  #   default=None,
  #   help="Optional: save binarized Sobel edge image (thresholded)."
  # )
  #
  # -------------------------------------------------------------------------
  
  return p.parse_args(argv)


def main(argv: list[str]) -> int:
  args = parse_args(argv)

  gray = load_gray_u8(args.img)
  edges = sobel_mag(gray, ksize=args.sobel_ksize)

  if args.auto_best:
    crop, best_score = best_crop_on_grid(
      edges, w=args.crop_w, h=args.crop_h, step=args.step, agg=args.agg
    )
    print(
      f"auto_best crop: x={crop.x} y={crop.y} w={crop.w} h={crop.h} "
      f"score={best_score:.6g} (agg={args.agg}, step={args.step})"
    )
  else:
    if args.x is None or args.y is None:
      print("ERROR: Provide --x and --y, or use --auto-best.", file=sys.stderr)
      return 2
    crop = CropSpec(x=args.x, y=args.y, w=args.crop_w, h=args.crop_h)
    s = crop_score(edges, crop, agg=args.agg)
    print(f"crop score: {s:.6g} (agg={args.agg})")

  if args.save_preview:
    save_crop_preview(gray, crop, args.save_preview)
    print(f"saved preview crop to: {args.save_preview}")

  if args.phase_sweep:
    grid_scores, rel_amp = phase_sweep_sanity(
      edges, crop, agg=args.agg, phase_span=args.phase_span
    )
    print(f"phase_sensitivity_rel_amp (grid={args.phase_span}x{args.phase_span}) = {rel_amp:.6g}")
    # Keep the grid print off by default; uncomment if you want it.
    # print(grid_scores)

  return 0


if __name__ == "__main__":
  raise SystemExit(main(sys.argv[1:]))
