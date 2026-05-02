#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fine-grained NTEC downsampling sweep.

Supports either:
- factor sweep
- target-width sweep
- target-height sweep

Optionally writes a contact sheet from downsampled-then-upsampled outputs.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import cv2
import numpy as np

from classes_module import SpatialSignalSampler, CropSpec


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Fine-grained downsampling sweep for NTEC image experiments."
    )

    p.add_argument("--input", required=True)
    p.add_argument("--outdir", required=True)

    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--factor-sweep", action="store_true")
    mode.add_argument("--target-w-sweep", action="store_true")
    mode.add_argument("--target-h-sweep", action="store_true")

    p.add_argument("--factor-start", type=float, default=1.0)
    p.add_argument("--factor-stop", type=float, default=8.0)
    p.add_argument("--factor-step", type=float, default=0.125)

    p.add_argument("--target-w-start", type=int)
    p.add_argument("--target-w-stop", type=int)
    p.add_argument("--target-w-step", type=int, default=-1)

    p.add_argument("--target-h-start", type=int)
    p.add_argument("--target-h-stop", type=int)
    p.add_argument("--target-h-step", type=int, default=-1)

    p.add_argument(
        "--interp",
        choices=["area", "nearest", "cubic"],
        default="area",
    )

    p.add_argument(
        "--up-interp",
        choices=["nearest", "area", "cubic"],
        default="nearest",
    )

    p.add_argument(
        "--crop",
        nargs=4,
        type=int,
        metavar=("X", "Y", "W", "H"),
        default=None,
    )

    p.add_argument("--prefix", default=None)

    p.add_argument(
        "--make-contact-sheet",
        action="store_true",
        help="Create a contact sheet from downsampled-then-upsampled outputs.",
    )

    p.add_argument(
        "--contact-sheet-cols",
        type=int,
        default=10,
        help="Number of columns in the contact sheet.",
    )

    return p.parse_args()
##endof:  parse_args()


def sweep_values(start: float, stop: float, step: float) -> list[float]:
    if step == 0:
        raise ValueError("step must not be zero.")

    vals: list[float] = []
    x = start

    if step > 0:
        while x <= stop + 1e-9:
            vals.append(round(x, 6))
            x += step
    else:
        while x >= stop - 1e-9:
            vals.append(round(x, 6))
            x += step

    return vals
##endof:  sweep_values(start, stop, step)


def safe_label(value: float | int) -> str:
    if isinstance(value, int):
        return f"{value:04d}"
    return f"{value:08.3f}".replace(".", "p")
##endof:  safe_label(value)


def make_contact_sheet(
    image_paths: list[Path],
    output_path: Path,
    cols: int = 10,
    thumb_w: int = 180,
) -> None:
    if not image_paths:
        return

    if cols <= 0:
        raise ValueError("cols must be positive.")

    thumbs: list[np.ndarray] = []

    for path in image_paths:
        img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        h, w = img.shape[:2]
        if w <= 0 or h <= 0:
            continue

        thumb_h = max(1, int(h * (thumb_w / w)))

        thumb = cv2.resize(
            img,
            (thumb_w, thumb_h),
            interpolation=cv2.INTER_AREA,
        )

        thumbs.append(thumb)
    ##endof:  for path in image_paths

    if not thumbs:
        return

    max_h = max(t.shape[0] for t in thumbs)
    rows = math.ceil(len(thumbs) / cols)

    sheet = np.full(
        (rows * max_h, cols * thumb_w),
        255,
        dtype=np.uint8,
    )

    for idx, thumb in enumerate(thumbs):
        row = idx // cols
        col = idx % cols
        y = row * max_h
        x = col * thumb_w

        sheet[y:y + thumb.shape[0], x:x + thumb.shape[1]] = thumb
    ##endof:  for idx, thumb in enumerate(thumbs)

    ok = cv2.imwrite(str(output_path), sheet)
    if not ok:
        raise IOError(f"Failed to write contact sheet: {output_path}")
