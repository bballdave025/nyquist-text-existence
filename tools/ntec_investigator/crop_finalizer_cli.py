#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
'''
@file : crop_finalizer_cli.py
@author: David Black   GitHub @bballdave025
         with ChatGPT (whatever version) as AI coding helper
@since : 2026-02-26

@brief : CLI bridge for CropFinalizer + slide-artifact generation.
'''

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import cv2

from classes_module import CropFinalizer, CropSpec


def _validate_output_path(path_str: str) -> None:
  p = Path(path_str)
  if p.suffix == "":
    raise ValueError(f"Output path must include a filename with extension: {path_str}")
  if p.parent and not p.parent.exists():
    raise FileNotFoundError(f"Directory does not exist: {p.parent}")


def _ensure_parent_dir_exists(path_str: str) -> None:
  p = Path(path_str)
  if p.parent and not p.parent.exists():
    raise FileNotFoundError(f"Directory does not exist: {p.parent}")


def _save_best_crop(path_str: str, gray_u8: np.ndarray, crop: CropSpec) -> None:
  """
  Save the selected crop patch as uint8 grayscale PNG.
  Crop is clipped to bounds for safety.
  """
  if gray_u8.ndim != 2 or gray_u8.dtype != np.uint8:
    raise ValueError("gray_u8 must be a uint8 2D image.")

  H, W = gray_u8.shape[:2]
  x = max(0, min(int(crop.x), max(0, W - 1)))
  y = max(0, min(int(crop.y), max(0, H - 1)))
  w = max(1, int(crop.w))
  h = max(1, int(crop.h))
  x2 = max(0, min(x + w, W))
  y2 = max(0, min(y + h, H))

  patch = gray_u8[y:y2, x:x2]
  _ensure_parent_dir_exists(path_str)
  ok = cv2.imwrite(str(path_str), patch)
  if not ok:
    raise IOError(f"Failed to write image: {path_str}")


def _save_sobel_mag_u8(path_str: str, edges_f32: np.ndarray) -> None:
  """
  Save Sobel magnitude as uint8 after min-max normalization.
  Deterministic. No smoothing/filtering.
  """
  if edges_f32.ndim != 2:
    raise ValueError("edges_f32 must be 2D.")
  x = edges_f32.astype(np.float32, copy=False)
  finite = np.isfinite(x)
  if not np.any(finite):
    out = np.zeros_like(x, dtype=np.uint8)
  else:
    mn = float(np.min(x[finite]))
    mx = float(np.max(x[finite]))
    if mx - mn < 1e-12:
      out = np.zeros_like(x, dtype=np.uint8)
    else:
      y = (x - mn) / (mx - mn)
      y = np.clip(y, 0.0, 1.0)
      out = (y * 255.0 + 0.5).astype(np.uint8)
  _ensure_parent_dir_exists(path_str)
  ok = cv2.imwrite(str(path_str), out)
  if not ok:
    raise IOError(f"Failed to write image: {path_str}")


