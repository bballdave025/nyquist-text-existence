# =========================
# End-to-end NTEC pipeline
# CropFinalizer -> Sampler FFT
# Non-overwriting outputs + per-run logs
# Run from: C:\David\my_repos_dwb\nyquist-text-existence\tools\ntec_investigator
# =========================

$INV_DIR  = "C:\David\my_repos_dwb\nyquist-text-existence\tools\ntec_investigator"
$TEST_DIR = "C:\David\my_repos_dwb\nyquist-text-existence\img\dev_figures_init_for_program\_tests"
$OUT_DIR  = "C:\David\my_repos_dwb\nyquist-text-existence\img\dev_figures_init_for_program\_presentation_outs"

$LOG_DIR  = Join-Path $OUT_DIR "logs"
New-Item -ItemType Directory -Force -Path $LOG_DIR | Out-Null


function Get-ImgDims {
  param([Parameter(Mandatory=$true)][string]$Path)

  $dims = python -c "import cv2; p=r'$Path'; im=cv2.imread(p, cv2.IMREAD_GRAYSCALE); print(f'{im.shape[1]} {im.shape[0]}' if im is not None else '0 0')"
  $w,$h = $dims -split ' '

  if ([int]$w -le 0 -or [int]$h -le 0) { throw "Failed to read image: $Path" }

  return @([int]$w, [int]$h)
}


function Run-CropFinalizer {
  param(
    [Parameter(Mandatory=$true)][string]$ImgPath,
    [Parameter(Mandatory=$true)][string]$Tag,
    [Parameter(Mandatory=$true)][int]$CropW,
    [Parameter(Mandatory=$true)][int]$CropH,
    [int]$Step = 8,
    [ValidateSet("mean","sum")][string]$Agg = "mean",
    [int]$SobelK = 3
  )

  $bestcrop = Join-Path $OUT_DIR ("{0}_bestcrop_{1}x{2}.png" -f $Tag,$CropW,$CropH)
  $overlay  = Join-Path $OUT_DIR ("{0}_overlay_{1}x{2}.png"  -f $Tag,$CropW,$CropH)
  $sobmag   = Join-Path $OUT_DIR ("{0}_sobel_mag.png"        -f $Tag)
  $sobbin   = Join-Path $OUT_DIR ("{0}_sobel_bin.png"        -f $Tag)

  $log = Join-Path $LOG_DIR ("{0}_cropfinalizer.txt" -f $Tag)

  Write-Host "`n=== CropFinalizer [$Tag] ==="
  Write-Host "img: $ImgPath"
  Write-Host "crop: ${CropW}x${CropH}  step=$Step  agg=$Agg  k=$SobelK"

  Push-Location $INV_DIR
  try {
    $null = python .\crop_finalizer_cli.py `
      --img $ImgPath `
      --auto-best `
      --crop-w $CropW --crop-h $CropH --step $Step --agg $Agg --sobel-ksize $SobelK `
      --save-best-crop $bestcrop `
      --save-overlay $overlay `
      --save-sobel-mag $sobmag `
      --save-sobel-binary $sobbin `
      2>&1 | Tee-Object -FilePath $log
  }
  finally { Pop-Location }

  if (-not (Test-Path $bestcrop)) { throw "Expected bestcrop not found: $bestcrop" }

  return $bestcrop
}