##endof:  make_contact_sheet(...)


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

    rows = []
    downup_paths: list[Path] = []

    if args.factor_sweep:
        sweep_kind = "factor"
        values = sweep_values(
            args.factor_start,
            args.factor_stop,
            args.factor_step,
        )
    elif args.target_w_sweep:
        sweep_kind = "target_w"
        if args.target_w_start is None or args.target_w_stop is None:
            raise ValueError(
                "target-width sweep requires --target-w-start and --target-w-stop."
            )
        values = [int(v) for v in sweep_values(
            args.target_w_start,
            args.target_w_stop,
            args.target_w_step,
        )]
    elif args.target_h_sweep:
        sweep_kind = "target_h"
        if args.target_h_start is None or args.target_h_stop is None:
            raise ValueError(
                "target-height sweep requires --target-h-start and --target-h-stop."
            )
        values = [int(v) for v in sweep_values(
            args.target_h_start,
            args.target_h_stop,
            args.target_h_step,
        )]
    else:
        raise ValueError("No sweep mode selected.")
    ##endof:  if/elif/elif/else <sweep mode>

    csv_path = outdir / f"{prefix}_{sweep_kind}_downsample_sweep.csv"

    interp_map = {
        "area": cv2.INTER_AREA,
        "nearest": cv2.INTER_NEAREST,
        "cubic": cv2.INTER_CUBIC,
    }

    for value in values:
        if sweep_kind == "factor":
            down = SpatialSignalSampler.resample_flexible(
                gray,
                factor=float(value),
                interp=args.interp,
            )
            value_label = f"f{safe_label(float(value))}"
        elif sweep_kind == "target_w":
            down = SpatialSignalSampler.resample_flexible(
                gray,
                target_w=int(value),
                interp=args.interp,
            )
            value_label = f"tw{safe_label(int(value))}"
        else:
            down = SpatialSignalSampler.resample_flexible(
                gray,
                target_h=int(value),
                interp=args.interp,
            )
            value_label = f"th{safe_label(int(value))}"
        ##endof:  if/elif/else <sweep kind>

        out_h, out_w = down.shape[:2]

        downup = cv2.resize(
            down,
            (sweep_w, sweep_h),
            interpolation=interp_map[args.up_interp],
        )

        down_name = (
            f"{prefix}_down_{value_label}_{out_w}x{out_h}_{args.interp}.png"
        )
        down_path = down_dir / down_name

        downup_name = (
            f"{prefix}_downup_{value_label}_{sweep_w}x{sweep_h}_"
            f"{args.interp}_to_{args.up_interp}.png"
        )
        downup_path = downup_dir / downup_name

        SpatialSignalSampler.save_gray_u8(down_path, down)
        SpatialSignalSampler.save_gray_u8(downup_path, downup)

        downup_paths.append(downup_path)

        rows.append(
            {
                "input": str(input_path),
                "downsampled_output": str(down_path),
                "downsampled_then_upsampled_output": str(downup_path),
                "sweep_kind": sweep_kind,
                "sweep_value": value,
                "down_interp": args.interp,
                "up_interp": args.up_interp,
                "sweep_w": sweep_w,
                "sweep_h": sweep_h,
                "out_w": out_w,
                "out_h": out_h,
                "crop_x": "" if crop_spec is None else crop_spec.x,
                "crop_y": "" if crop_spec is None else crop_spec.y,
                "crop_w": "" if crop_spec is None else crop_spec.w,
                "crop_h": "" if crop_spec is None else crop_spec.h,
            }
        )
    ##endof:  for value in values

    if rows:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        ##endof:  with csv_path.open(...) as f
    ##endof:  if rows

    if args.make_contact_sheet:
        contact_sheet_path = outdir / f"{prefix}_{sweep_kind}_contact_sheet.png"
        make_contact_sheet(
            image_paths=downup_paths,
            output_path=contact_sheet_path,
            cols=args.contact_sheet_cols,
        )
        print(f"Wrote contact sheet to: {contact_sheet_path}")
    ##endof:  if args.make_contact_sheet

    print(f"Wrote {len(rows)} downsampled images to: {down_dir}")
    print(f"Wrote {len(rows)} downsampled-then-upsampled images to: {downup_dir}")
    print(f"Wrote CSV log to: {csv_path}")
##endof:  main()


if __name__ == "__main__":
    main()
##endof:  if __name__ == "__main__"
