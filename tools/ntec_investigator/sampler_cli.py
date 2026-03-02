#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file : sampler_cli.py
@author : Dave Black  GitHub @bballdave025
@since: 2026-02-27

Minimal CLI harness for hook-slide artifact generation:
- Crop (optional)
- Downsample (optional, strict integer factor)
- Upsample-to-size with nearest neighbor for "big pixels" view (optional)
- FFT magnitude (computed on the *pre-upsample* resolution unless you don't upsample)

New stuff for sprints, 2025-03-01
  ...
"""

from __future__ import annotations

import argparse
from pathlib import Path

from typing import Tuple

import numpy as np

from classes_module import CropSpec, SpatialSignalSampler


def _validate_output_path(path_str: str) -> None:
  p = Path(path_str)
  if p.suffix == "":
    raise ValueError(f"Output path must include a filename with extension: {path_str}")
  if not p.parent.exists():
    raise FileNotFoundError(f"Directory does not exist: {p.parent}")


def _parse_args() -> argparse.Namespace:
  p = argparse.ArgumentParser(description="NTEC SpatialSignalSampler CLI (hook-slide artifacts)")

  p.add_argument("--img", required=True, help="Input image path (grayscale read).")

  p.add_argument(
    "--crop",
    nargs=4,
    type=int,
    metavar=("X", "Y", "W", "H"),
    help="Optional crop (x y w h). Default: full image.",
  )

  p.add_argument(
    "--down",
    type=int,
    default=None,
    help="Optional integer downsample factor (e.g., 32 for 256->8).",
  )

  p.add_argument(
    "--up-nn",
    nargs=2,
    type=int,
    metavar=("OUT_W", "OUT_H"),
    default=None,
    help="Optional upsample (nearest) to exact size (e.g., 256 256 for big pixels).",
  )

  p.add_argument(
    "--save-img",
    type=str,
    default=None,
    help="Path to save the post-resample image (uint8).",
  )

  p.add_argument(
    "--fft",
    action="store_true",
    help="If set, compute FFT magnitude of the working image *before* --up-nn.",
  )

  p.add_argument(
    "--save-fft-mag",
    type=str,
    default=None,
    help="Path to save FFT magnitude image.",
  )
  
  p.add_argument(
    "--save-fft-centerline",
    type=str,
    default=None,
    help="Optional: save 1D centerline FFT profiles (row+col) as a PNG.",
  )

  p.add_argument(
    "--save-fft-radial",
    type=str,
    default=None,
    help="Optional: save radial-mean FFT profile as a PNG.",
  )

  p.add_argument("--log1p", action="store_true", default=True, help="Log1p compress FFT mag (default on).")
  p.add_argument("--no-log1p", dest="log1p", action="store_false", help="Disable log1p compression.")
  p.add_argument("--no-shift", dest="shift", action="store_false", default=True, help="Disable fftshift.")
  p.add_argument("--no-normalize", dest="normalize", action="store_false", default=True, help="Disable normalization.")

  return p.parse_args()


def _ensure_parent_dir_exists(path_str: str) -> None:
  p = Path(path_str)
  if p.parent and not p.parent.exists():
    raise FileNotFoundError(f"Directory does not exist: {p.parent}")


def _plot_centerline_profiles_png(path_str: str, mag2d: np.ndarray, title: str) -> None:
  """
  Save a single PNG containing two 1D profiles:
    - horizontal center row
    - vertical center column
  
  Kept in the CLI helper, because they are more for pretty plots
  used in presentations and such.
  """
  if mag2d.ndim != 2:
    raise ValueError("mag2d must be 2D.")

  # Normalize for plotting only (keeps shape; avoids huge y-axis)
  x = mag2d.astype(np.float32, copy=False)
  finite = np.isfinite(x)
  if not np.any(finite):
    raise ValueError("mag2d has no finite values to plot.")
  mx = float(np.max(x[finite]))
  if mx <= 0:
    mx = 1.0
  x = x / mx

  H, W = x.shape
  r = x[H // 2, :]          # horizontal center row
  c = x[:, W // 2]          # vertical center col

  import matplotlib.pyplot as plt  #  lazy import to reduce startup
                                   #+ costs unless used.
  plt.figure()
  plt.plot(r, label="center row (horizontal)")
  plt.plot(c, label="center col (vertical)")
  plt.title(title)
  plt.xlabel("index (pixels in FFT grid)")
  plt.ylabel("normalized magnitude (arb.)")
  plt.legend()
  _ensure_parent_dir_exists(path_str)
  plt.savefig(path_str, dpi=150, bbox_inches="tight")
  plt.close()


def _radial_profile(mag2d: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
  """
  Radial mean of a 2D magnitude image around its center.
  Returns:
    radii (int bins) and mean magnitude per radius bin.
  """
  if mag2d.ndim != 2:
    raise ValueError("mag2d must be 2D.")

  x = mag2d.astype(np.float32, copy=False)
  finite = np.isfinite(x)
  if not np.any(finite):
    raise ValueError("mag2d has no finite values.")

  H, W = x.shape
  cy = (H - 1) / 2.0
  cx = (W - 1) / 2.0

  yy, xx = np.indices((H, W))
  rr = np.sqrt((yy - cy) ** 2 + (xx - cx) ** 2)
  rbin = rr.astype(np.int32)

  # Only use finite values
  rbin_f = rbin[finite]
  x_f = x[finite]

  rmax = int(rbin_f.max()) if rbin_f.size else 0
  sums = np.bincount(rbin_f.ravel(), weights=x_f.ravel(), minlength=rmax + 1)
  counts = np.bincount(rbin_f.ravel(), minlength=rmax + 1).astype(np.float32)

  means = np.zeros_like(sums, dtype=np.float32)
  nz = counts > 0
  means[nz] = (sums[nz] / counts[nz]).astype(np.float32)

  radii = np.arange(means.size, dtype=np.int32)
  return radii, means


def _plot_radial_profile_png(path_str: str, mag2d: np.ndarray, title: str) -> None:
  radii, means = _radial_profile(mag2d)

  # Normalize for plotting only
  finite = np.isfinite(means)
  if not np.any(finite):
    raise ValueError("radial means has no finite values.")
  mx = float(np.max(means[finite]))
  if mx <= 0:
    mx = 1.0
  y = means / mx

  import matplotlib.pyplot as plt  #  lazy import to reduce startup
                                   #+ costs unless used.
  plt.figure()
  plt.plot(radii, y)
  plt.title(title)
  plt.xlabel("radius (pixels in FFT grid)")
  plt.ylabel("normalized mean magnitude (arb.)")
  _ensure_parent_dir_exists(path_str)
  plt.savefig(path_str, dpi=150, bbox_inches="tight")
  plt.close()







def main() -> int:
  args = _parse_args()

  img_path = Path(args.img)
  gray = SpatialSignalSampler.load_gray_u8(img_path)

  crop = None
  if args.crop is not None:
    x, y, w, h = args.crop
    crop = CropSpec(x=x, y=y, w=w, h=h)
    gray = SpatialSignalSampler.crop_gray_u8(gray, crop)

  working = gray

  # Downsample (area)
  if args.down is not None:
    if args.down <= 0:
      raise ValueError("--down must be positive.")
    working = SpatialSignalSampler.resample_gray_u8(working, mode="down", factor=int(args.down), interp="area")

  ##  FFT is computed on the working resolution BEFORE
  ##+ upsampling to big pixels for slide viewing
  
  # FFT-related outputs (2D mag image and/or 1D profiles)
  want_fft_mag = args.fft
  want_centerline = args.save_fft_centerline is not None
  want_radial = args.save_fft_radial is not None

  if want_fft_mag or want_centerline or want_radial:
    # enforce save paths where needed
    if want_fft_mag:
      if args.save_fft_mag is None:
        raise ValueError("--fft set but --save-fft-mag not provided.")
      _validate_output_path(args.save_fft_mag)
    if want_centerline:
      _validate_output_path(args.save_fft_centerline)
    if want_radial:
      _validate_output_path(args.save_fft_radial)

    f = SpatialSignalSampler.fft2(SpatialSignalSampler.to_float01(working))

    # For the 2D mag image, use your existing normalization options.
    mag_img = SpatialSignalSampler.fft_mag(
      f,
      shift=bool(args.shift),
      log1p=bool(args.log1p),
      normalize=bool(args.normalize),
    )

    if want_fft_mag:
      SpatialSignalSampler.save_float_image(args.save_fft_mag, mag_img)

    # For 1D plots, we want *shape* not absolute scaling; use a non-normalized mag.
    # (We normalize only for plotting.)
    mag_for_profiles = SpatialSignalSampler.fft_mag(
      f,
      shift=bool(args.shift),
      log1p=bool(args.log1p),
      normalize=False,
    )

    if want_centerline:
      _plot_centerline_profiles_png(
        args.save_fft_centerline,
        mag_for_profiles,
        title="FFT magnitude centerline profiles",
      )

    if want_radial:
      _plot_radial_profile_png(
        args.save_fft_radial,
        mag_for_profiles,
        title="FFT magnitude radial mean profile",
      )

  # Optional big-pixel visualization: upsample to exact size using NN.
  out_img = working
  if args.up_nn is not None:
    out_w, out_h = args.up_nn
    out_img = SpatialSignalSampler.resize_to(out_img, out_w=out_w, out_h=out_h, interp="nearest")

  if args.save_img is not None:
    _validate_output_path(args.save_img)
    SpatialSignalSampler.save_gray_u8(args.save_img, out_img)

  return 0


if __name__ == "__main__":
  raise SystemExit(main())