function Run-SamplerLadder {
  param(
    [Parameter(Mandatory=$true)][string]$CropImgPath,
    [Parameter(Mandatory=$true)][string]$Tag,
    [Parameter(Mandatory=$true)][int[]]$Factors
  )

  $w,$h = Get-ImgDims -Path $CropImgPath

  foreach ($d in $Factors) {

    $stem = if ($d -eq 0) { "${Tag}_orig" } else { "${Tag}_d$d" }

    $save_img = Join-Path $OUT_DIR ("{0}_bigpixels.png"      -f $stem)
    $fft_mag  = Join-Path $OUT_DIR ("{0}_fftmag.png"         -f $stem)
    $fft_cent = Join-Path $OUT_DIR ("{0}_fft_centerline.png" -f $stem)
    $fft_rad  = Join-Path $OUT_DIR ("{0}_fft_radial.png"     -f $stem)
    $log      = Join-Path $LOG_DIR ("{0}_sampler.txt"        -f $stem)

    Write-Host "`n=== Sampler [$stem] ==="
    Write-Host "cropimg: $CropImgPath"
    Write-Host "up-nn: ${w}x${h}"

    if ($d -eq 0) { Write-Host "down: (none)" } else { Write-Host "down: $d" }

    Push-Location $INV_DIR
    try {
      if ($d -eq 0) {
        python .\sampler_cli.py `
          --img $CropImgPath `
          --up-nn $w $h `
          --save-img $save_img `
          --fft `
          --save-fft-mag $fft_mag `
          --save-fft-centerline $fft_cent `
          --save-fft-radial $fft_rad `
          2>&1 | Tee-Object -FilePath $log
      } else {
        python .\sampler_cli.py `
          --img $CropImgPath `
          --down $d `
          --up-nn $w $h `
          --save-img $save_img `
          --fft `
          --save-fft-mag $fft_mag `
          --save-fft-centerline $fft_cent `
          --save-fft-radial $fft_rad `
          2>&1 | Tee-Object -FilePath $log
      }
    }
    finally { Pop-Location }
  }
}


# -------------------------
# Configure runs here
# -------------------------

# 1) anchor (72x988): crop a band, then height-aware ladder
$anchor_img = Join-Path $TEST_DIR "anchor_play_full_res.png"
$anchor_tag = "anchor"
$anchor_cropW = 256
$anchor_cropH = 64
$anchor_step  = 8
$anchor_factors = @(0,2,3,4,6,8,9,12)

# 2) folger fingerprint (1465x1411): crop 256x256 then classic ladder
$folger_img = Join-Path $TEST_DIR "Folger_fingerprint_full_res_2_screens.png"
$folger_tag = "folger_fp"
$folger_cropW = 256
$folger_cropH = 256
$folger_step  = 8
$folger_factors = @(0,2,4,8,16,32)

# 3) montesquieu (179x1125): use your 900x96 crop; step 4 matches your earlier reference
$mont_img = Join-Path $TEST_DIR "full_res_crop_montesquieu_mieux_ennemi_bien.png"
$mont_tag = "montesquieu"
$mont_cropW = 900
$mont_cropH = 96
$mont_step  = 4
$mont_factors = @(0,2,3,4,6,8,12,16)

# 4) wellcome (221x177): crop a moderately square region
$well_img = Join-Path $TEST_DIR "Wellcome_-_MS-438_00374_test_strip_horiz_txt_vert_edge.png"
$well_tag = "wellcome"
$well_cropW = 160
$well_cropH = 160
$well_step  = 8
$well_factors = @(0,2,4,6,8,12,16)

# 5) FamilySearch strip 1
$fs1_img = Join-Path $TEST_DIR "FamilySearch_-_DGS004321734_00003_test_strip_1.png"
$fs1_tag = "fs_dgs004321734_00003_strip1"
$fs1_cropW = 256
$fs1_cropH = 96
$fs1_step  = 8
$fs1_factors = @(0,2,4,6,8,12,16)

# 6) FamilySearch strip 2
$fs2_img = Join-Path $TEST_DIR "FamilySearch_-_DGS004321734_00003_test_strip_2.png"
$fs2_tag = "fs_dgs004321734_00003_strip2"
$fs2_cropW = 256
$fs2_cropH = 96
$fs2_step  = 8
$fs2_factors = @(0,2,4,6,8,12,16)

# 7) FamilySearch lack strip
$fs3_img = Join-Path $TEST_DIR "FamilySearch_-_DGS004321734_00087_test_strip_for_lack.png"
$fs3_tag = "fs_dgs004321734_00087_lack"
$fs3_cropW = 256
$fs3_cropH = 96
$fs3_step  = 8
$fs3_factors = @(0,2,4,6,8,12,16)

# 8) FamilySearch different sizes/darkness strip
$fs4_img = Join-Path $TEST_DIR "FamilySearch_-_DGS008104286_01018_test_strip_difft_sizes_darkness.png"
$fs4_tag = "fs_dgs008104286_01018_sizes_dark"
$fs4_cropW = 256
$fs4_cropH = 96
$fs4_step  = 8
$fs4_factors = @(0,2,4,6,8,12,16)

# 9) FamilySearch horiz text + vert edge strip
$fs5_img = Join-Path $TEST_DIR "FamilySearch_-_DGS0081104286_01108_test_strip_horiz_txt_vert_edge.png"
$fs5_tag = "fs_dgs0081104286_01108_horiz_vert_edge"
$fs5_cropW = 256
$fs5_cropH = 96
$fs5_step  = 8
$fs5_factors = @(0,2,4,6,8,12,16)


# -------------------------
# Execute all pipelines
# -------------------------

$anchor_crop = Run-CropFinalizer -ImgPath $anchor_img -Tag $anchor_tag -CropW $anchor_cropW -CropH $anchor_cropH -Step $anchor_step
Run-SamplerLadder -CropImgPath $anchor_crop -Tag "${anchor_tag}_bestcrop_${anchor_cropW}x${anchor_cropH}" -Factors $anchor_factors


$folger_crop = Run-CropFinalizer -ImgPath $folger_img -Tag $folger_tag -CropW $folger_cropW -CropH $folger_cropH -Step $folger_step
Run-SamplerLadder -CropImgPath $folger_crop -Tag "${folger_tag}_bestcrop_${folger_cropW}x${folger_cropH}" -Factors $folger_factors


$mont_crop = Run-CropFinalizer -ImgPath $mont_img -Tag $mont_tag -CropW $mont_cropW -CropH $mont_cropH -Step $mont_step
Run-SamplerLadder -CropImgPath $mont_crop -Tag "${mont_tag}_bestcrop_${mont_cropW}x${mont_cropH}" -Factors $mont_factors


$well_crop = Run-CropFinalizer -ImgPath $well_img -Tag $well_tag -CropW $well_cropW -CropH $well_cropH -Step $well_step
Run-SamplerLadder -CropImgPath $well_crop -Tag "${well_tag}_bestcrop_${well_cropW}x${well_cropH}" -Factors $well_factors


$fs1_crop = Run-CropFinalizer -ImgPath $fs1_img -Tag $fs1_tag -CropW $fs1_cropW -CropH $fs1_cropH -Step $fs1_step
Run-SamplerLadder -CropImgPath $fs1_crop -Tag "${fs1_tag}_bestcrop_${fs1_cropW}x${fs1_cropH}" -Factors $fs1_factors


$fs2_crop = Run-CropFinalizer -ImgPath $fs2_img -Tag $fs2_tag -CropW $fs2_cropW -CropH $fs2_cropH -Step $fs2_step
Run-SamplerLadder -CropImgPath $fs2_crop -Tag "${fs2_tag}_bestcrop_${fs2_cropW}x${fs2_cropH}" -Factors $fs2_factors


$fs3_crop = Run-CropFinalizer -ImgPath $fs3_img -Tag $fs3_tag -CropW $fs3_cropW -CropH $fs3_cropH -Step $fs3_step
Run-SamplerLadder -CropImgPath $fs3_crop -Tag "${fs3_tag}_bestcrop_${fs3_cropW}x${fs3_cropH}" -Factors $fs3_factors


$fs4_crop = Run-CropFinalizer -ImgPath $fs4_img -Tag $fs4_tag -CropW $fs4_cropW -CropH $fs4_cropH -Step $fs4_step
Run-SamplerLadder -CropImgPath $fs4_crop -Tag "${fs4_tag}_bestcrop_${fs4_cropW}x${fs4_cropH}" -Factors $fs4_factors


$fs5_crop = Run-CropFinalizer -ImgPath $fs5_img -Tag $fs5_tag -CropW $fs5_cropW -CropH $fs5_cropH -Step $fs5_step
Run-SamplerLadder -CropImgPath $fs5_crop -Tag "${fs5_tag}_bestcrop_${fs5_cropW}x${fs5_cropH}" -Factors $fs5_factors


Write-Host "`nDONE. Outputs in: $OUT_DIR"
Write-Host "Logs in: $LOG_DIR"