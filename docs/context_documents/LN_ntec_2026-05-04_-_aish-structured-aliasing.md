CONTEXT DOCUMENT for continuation of the "[NTEC AISH / structured aliasing and measurement-dependent artifact formation — exploratory Addendum 2 work on how downsampling can remove true inscription signal while producing stroke-like artifacts from periodic decorative structures]" project

DOCUMENT PREPARED FOR CONTINUATION: 
1777915733_2026-05-04T13:28:53-0400

date +'%s_%Y-%m-%dT%H:%M:%S%z'  # use current Boston, MA time zone

CONTINUED FROM CHAT ENTITLED:
C++ Jupyter Config Class
ALSO INVOLVING
`NTEC, RMFB, AISH, Addendum 2, measurement dependence, regional dependence, Bordeaux weave, watermark downsampling, zebra scout, no-code-jupyter-nb`
FROM USER
  (GitHub) @bballdave025

---

## Purpose of this context document

This document preserves the state of an exploratory NTEC thread concerning:

- downsampling,
- Moiré-like behavior,
- watermark/weave visibility loss,
- periodic decorative borders,
- and the emergence of stroke-like artifacts under sampling loss.

The working phenomenon name is:

**Aliasing-Induced Stroke Hallucination (AISH).**

This is intended as context for continuing work in a new chat with less lag and better computer access.

---

## Relationship to NTEC Addendum 2

This work belongs after the already-developing Addendum 2 thread on:

- measurement dependence,
- regional dependence,
- and the non-transitivity of text existence across regions and sampled representations.

The central connection is:

> Measurement can destroy inscription-specific signal, but measurement can also create visually stroke-like artifacts that are not supported by inscription-specific signal.

This strengthens rather than weakens NTEC, because it identifies a false-positive counterpart to the familiar false-negative problem of signal annihilation.

---

## Anchor image vs. canonical crop

The uploaded preregistration already distinguishes the role of an image anchor and a canonical crop.

Working distinction:

### Anchor image

An **anchor image** is an image used to instantiate, communicate, or explore a theoretical phenomenon under NTEC.

An anchor image may support exploratory reasoning, figure-building, or addendum development. It does not necessarily imply unique evaluation status, optimality, or fixed confirmatory coordinates.

### Canonical crop

A **canonical crop** is a uniquely defined, fixed region selected by a specified deterministic procedure and used as the evidentiary object for confirmatory evaluation.

Canonical crop means:

- fixed coordinates,
- no substitution after locking,
- no outcome-dependent replacement,
- privileged role in confirmatory analysis.

### Current AISH status

The AISH examples discussed here are currently **anchor-level exploratory examples**, not canonical crops.

They are candidates for:

- exploratory addendum figures,
- measurement-dependence demonstrations,
- and region-selection protocols.

They should not be treated as locked confirmatory crops until a later explicit locking step.

---

## Working definition of AISH

**Aliasing-Induced Stroke Hallucination (AISH)** refers to the emergence of stroke-like visual structures under downsampling or resampling that are not supported by inscription-specific signal in the source image.

Important refinement:

AISH does **not** imply that new information has been added.

Instead:

> AISH arises under information loss when high-frequency structure is aliased, folded, reorganized, or otherwise represented at lower spatial scales in ways that become visually stroke-like.

AISH is therefore a measurement-induced false-positive risk at or beyond sampling boundaries.

---

## Reviewer-safe definition

Use something like this in formal prose:

> We define Aliasing-Induced Stroke Hallucination (AISH) as the emergence, under downsampling or resampling, of stroke-like structures that are not supported by inscription-specific signal in the source image. AISH does not represent the addition of new evidentiary information; rather, it reflects the reorganization of existing high-frequency structure under information loss, such that the sampled image visually suggests stroke-like form without preserving recoverable inscription-specific signal.

---

## Entropy footnote idea

The user wanted a tiny entropy measure to avoid turning this into a separate project.

Minimal code:

```python
import numpy as np
from PIL import Image

def entropy(path):
    img = np.array(Image.open(path).convert('L'))
    p = np.bincount(img.ravel(), minlength=256) / img.size
    p = p[p > 0]
    return -(p * np.log2(p)).sum()

print(entropy("your_image.png"))
```

