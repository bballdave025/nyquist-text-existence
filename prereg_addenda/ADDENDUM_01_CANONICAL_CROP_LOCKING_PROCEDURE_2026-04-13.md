# Addendum 1 — Canonical Crop Locking Procedure (Image B)

**Project:** Nyquist Text Existence Criterion (NTEC)  
**Author:** David Black (GitHub @bballdave025)  
**Date Locked:** 2026-04-13T18:22:26−0400  
**Status:** Confirmatory (post-preregistration addendum)

---

## 1. Purpose

This addendum establishes a confirmatory locking procedure for Image B in the NTEC project.

Its purpose is to:
- prevent outcome-driven selection within a candidate-containing region,
- define a reproducible method for selecting a single canonical crop, and
- formally separate exploratory identification from confirmatory evaluation.

This procedure implements a **seeded stochastic perturbation followed by deterministic selection**, ensuring that the final crop is not influenced by post hoc tuning.

---

## 2. Initial Region Selection (Pre-Confirmatory Step)

An initial **Multiple-Candidate-Containing (MCC)** region was selected by the author (David Black) based on visual inspection of Image B, with the goal of including multiple plausible stroke-like structures.

This selection is:
- **explicitly pre-confirmatory**, and
- **not used to determine the final crop directly**.

All subsequent steps remove degrees of freedom from this initial choice.

---

## 3. Locking Procedure

The canonical crop is obtained via a two-stage process:

### Stage 1 — Seeded stochastic perturbation

The initial MCC region is perturbed using a stochastic transformation defined as follows:

- Gaussian coordinate perturbation, with the x-coordinate perturbed using a normal distribution with standard deviation 10% of the MCC width, and the y-coordinate perturbed using a normal distribution with standard deviation 10% of the MCC height
- Independent multiplicative scaling of each dimension by a factor in [0.95, 1.05]
- Random number generator initialized with seed 137 (for reproducibility)

The perturbation is applied to the MCC region only; the canonical crop size remains fixed.

This produces a **shaken MCC region** that is:
- stochastic in construction,
- but fully deterministic and reproducible given the seed.

This perturbation step refines the preregistered candidate-region specification by introducing a seed-fixed transformation prior to deterministic crop selection, without introducing outcome-dependent degrees of freedom.

---

### Stage 2 — Deterministic Crop Selection

From the shaken MCC region, a single crop is selected using a deterministic scoring procedure:

- Metric: Sobel gradient magnitude
- Aggregation: mean over the crop
- Stride: step = 1
- Selection rule: argmax over all candidate crops of fixed size

The Sobel-based scoring function is:
- fixed prior to execution, and
- used solely as a **necessary-condition filter for gradient presence**, not as a recognition, classification, or transcription mechanism.

---

## 4. Fixed Parameters

| Parameter   | Value |
|:------------|:------|
| Crop size   | 192 × 64 |
| Step size   | 1 |
| Aggregation | mean |
| RNG seed    | 137 |

The crop dimensions were chosen to:
- provide a nontrivial rectangular aspect ratio, and
- allow repeated factorization by 2 (six times per dimension), facilitating later downsampling experiments.

---

## 5. Execution Results

| Metric | Value |
|:------|:------|
| Initial MCC | `x=2975, y=40, w=1425, h=375` |
| Shaken MCC | `x=2885, y=40, w=1476, h=366` |
| Locked Canonical Crop (full image) | `x=3364, y=209, w=192, h=64` |
| Locked Canonical Crop (relative to MCC) | `x=479, y=169, w=192, h=64` |
| Sobel Energy Score | `116.082024` |

Coordinates use the convention that (x, y) denotes the top-left pixel, and (w, h) denote width and height. All coordinates are given relative to the full image unless otherwise indicated.

---

## 6. Evidence Witness

The locked canonical crop is preserved as a **digital evidence witness**.

**Native resolution (192×64):**

<img src="https://raw.githubusercontent.com/bballdave025/nyquist-text-existence/refs/heads/addendum-1-lock/img/canonical_crop_imgB_process/canonical_crop_out/Image_B_Canonical_Crop_-_Locked_2026-04-13T182226-0400.png" width="192" style="image-rendering: pixelated;">

**Pixel-enlarged visualization (4×):**

<img src="https://raw.githubusercontent.com/bballdave025/nyquist-text-existence/refs/heads/addendum-1-lock/img/canonical_crop_imgB_process/canonical_crop_out/Image_B_Canonical_Crop_-_Locked_big_pix_04x.png" width="768">

This pixel-enlarged visualization is provided to expose the sampled structure without interpolation. The image is upsampled using nearest-neighbor interpolation by a factor of 4; in the underlying image data, each pixel in the native-resolution canonical crop is represented by a 4×4 block of identical pixels. Apparent deviations from this structure in rendered views may occur due to display or PDF rescaling.

A self-contained HTML (base64-encoded) version is archived at:

`REPO_ROOT/img/canonical_crop_imgB_process/canonical_crop_out/ Image_B_Canonical_Crop_-_Locked_2026-04-13T182226-0400.html`

---

## 7. Verification and Quarantine

The canonical crop:
- was selected deterministically from the shaken MCC region, and
- is now quarantined.

No further:
- metric tuning,
- parameter adjustment, or
- exploratory analysis

will be run on or applied to this region prior to confirmatory evaluation.

---

## 8. Epistemic Boundary Note

This procedure is designed to enforce a confirmatory firewall consistent with the preregistration (§1, §10).

- The initial MCC selection is separated from the locking mechanism.
- The stochastic perturbation reduces alignment bias.
- The deterministic selector removes researcher degrees of freedom.

The result is a single, reproducibly defined canonical crop that can be used for confirmatory testing without risk of outcome-driven selection.

---

## 9. Submission Note

This addendum documents the transition from:
- theoretical specification  
to  
- locked experimental input.

It is intended for archival in OSF as part of the preregistered workflow.

---

_End of Addendum 1_
