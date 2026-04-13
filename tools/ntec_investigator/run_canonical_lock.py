#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file: run_canonical_lock.py
@author: David Black   GitHub @bballdave025
@since: 2026-04-13

Dependencies:
  - numpy
  - cv2
'''

import sys
from datetime import datetime

import numpy as np
import cv2

from classes_module import \
         CropSpec, CropFinalizer, SpatialSignalSampler

def run_canonical_lock():
  # 1. Setup
  sampler = SpatialSignalSampler()
  finalizer = CropFinalizer()
  
  # Path to your native resolution Image B
  img_path = (
    'C:\\David\my_repos_dwb\\nyquist-text-existence\\img\\'
    'canonical_crop_imgB_process\\'
    'FamilySearch_-_DGS004534287_00361.jpg'
  )
  img = sampler.load_gray_u8(img_path)
  H_img, W_img = img.shape
  
  # 2. The Physics Shake (Seed 137: 
  #    Negative, Inverse Fine-Structure Constant)
  rng = np.random.default_rng(137)
  
  # Initial MCC Coordinates (Unshaken). Picked by Dave
  DWB_X_INIT = 2975
  DWB_Y_INIT = 40
  DWB_W_INIT = 1425
  DWB_H_INIT = 375
  x_init, y_init = DWB_X_INIT, DWB_Y_INIT
  w_init, h_init = DWB_W_INIT, DWB_H_INIT
  mcc_init = CropSpec(x_init, y_init, w_init, h_init)
  
  x_init_max = x_init + w_init
  y_init_max = y_init + h_init
  
  # Use the formalized class method to ensure parity with Addendum 1 description
  mcc_shaken = CropFinalizer.generate_unbiased_mcc(
    mcc_init, 
    (H_img, W_img), 
    seed=137
  )
  
  shkn_mcc_x_min = mcc_shaken.x
  shkn_mcc_y_min = mcc_shaken.y
  shkn_mcc_w     = mcc_shaken.w
  shkn_mcc_h     = mcc_shaken.h
  
  shkn_mcc_x_max = shkn_mcc_x_min + shkn_mcc_w
  shkn_mcc_y_max = shkn_mcc_y_min + shkn_mcc_h
  
  # 3. Deterministic Sobel Ranking (The NTEC Finalizer)
  # Target Dimensions: 192x64 = 3 * 2^6 x 2^6
  target_w, target_h = 192, 64
  mcc_patch = sampler.crop_gray_u8(img, mcc_shaken)
  edges = finalizer.sobel_mag(mcc_patch)
  
  # step=1 ensures we check every possible pixel for the canonical lock
  best_rel, score = finalizer.best_crop_on_grid(
    edges, w=target_w, h=target_h, step=1, agg='mean'
  )
  
  # 4. Project back to Global Coordinates
  canonical_crop_x_min = mcc_shaken.x + best_rel.x
  canonical_crop_y_min = mcc_shaken.y + best_rel.y
  canonical_crop_w = target_w
  canonical_crop_h = target_h
  
  canonical_crop_x_max = canonical_crop_x_min + canonical_crop_w
  canonical_crop_y_max = canonical_crop_y_min + canonical_crop_h
  
  canonical_global = CropSpec(
    x=canonical_crop_x_min,
    y=canonical_crop_y_min,
    w=target_w,
    h=target_h
  )
  
  print(f"--- NTEC ADDENDUM 1: FINAL LOCK REPORT ---")
  print(f"Image B Native Path: {img_path}")
  print(f"Shaking MCC Initial Seed: 137")
  print(f"Shaken MCC: {mcc_shaken}")
  print(f"Locked Canonical Crop: {canonical_global}")
  print(f"Sobel Energy Score: {score:.6f}")
  print()
  print("Other Details")
  
  pre_shaking_str = (
     "Pre-shaking Region (pre-MCC): "
    f"X={x_init}, Y={y_init}, W={w_init}, H={h_init}"
  )
  
  print(pre_shaking_str)
  
  shaken_string = (
     "Shaken MCC:                   "
    f"X={shkn_mcc_x_min}, Y={shkn_mcc_y_min}, "
    f"W={shkn_mcc_w}, H={shkn_mcc_h}"
  )
  
  now = datetime.now().astimezone()
  timestamp = now.strftime("%Y-%m-%dT%H%M%S%z")
  
  print(f"Calculated and Locked: {timestamp}")
  
  print()
  
  # ----------------------------
  # Let's output our MCC region
  mcc_img_path = (
     'C:\\David\\my_repos_dwb\\nyquist-text-existence\\img\\'
     'canonical_crop_imgB_process\\'
     'canonical_crop_out\\'
    f'Image_B_MCC_-_Shaken_{timestamp}.png'
  )
  
  # Save the shaken MCC region (crop)
  
  # read in
  try:
    img = cv2.imread(img_path)
  except Exception as ex:
    print(f"imread fail for {img_path}",     file=sys.stderr)
    print(f"Exception details:\n{str(ex)}",  file=sys.stderr)
    raise(ex)
  finally:
    pass
  ##endof:  try/except/finally <cv2 read image>
  
  mcc_img=img[
    shkn_mcc_y_min:shkn_mcc_y_max,
    shkn_mcc_x_min:shkn_mcc_x_max
  ]
  
  # read out
  try:
    cv2.imwrite(mcc_img_path, mcc_img)
    print(f"Shaken MCC for Image B saved to\n  {mcc_img_path}")
  except Exception as ex:
    print(f"imwrite fail for {mcc_img_path}", file=sys.stderr)
    print(f"Exception details:\n{str(ex)}", file=sys.stderr)
    raise(ex)
  finally:
    pass
  ##endof:  try/except/finally <cv2 write mcc image>
  
  print()
  
  # ----------------------------------------
  # Let's output our canonical crop's image
  out_img_path = (
     'C:\\David\\my_repos_dwb\\nyquist-text-existence\\img\\'
     'canonical_crop_imgB_process\\'
     'canonical_crop_out\\'
    f'Image_B_Canonical_Crop_-_Locked_{timestamp}.png'
  )
  
  # Save the final, locked canonical crop
  
  # read in
  try:
    img = cv2.imread(img_path)
  except Exception as ex:
    print(f"imread fail for {img_path}", file=sys.stderr)
    print(f"Exception details:\n{str(ex)}", file=sys.stderr)
    raise(ex)
  finally:
    pass
  ##endof:  try/except/finally <cv2 read image>
  
  cropped_img=img[
    canonical_crop_y_min:canonical_crop_y_max,
    canonical_crop_x_min:canonical_crop_x_max
  ]
  
  # read out
  try:
    cv2.imwrite(out_img_path, cropped_img)
    print(f"Canonical Crop for Image B saved to\n  {out_img_path}")
  except Exception as ex:
    print(f"imwrite fail for {out_img_path}", file=sys.stderr)
    print(f"Exception details:\n{str(ex)}", file=sys.stderr)
    raise(ex)
  finally:
    pass
  ##endof:  try/except/finally <cv2 write canonical crop image>

if __name__ == '__main__':
  run_canonical_lock()