Possible footnote language:

> A simple grayscale histogram entropy check may be used illustratively to confirm that global image information decreases under downsampling, even when visually structured artifacts appear. This entropy measure is not treated as a descriptor of inscription-specific evidence, since histogram entropy does not capture spatial stroke structure.

Important boundary:

Do not build a full entropy section unless later evidence demands it.

---

## Prior scout results

### Bordeaux weave / watermark crop

A crop was made from a watermark-bearing page, selecting a right-side region that excluded handwriting while preserving visible weave and watermark structure.

Approximate crop from the screenshot-sized image:

```python
CropSpec(x=795, y=77, w=367, h=1382)
```

This was saved as:

```text
weave_crop.png
```

Run:

```bash
python sweep_downsample.py \
  --input ./weave_crop.png \
  --outdir ./outputs/weave_crop_sweep/run_01_start_lesser_res_orig_contrast \
  --target-w-sweep \
  --target-w-start 301 \
  --target-w-stop 1 \
  --target-w-step -3 \
  --interp area
```

Observation:

- weave starts breaking down around target width 100–65,
- watermark is definitely gone by about target width 30,
- no strong stroke-like AISH was observed in this crop.

### Synthetic zebra scout

A synthetic image was generated:

```text
stark_zebra_100.png
```

Specification:

- 100 px wide,
- 1000 px tall,
- vertical stripes,
- 5 px stripe width,
- alternating values 255 and 0.

A target-width sweep from 99 down to 1 was run.

Observation:

- aliasing appeared where expected,
- no convincing stroke-like structure appeared,
- high symmetry likely suppresses the kind of irregular pseudo-stroke morphology of interest.

---

## Current sweep CLI

The current script is named in the repo as:

```text
sweep_downsample.py
```

It had previously been referred to in-chat as:

```text
sweep_downsample_2point0.py
```

Capabilities:

- factor sweep,
- target-width sweep,
- target-height sweep,
- optional crop,
- downsampled output,
- downsampled-then-upsampled output,
- CSV log,
- optional contact sheet.

Relevant command for the focused watermark/weave run:

```bash
python sweep_downsample.py \
  --input ./weave_crop.png \
  --outdir ./outputs/weave_crop_sweep/run_02_lesser_res_orig_contrast_ginr_tooth \
  --target-w-sweep \
  --target-w-start 100 \
  --target-w-stop 3 \
  --target-w-step -1 \
  --make-contact-sheet \
  --contact-sheet-cols 10 \
  --interp area
```

PowerShell equivalent:

```powershell
python .\sweep_downsample.py `
  --input .\weave_crop.png `
  --outdir .\outputs\weave_crop_sweep\run_02_lesser_res_orig_contrast_ginr_tooth `
  --target-w-sweep `
  --target-w-start 100 `
  --target-w-stop 3 `
  --target-w-step -1 `
  --make-contact-sheet `
  --contact-sheet-cols 10 `
  --interp area
