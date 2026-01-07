# Thematic Image Information — Image B
## Text Existence at the Nyquist Boundary

## Purpose of this document

This document explains why a small number of images recur across multiple
Nyquist- and RMFB-related documents, talks, and experiments.

These images are not presented as ground truth annotations, transcriptions,
or paleographic claims. Instead, they function as **thematic anchors** for
discussing the information-theoretic limits of text existence detection in
digitized manuscript imagery.

Image B is one such anchor.

---

## Image B: Low–Pixel-Footprint Text in a Binding Context

Image B depicts a fragment of writing embedded in a book-binding context,
visible only along the edge of the material rather than on a primary page
surface. The writing is peripheral, non-focal, and easily deprioritized by
routine digitization and preprocessing pipelines.

At full resolution:

- The trace exhibits **parallel vertical strokes (minims)**.
- Stroke spacing, continuity, and alignment are consistent with
  human-produced writing.
- Ink–substrate alternation is preserved at stroke scale.
- A trained paleographer would almost certainly classify the trace as text,
  even in isolation.

Importantly, this is **not faint text**. The ink contrast is adequate; the
limiting factor is spatial scale. The writing occupies only a few pixels
across its critical dimension (on the order of single-digit pixels) while
extending meaningfully along the orthogonal direction in a much larger image
(≈ thousands of pixels).

---

## Why Image B Matters

Image B sits precisely at the boundary between:

- **Recoverable signal** and **irreversible information loss**, and
- **Expert certainty** and **computational undecidability**.

At native resolution, the ink–background alternation that defines stroke
structure is preserved. After modest downsampling or compression—of the sort
commonly used in computer vision pipelines—the same region becomes
indistinguishable from background texture, abrasion, or noise.

This collapse is **structural, not semantic**. It is not a failure of model
architecture, training data, or enhancement technique. It is a direct
consequence of violating the Nyquist criterion for stroke-scale spatial
frequencies.

Once those frequencies are lost, no downstream method—human or
machine—can recover the fact that text existed there at all.

---

## Text Existence vs. Text Recognition

Image B motivated a key distinction formalized in this work:

- **Text existence detection** is a signal-presence problem.
- **Text recognition** is a symbol-decoding problem.

These problems operate at different sampling thresholds. In Image B, the
threshold for detecting *that writing is present* is exceeded before any
question of *what the writing says* can meaningfully arise.

This distinction explains why whole-image downsampling systematically erases
precisely the class of signals most relevant for manuscript reuse discovery.

---

## Pixel-Faithful Zooms and Display Interpolation

Zoomed views of Image B are used to illustrate proximity to the sampling
boundary.

To distinguish recoverable signal from visualization artifacts:

- **Pixel-faithful zooms** are produced using nearest-neighbor scaling with
  interpolation explicitly disabled. These renderings preserve the original
  sampled pixels exactly, making the presence or absence of stroke-scale
  structure explicit.
- **Interpolated zooms** (e.g., bicubic or bilinear) may also be shown for
  visual intuition. These introduce continuity assumptions and are clearly
  labeled as illustrative only.

Square-pixel renderings demonstrate that observed stroke structure is present
in the original image data and not introduced by interpolation or smoothing.

---

## Super-Resolution as Contrast, Not Evidence

Super-resolution models may generate visually plausible text-like structures
from low-resolution inputs. Such reconstructions necessarily introduce
information beyond what was sampled.

In this project, super-resolution outputs—where shown—are used solely to
contrast human interpretive tendencies and model generativity with
information-theoretic constraints. They are **not** treated as evidence of
original inscription or recoverable signal.

As a guiding principle:

> Plausibility does not imply provenance.

---

## Scope Limitation

No claim is made here regarding:

- legibility,
- transcription,
- script identification,
- dating,
- or historical interpretation.

Those questions require access to higher-fidelity imaging or the physical
artifact itself and fall outside the scope of this work.

---

## Summary

Image B is not merely an example of manuscript reuse. It is a concrete
demonstration that:

- some historically meaningful signals exist only above specific sampling
  thresholds,
- digitization and preprocessing decisions bound all future computational
  analysis,
- and abstention is a principled response when information has been
  irreversibly destroyed.

For these reasons, Image B recurs intentionally across RMFB vision documents,
Nyquist technical notes, talks, and experimental designs. It reliably bridges
expert intuition and formal sampling theory—and makes visible a boundary that
is otherwise easy to dismiss.