def _save_sobel_binary_u8(path_str: str, edges_f32: np.ndarray) -> None:
  """
  Save a binarized Sobel edge image using Otsu thresholding on a normalized uint8 mag.
  Deterministic.
  """
  if edges_f32.ndim != 2:
    raise ValueError("edges_f32 must be 2D.")

  # Normalize to uint8 first (deterministic), then apply Otsu.
  x = edges_f32.astype(np.float32, copy=False)
  finite = np.isfinite(x)
  if not np.any(finite):
    mag_u8 = np.zeros_like(x, dtype=np.uint8)
  else:
    mn = float(np.min(x[finite]))
    mx = float(np.max(x[finite]))
    if mx - mn < 1e-12:
      mag_u8 = np.zeros_like(x, dtype=np.uint8)
    else:
      y = (x - mn) / (mx - mn)
      y = np.clip(y, 0.0, 1.0)
      mag_u8 = (y * 255.0 + 0.5).astype(np.uint8)

  # Otsu threshold → binary (0/255)
  _, bin_u8 = cv2.threshold(mag_u8, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  _ensure_parent_dir_exists(path_str)
  ok = cv2.imwrite(str(path_str), bin_u8)
  if not ok:
    raise IOError(f"Failed to write image: {path_str}")


def _save_overlay(path_str: str, gray_u8: np.ndarray, crop: CropSpec) -> None:
  """
  Draw a green rectangle overlay on the original image and save as PNG.
  Uses a 2 px bounding box. No alpha blending.
  """
  if gray_u8.ndim != 2 or gray_u8.dtype != np.uint8:
    raise ValueError("gray_u8 must be a uint8 2D image.")

  H, W = gray_u8.shape[:2]
  # Clip crop to image bounds for safety.
  x = max(0, min(int(crop.x), max(0, W - 1)))
  y = max(0, min(int(crop.y), max(0, H - 1)))
  w = max(1, int(crop.w))
  h = max(1, int(crop.h))
  x2 = max(0, min(x + w - 1, W - 1))
  y2 = max(0, min(y + h - 1, H - 1))

  # Convert to color so "green box" is literal.
  bgr = cv2.cvtColor(gray_u8, cv2.COLOR_GRAY2BGR)
  cv2.rectangle(bgr, (x, y), (x2, y2), color=(0, 255, 0), thickness=2)

  _ensure_parent_dir_exists(path_str)
  ok = cv2.imwrite(str(path_str), bgr)
  if not ok:
    raise IOError(f"Failed to write image: {path_str}")


def parse_args(argv: list[str]) -> argparse.Namespace:
  p = argparse.ArgumentParser(
    description="CLI bridge for CropFinalizer (class-based parity harness) + slide artifacts."
  )
  p.add_argument("--img", required=True, help="Path to input image.")
  p.add_argument("--crop-w", type=int, default=256, help="Crop width.")
  p.add_argument("--crop-h", type=int, default=256, help="Crop height.")
  p.add_argument("--step", type=int, default=8, help="Sliding window step.")
  p.add_argument("--agg", choices=["mean", "sum"], default="mean", help="Aggregation.")
  p.add_argument("--sobel-ksize", type=int, default=3, help="Sobel kernel size (odd).")

  p.add_argument("--x", type=int, default=None, help="Crop x (top-left).")
  p.add_argument("--y", type=int, default=None, help="Crop y (top-left).")
  p.add_argument("--auto-best", action="store_true", help="Pick best crop on grid.")

  p.add_argument("--phase-sweep", action="store_true", help="Run phase sweep sanity check.")
  p.add_argument("--phase-span", type=int, default=9, help="Phase sweep grid size per axis.")

  # --- Slide artifact outputs (CLI-only) ---
  p.add_argument(
    "--save-best-crop",
    default=None,
    help="Optional: save the selected crop patch as a grayscale image (uint8).",
  )
  p.add_argument(
    "--save-overlay",
    default=None,
    help="Optional: save original image with selected crop outlined (green box).",
  )
  p.add_argument(
    "--save-sobel-mag",
    default=None,
    help="Optional: save Sobel magnitude image (uint8 min-max normalized).",
  )
  p.add_argument(
    "--save-sobel-binary",
    default=None,
    help="Optional: save binarized Sobel edge image (Otsu threshold on normalized mag).",
  )

  return p.parse_args(argv)


def main(argv: list[str]) -> int:
  args = parse_args(argv)

  # Validate output paths early (fail fast)
  for opt in (args.save_overlay, args.save_sobel_mag, args.save_sobel_binary, args.save_best_crop):
    if opt is not None:
      _validate_output_path(opt)

  gray = CropFinalizer.load_gray_u8(args.img)
  edges = CropFinalizer.sobel_mag(gray, ksize=args.sobel_ksize)

  # Optional artifact outputs that don't depend on crop choice
  if args.save_sobel_mag is not None:
    _save_sobel_mag_u8(args.save_sobel_mag, edges)

  if args.save_sobel_binary is not None:
    _save_sobel_binary_u8(args.save_sobel_binary, edges)

  # Determine crop (auto or manual)
  if args.auto_best:
    crop, best_score = CropFinalizer.best_crop_on_grid(
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
    s = CropFinalizer.crop_score(edges, crop, agg=args.agg)
    print(f"crop score: {s:.6g} (agg={args.agg})")

  # Crop-dependent artifact output
  if args.save_best_crop is not None:
    _save_best_crop(args.save_best_crop, gray, crop)
  
  if args.save_overlay is not None:
    _save_overlay(args.save_overlay, gray, crop)

  if args.phase_sweep:
    _, rel_amp = CropFinalizer.phase_sweep_sanity(
      edges, crop, agg=args.agg, phase_span=args.phase_span
    )
    print(f"phase_sensitivity_rel_amp (grid={args.phase_span}x{args.phase_span}) = {rel_amp:.6g}")

  return 0


if __name__ == "__main__":
  raise SystemExit(main(sys.argv[1:]))