```

---

## Contact sheets

A contact sheet means:

> one single image containing a tiled grid of many sweep outputs.

Purpose:

- quick visual scan,
- one Git-friendly representative artifact,
- easier comparison of transition ranges,
- useful for lab notebooks and exploratory figures.

Contact sheets are scout/visualization tools, not quantitative evidence by themselves.

---

## AISH source-image set

A later group of images came from FamilySearch viewer screenshots and related views of a decorative frame/title-page style image.

The relevant image group shown in screenshots was:

```text
008013965
```

The source image resolution shown in metadata was:

```text
4161 x 3317
```

The images show:

- a decorative frame,
- dense periodic grating-like bottom/top border regions,
- chain-like decorative edges,
- flower/corner boxes,
- leafy/garland ornamentation,
- blank interior/adjacent regions,
- dense handwritten pages elsewhere in the same image group.

---

## Important correction to earlier interpretation

Earlier language about a generator edge “injecting artifacts into nearby regions” was too strong.

Corrected framing:

> The grating, chain, and flower/corner regions are likely both the generators and the locations where pseudo-strokes appear. Adjacent blank regions are control or receptor candidates, but transfer of structured artifacts into blank space is an empirical question, not an assumption.

This distinction should be preserved.

---

## Preferred phenomenon name

Do not use “Moiré++” in the paper.

Preferred term:

```text
Aliasing-Induced Stroke Hallucination (AISH)
```

Short phrase:

```text
AISH
```

Paper-safe long phrase:

```text
aliasing-induced stroke-like artifacts
```

or

```text
aliasing-induced stroke hallucination
```

---

## Region logic

The user proposed a region design centered on decorative frame components.

Important definitions:

### Generator candidate

A **generator candidate** is a high-frequency or structured decorative region that may produce AISH when downsampled.

Examples:

- grating strips,
- chain borders,
- flower/corner boxes,
- leafy garland regions.

### Pseudo-stroke location

A **pseudo-stroke location** is where visually stroke-like artifacts appear after downsampling.

Current hypothesis:

> pseudo-strokes will most likely exist within the grating or decorative structures themselves, not necessarily in adjacent blank space.

### Control / adjacent blank region

A blank region near a generator candidate may be used as a control to determine whether visually stroke-like structure appears outside the source structure.

---

## Theta definition

The user’s intended θ was not a generic distance-to-generator parameter.

The intended θ is:

> Let the lower-left flower box be treated as a square of side length `s`. Define θ as the diagonal of that square, θ = s√2.

Important reproducibility rule:

> θ is defined once from the lower-left flower box and reused globally. It should not be recalculated independently at each corner.

The measurement from the bottom-left flower box should be used everywhere in determining regions with θ.

---

## Proposed region families

### Region 1

Generator:

- bottom frame at the left-hand side,
- lower-left flower box,
- plus a length of grating,
- corresponding conceptually to the square inscribing T, then H, M, and P slid left to abut the flower square.

Measurement/control region:

- white blank space underneath,
- analogous to L,
- slid underneath the generator,
- possibly expanded on all edges except the top edge.

### Region 2

Same as Region 1, but with the flower box removed.

Purpose:

- isolate grating/chain effect without corner ornament.

### Region 3

Generator:

- only the box with the flower.

Measurement/control region:

- white space to the bottom and left of the flower box,
- excluding anything above the top of the flower box or to its right.

### Region 4

Generator:

- H-like grating strip,
- slid so it is next to but does not include the flower box.

Measurement/control region:

- L-like blank region,
- slid in the same way.

### Region 5

Same as Region 4, but generator includes M slid appropriately left.

### Region 6

Same as Region 5, but with P appropriately slid.

Equivalent to Region 2.

---

## Additional region families

Repeat similar regions:

- including only the inside of the frame,
- excluding outside whitespace,
- in the middle of frame-border lengths rather than abutting the flower boxes,
- across the four major corners or edge directions,
- especially the top-right region, where spacing appears smaller.

Also include leafy garland regions.

The term “garland” is acceptable for the leafy decorative structure, though the user may refine the term later.

---

## Suggested experimental hypothesis

Use this as the safe hypothesis:

> AISH, if present, will arise primarily within downsampled periodic decorative structures themselves, especially grating and chain borders. Adjacent blank regions are included as controls to test whether apparent stroke-like structure appears outside the decorative source.

---

## Measurement dependence claim

This case is useful for Addendum 2 because it shows:

> The answer to “does this sampled image contain stroke-like evidence?” depends not only on the physical source and region, but on the measurement representation.

Specifically:

- high-resolution anchor view,
- downsampled derivatives,
- thumbnail grids,
- browser-rendered zoom states,
- and mobile screenshots

may each present different apparent structure.

This is not merely visual inconvenience; it is part of the NTEC measurement-dependence problem.

---

## Regional dependence claim

The same image can contain:

- true writing regions,
- decorative grating regions,
- chain/flower/garland ornament regions,
- blank regions,
- watermark-like or substrate-like regions.

Under downsampling, each may cross evidentiary boundaries at different scales.

Thus:

> text existence and stroke-like evidence are regional, not image-global.

---

## Important controls

Include controls such as:

- blank region far from decorative border,
- dense handwriting page from same image group,
- decorative border crop,
- grating-only crop,
- flower-only crop,
- garland-only crop,
- adjacent blank crop.

Dense handwritten pages are useful because the same viewer/downsampling pipeline applies, but the signal structure is different. If artifacts appear mainly in periodic decorative regions, that supports a border-specific AISH mechanism rather than a whole-pipeline artifact claim.

---

## Images likely useful for the context/new chat

The user sent multiple batches of numbered screenshots.

Promising figure candidates:

1. Full or near-native decorative title/frame image as anchor.
2. Intermediate downsampling state showing onset of aliasing.
3. Close-up of the border/grating structure.
4. Downsampled state where pseudo-stroke-like artifacts appear.
5. Image group / thumbnail grid showing broader measurement context.
6. Dense handwriting pages as control contrast.
7. Metadata screenshot showing image group and native dimensions.

The user also sent labeled images and intends to send/describe labeled crops in the new chat.

---

## Terminology to avoid or soften

Avoid:

```text
Moiré++
```

Avoid making strong claims that artifacts transfer into blank regions until an experiment shows it.

The first paper/addendum should focus on NTEC, sampling, downsampling, and measurement dependence.

---

## Minimal code organization goal after Addendum 2

After Addendum 2 stabilizes, reorganize the experimental code.

Current issue:

> image loading, resampling, early Fourier utilities, Sobel energy, and canonical/crop-finalization logic are mixed in one file.

The user wants to preserve class-based design with static methods but make the code tidy.

Possible classes/modules to consider, subject to later refinement:

### Image operations

Could include:

- loading,
- grayscale conversion,
- cropping,
- CropSpec,
- outlining selections,
- downsampling,
- upsampling,
- nearest-neighbor visualization,
- contact sheets.

### Descriptor measures

Could include:

- entropy,
- Fourier descriptors,
- gradient measures,
- Sobel edge energy,
- connected components,
- structure tensor,
- edge smoothness,
- possible fractal / box-counting measures,
- other NTEC descriptor families noted elsewhere.

### Pipelines

Could include:

- canonical crop selection,
- crop finalization,
- downsampling sweeps,
- descriptor passes,
- visualization/export routines,
- figure generation.

This organization is only one possible starting point. The next chat should accept the user’s existing class and method names and help design a tidy class-based organization.

---

## Bash commands to preserve

Run focused weave crop sweep with contact sheet:

```bash
python sweep_downsample.py \
  --input ./weave_crop.png \
  --outdir ./outputs/weave_crop_sweep/run_02_lesser_res_orig_contrast_ginr_tooth \
  --target-w-sweep \
  --target-w-start 100 \
  --target-w-stop 3 \
  --target-w-step -1 \
  --make-contact-sheet \
  --contact-sheet-cols 10 \
  --interp area
