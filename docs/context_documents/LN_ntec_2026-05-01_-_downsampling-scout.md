CONTEXT DOCUMENT for continuation of the "NTEC synthetic and manuscript downsampling scout — informal visual experiments for observing when periodic substrate structures, watermarks, weave, and true stroke signals disappear, alias, or become inadmissable as evidence under downsampling" project

DOCUMENT PREPARED FOR CONTINUATION: 

1777689001_2026-05-01T22:30:01-0400

date +'%s_%Y-%m-%dT%H:%M:%S%z'  # use current Boston, MA time zone

CONTINUED FROM CHAT ENTITLED:
C++ Jupyter Config Class (ChatGPT didn't catch that I wanted
ALSO INVOLVING
`NTEC, RMFB, Nyquist Text Existence, Bordeaux weave, watermark downsampling, Moiré scout experiments`

FROM USER thebballdave025@gmail.com

---

## Project State

This session shifted into an NTEC-related visual intake/scouting task.

The goal was not formal proof or polished experimentation. The goal was to look at downsampling behavior in manuscript and synthetic images while staying mostly in “observe-only” mode.

The relevant NTEC framing was:

> When information has been destroyed by sampling, it does not exist in the digitized image.

The important extension noticed here was:

> Downsampling may not only remove true writing or watermark evidence; it may also introduce aliasing or Moiré-like structures from periodic substrate features such as paper weave.

This creates a second evidentiary problem:

```text
true writing signal may disappear
while non-writing substrate structure may become stroke-like
```

---

## Conceptual Observations

Several manuscript/rag-paper images were discussed.

Important visual categories:

- true writing signal
- watermark signal
- rag-paper weave / substrate signal
- high-contrast specks or stains
- possible aliasing/Moiré artifacts after downsampling

A page with “153” and visible weave was selected for an initial sweep and named:

```text
weave_153.png
```

The provenance is captured in the original filename: 

`BibMunBordeauxMeriadeck_-_Reflections_et_pensees_de_Montaigne_MS-1866-1_00157.png`

Repository: La Bibliothèque municipale de Bordeaux, Meriadeck
Title: _Réflections et pensées de Montaigne_
Shelfmark: MS 1866-1
Image number in digitization: 157


The first sweep covered factors:

```text
1.0 → 8.0
step 0.125
interp area
```

The second sweep covered:

```text
8.125 → 16.0
step 0.125
interp area
```

No obvious Moiré or stroke-like aliasing was seen in those first two visual inspections.

---

## Important Methodological Note

OpenCV grayscale loading was used:

```python
cv2.imread(path, cv2.IMREAD_GRAYSCALE)
```

Some outputs may visually seem parchment-toned or color-like on a phone display, but the generated outputs are grayscale if the pipeline is run as written.

A quick sanity check is:

```python
img.ndim == 2
```

If true, the image is single-channel grayscale.

---

## Existing Supporting Code

The shared `classes_module.py` includes:

- `CropSpec`
- `SpatialSignalSampler`
- `CropFinalizer`

Key `SpatialSignalSampler` functions used or relevant:

```python
load_gray_u8(...)
crop_gray_u8(...)
save_gray_u8(...)
resample_flexible(...)
```

A bug was noted and fixed in `resample_flexible(...)`:

```python
return cv2.resize(...)
```

was indented inside the `target_h` branch. It needed be dedented so that it applies after all three modes:

```text
factor
target_w
target_h
```

Also, `Optional` was used but not imported in the pasted version. Fixed with `from typing import Optional`.

---

## Downsampling CLI v1

The original CLI, `sweep_downsample.py`, supported factor sweeps.

It originally used:

```python
round(sweep_w / factor)
round(sweep_h / factor)
```

This was corrected back to floored division behavior, consistent with the desired NTEC linear reduction logic:

```python
new_w = max(1, int(sweep_w // factor))
new_h = max(1, int(sweep_h // factor))
```

---

## Downsampling CLI v2

Additions to the CLI were made and committed.

Purpose:

- preserve `factor` sweep behavior
- add `target_w` sweep behavior
- add `target_h` sweep behavior
- avoid duplicate-width factor artifacts
- support clean synthetic scout experiments

The key new modes are mutually exclusive:

```text
--factor-sweep
--target-w-sweep
--target-h-sweep
```

Example target-width sweep:

```bash
python sweep_downsample.py \
  --input ./stark_zebra_100.png \
  --outdir ./outputs/downsample_sweep/stark_value_0 \
  --target-w-sweep \
  --target-w-start 99 \
  --target-w-stop 1 \
  --target-w-step -1 \
  --interp area
```

PowerShell equivalent:

```powershell
python .\sweep_downsample.py `
  --input .\stark_zebra_100.png `
  --outdir .\outputs\downsample_sweep\stark_value_0 `
  --target-w-sweep `
  --target-w-start 99 `
  --target-w-stop 1 `
  --target-w-step -1 `
  --interp area
```

---

## Synthetic Scout Image

A synthetic image was generated:

```text
stark_zebra_100.png
```

Specification:

- 100 pixels wide
- 1000 pixels tall
- vertical stripes
- stripe width: 5 pixels
- alternating black and white
- pixel values:
  - white = 255
  - black = 0

The initial hypothesis was that this highly symmetric case may show little or no Moiré behavior unless rotated, warped, jittered, or otherwise made less ideal.

---

## Generated Scout Outputs

A target-width sweep from width 99 down to width 1 was run on:

```text
stark_zebra_100.png
```

Outputs included:

- 99 downsampled images
- 99 downsampled-then-upsampled images
- CSV log
- contact sheet

The user wants the contact sheet as the next commit goal.

A “contact sheet” in this context means:

```text
one single image containing a tiled grid of many sweep outputs
```

Purpose:

- quickly inspect transitions
- avoid opening 99 images one by one
- provide one Git-friendly representative visual artifact

This will be set up in a follow-up commit.
---

## Possible Next Experiment Directions

Do not overbuild yet.

Likely next scouts:

1. contact sheet for stark zebra target-width sweep
2. rotated zebra pattern
3. noisy / jittered zebra pattern
4. gradient-softened zebra pattern
5. manuscript weave crop with contrast-boost scout
~~6. area vs nearest vs cubic comparator~~

We want to keep our interpolation consistent.

Important distinction:

```text
contrast-boosted or nearest-neighbor outputs are scout tools,
not evidentiary proof
```

---

## Very synthetic

Create synthetic zebra (from ChatGPT) and run target-width sweep.

**Most important part of prompt**

> Let's make this really scout-y. Let's take an ideal image, 100 px wide by 1000 px tall. I was going to say let's do small random distortions or a gradient between dark and light, but let's make things stark. I want vertical lines five pixels wide, where pixel value is only a function of $x$. For the first five pixels, the pixel value are all 255, for the second five, the values are all 0, for the third five, the values are all 255, etc. Call the image `stark_zebra_100.png`.


**Other scientifically important parts of prompt: 

> Let's make this really scout-y. Let's take an ideal image, 100 px wide by 1000 px tall. I was going to say let's do small random distortions or a gradient between dark and light, but let's make things stark. I want vertical lines five pixels wide, where pixel value is only a function of $x$. For the first five pixels, the pixel value are all 256, for the second five, the values are all 0, for the third five, the values are all 256, etc. Call the image `stark_zebra_100.png`. Rather than mess with the factor nonsense, let's go with my favorite fine-tunable resolution tool. We can go with downsampling to a width of 99 pixels all the way down to a width of 1 pixel -- 99 images (rather than something like going with a factor of 1 to 100 in increments of 0.2 and having 99*5 images, a bunch of which would have duplicate widths.)
> 
> (Now, we are very isotropic in one direction, just about as much as we can be. We will probably have to wonky-ize the lines with gradients, noisy jitter around ideal values, different, non-infinite slopes for each line and/or for different parts of each line, etc.)
> ...
> ~~Where the stark value being 1 means the max of \[0,1\], maybe of \[-1,1\], because what I thought of as zero starkness could be all black or could be all white.~~ Maybe the `anti_starkness` could be 0 in my example and the range of `anti_starkness` could be \[-1,1\], and you'll have to change my command and give me a nice way of gradating this.
>
> My hypothesis is that we will see absolutely nothing in the Moirée department (due to high symmetry,) but that if we rotate it our stripes, we should be able to get some aliasing after downsampling. (I'm not sure if 5° or 45° will be better, and I'm working hard to ERP my mind away from deriving...) I think that the parallel case would actually be $f_{Moiré} = \frac{f_1 \cdot f_2}{f_1 \pm f_2}$ because... waves&beats, and it's probably minus and an absolute value around the denominator. And we see the problem with our highly symmetric thing $f_1 = n \cdot f_2, n \elem \mathcal{Z}$ ($\mathbb{Z}$? I'm talking about the integers.)
> 
> I'm also trying not to, but I'm thinking... that two gratings of the same frequency probably do a thing like $f_{Moiré} = \frac{f}{sin\left(\theta\right)}$, or probably the argument of the sine should be 2θ or θ/2.

## Bash Commands

Set executable bit on Linux/macOS:

```bash
chmod +x sweep_downsample.py
```

```bash
python sweep_downsample.py \
  --input ./stark_zebra_100.png \
  --outdir ./outputs/downsample_sweep/stark_value_1 \
  --target-w-sweep \
  --target-w-start 99 \
  --target-w-stop 1 \
  --target-w-step -1 \
  --interp area
```

Run original weave image factor sweep, first range:

```bash
python sweep_downsample.py \
  --input ./weave_153.png \
  --outdir ./outputs/downsample_sweep \
  --factor-sweep \
  --factor-start 1.0 \
  --factor-stop 8.0 \
  --factor-step 0.125 \
  --interp area
```

Run original weave image factor sweep, second range:

```bash
python sweep_downsample.py \
  --input ./weave_153.png \
  --outdir ./outputs/downsample_sweep \
  --factor-sweep \
  --factor-start 8.125 \
  --factor-stop 16.0 \
  --factor-step 0.125 \
  --interp area
```

---

## PowerShell Commands

Run target-width sweep:

```powershell
python .\sweep_downsample.py `
  --input .\stark_zebra_100.png `
  --outdir .\outputs\downsample_sweep\stark_value_1 `
  --target-w-sweep `
  --target-w-start 99 `
  --target-w-stop 1 `
  --target-w-step -1 `
  --interp area
```

Run original weave image factor sweep, first range:

```powershell
python .\sweep_downsample.py `
  --input .\weave_153.png `
  --outdir .\outputs\downsample_sweep `
  --factor-sweep `
  --factor-start 1.0 `
  --factor-stop 8.0 `
  --factor-step 0.125 `
  --interp area
```

Run original weave image factor sweep, second range:

```powershell
python .\sweep_downsample.py `
  --input .\weave_153.png `
  --outdir .\outputs\downsample_sweep `
  --factor-sweep `
  --factor-start 8.125 `
  --factor-stop 16.0 `
  --factor-step 0.125 `
  --interp area
```

---

## Notes on Shell Quoting

These are equivalent in Bash:

```bash
--interp area
```

and

```bash
--interp 'area'
```

The shell removes the quotes before Python receives the argument.

Runtime validation comes from `argparse`:

```python
choices=["area", "nearest", "cubic"]
```

`Literal[...]` is for type checkers and documentation, not runtime argument validation.

---

## Immediate Next Steps

1. Commit `sweep_downsample.py` changes.
2. Create `docs/context_documents/` if needed.
3. Save this context document there.
4. Later generate and commit a contact sheet.

---

## Suggested Filename

```text
LN_ntec_2026-05-01_ctx01_downsampling-scout.md
```

Alternative if this lives inside the code-prep repo:

```text
LN_ntec-scout_2026-05-01_ctx01_stark-zebra-target-width-sweep.md
```

---

*End of context document.*
