#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
'''
@file : crop_finalizer_cli.py
@author : David Black   GitHub @bballdave025
          with ChatGPT (whatever version) as AI coding helper
@since : 2026-02-26

@brief : LATER!!! I ERP-ed the h-bar out of that!
'''

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from classes_module import CropFinalizer, CropSpec


def parse_args(argv: list[str]) -> argparse.Namespace:
  p = argparse.ArgumentParser(
    description="CLI bridge for CropFinalizer (class-based parity harness)."
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

  gray = CropFinalizer.load_gray_u8(args.img)
  edges = CropFinalizer.sobel_mag(gray, ksize=args.sobel_ksize)

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

  if args.phase_sweep:
    _, rel_amp = CropFinalizer.phase_sweep_sanity(
      edges, crop, agg=args.agg, phase_span=args.phase_span
    )
    print(f"phase_sensitivity_rel_amp (grid={args.phase_span}x{args.phase_span}) = {rel_amp:.6g}")

  return 0


if __name__ == "__main__":
  raise SystemExit(main(sys.argv[1:]))