```

Make script executable:

```bash
chmod +x sweep_downsample.py
```

Run entropy check:

```bash
python entropy_check.py
```

---

## PowerShell commands to preserve

Run focused weave crop sweep with contact sheet:

```powershell
python .\sweep_downsample.py `
  --input .\weave_crop.png `
  --outdir .\outputs\weave_crop_sweep\run_02_lesser_res_orig_contrast_ginr_tooth `
  --target-w-sweep `
  --target-w-start 100 `
  --target-w-stop 3 `
  --target-w-step -1 `
  --make-contact-sheet `
  --contact-sheet-cols 10 `
  --interp area
```

Run entropy check:

```powershell
python .\entropy_check.py
```

---

## Immediate next steps for the new chat

1. Receive this context document as authoritative state.
2. Review the user’s labeled screenshots and clarify region definitions.
3. Define AISH formally.
4. Define anchor image vs canonical crop language.
5. Draft Addendum 2 subsection:
   - measurement-dependent artifacts,
   - AISH,
   - decorative-border aliasing,
   - regional dependence.
6. Decide which images become:
   - anchor figures,
   - exploratory examples,
   - controls.
7. Only after that, reorganize code classes/modules.

---

## Suggested filename

No optional tag:

```text
LN_ntec_2026-05-04_aish-structured-aliasing.md
```

---

End of context document.
