#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fine-grained NTEC downsampling sweep.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import cv2

from classes_module import SpatialSignalSampler, CropSpec


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Fine-grained downsampling sweep for NTEC image experiments."
    )

    p.add_argument("--input", required=True, help="Input image path")
    p.add_argument("--outdir", required=True, help="Output directory")

    p.add_argument("--factor-start", type=float, default=1.0)
    p.add_argument("--factor-stop", type=float, default=8.0)
    p.add_argument("--factor-step", type=float, default=0.125)

    p.add_argument(
        "--interp",
        choices=["area", "nearest", "cubic"],
        default="area",
        help="OpenCV interpolation mode used for downsampling",
    )

    p.add_argument(
        "--up-interp",
        choices=["nearest", "area", "cubic"],
        default="nearest",
        help="OpenCV interpolation mode used for upsampling back to sweep size",
    )

    p.add_argument(
        "--crop",
        nargs=4,
        type=int,
        metavar=("X", "Y", "W", "H"),
        default=None,
        help="Optional crop before sweep",
    )

    p.add_argument(
        "--prefix",
        default=None,
        help="Optional output filename prefix; defaults to input stem",
    )

    return p.parse_args()


def factor_values(start: float, stop: float, step: float) -> list[float]:
    if start <= 0 or stop <= 0 or step <= 0:
        raise ValueError("factor start/stop/step must be positive.")
    if stop < start:
        raise ValueError("factor-stop must be >= factor-start.")

    vals: list[float] = []
    x = start
    while x <= stop + 1e-9:
        vals.append(round(x, 6))
        x += step
    return vals


def safe_factor_label(factor: float) -> str:
    return f"{factor:08.3f}".replace(".", "p")


def main() -> None:
    args = parse_args()

    input_path = Path(args.input)
    outdir = Path(args.outdir)
    down_dir = outdir / "downsampled"
    downup_dir = outdir / "downsampled_then_upsampled"

    outdir.mkdir(parents=True, exist_ok=True)
    down_dir.mkdir(parents=True, exist_ok=True)
    downup_dir.mkdir(parents=True, exist_ok=True)

    prefix = args.prefix or input_path.stem

    gray = SpatialSignalSampler.load_gray_u8(input_path)

    crop_spec = None
    if args.crop is not None:
        crop_spec = CropSpec(*args.crop)
        gray = SpatialSignalSampler.crop_gray_u8(gray, crop_spec)

    sweep_h, sweep_w = gray.shape[:2]

    csv_path = outdir / f"{prefix}_downsample_sweep.csv"

    interp_map = {
        "area": cv2.INTER_AREA,
        "nearest": cv2.INTER_NEAREST,
        "cubic": cv2.INTER_CUBIC,
    }

    rows = []

    for factor in factor_values(args.factor_start, args.factor_stop, args.factor_step):
        if factor <= 0:
            raise ValueError("factor must be positive.")

        new_w = max(1, int(sweep_w // factor))
        new_h = max(1, int(sweep_h // factor))

        down = cv2.resize(
            gray,
            (new_w, new_h),
            interpolation=interp_map[args.interp],
        )

        downup = cv2.resize(
            down,
            (sweep_w, sweep_h),
            interpolation=interp_map[args.up_interp],
        )

        label = safe_factor_label(factor)

        down_name = f"{prefix}_down_f{label}_{new_w}x{new_h}_{args.interp}.png"
        down_path = down_dir / down_name

        downup_name = (
            f"{prefix}_downup_f{label}_{sweep_w}x{sweep_h}_"
            f"{args.interp}_to_{args.up_interp}.png"
        )
        downup_path = downup_dir / downup_name

        SpatialSignalSampler.save_gray_u8(down_path, down)
        SpatialSignalSampler.save_gray_u8(downup_path, downup)

        rows.append(
            {
                "input": str(input_path),
                "downsampled_output": str(down_path),
                "downsampled_then_upsampled_output": str(downup_path),
                "factor": factor,
                "down_interp": args.interp,
                "up_interp": args.up_interp,
                "sweep_w": sweep_w,
                "sweep_h": sweep_h,
                "out_w": new_w,
                "out_h": new_h,
                "crop_x": "" if crop_spec is None else crop_spec.x,
                "crop_y": "" if crop_spec is None else crop_spec.y,
                "crop_w": "" if crop_spec is None else crop_spec.w,
                "crop_h": "" if crop_spec is None else crop_spec.h,
            }
        )

    if rows:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    print(f"Wrote {len(rows)} downsampled images to: {down_dir}")
    print(f"Wrote {len(rows)} downsampled-then-upsampled images to: {downup_dir}")
    print(f"Wrote CSV log to: {csv_path}")


if __name__ == "__main__":
    main()
