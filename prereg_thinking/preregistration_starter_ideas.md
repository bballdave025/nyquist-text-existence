# Preregistration — Nyquist Text Existence

**Project: Nyquist Text Existence**
**Authors: David Black (GitHub @bballdave025), Keith Prisbrey (GitHub @KeithPrisbrey)**
**Date of preregistration: YYYY-MM-DD**
**Status: Pre-experimental (confirmatory phase not yet begun)**


---

## 1. Purpose of this preregistration

This preregistration records the core theoretical claims and expected outcomes of the Nyquist Text Existence project prior to confirmatory experimentation.

The goal is to clearly distinguish:

- predictions derived from sampling theory, and

- exploratory analyses conducted to refine intuition or visualization.


This document is theory-forward and does not commit to specific model architectures, training regimes, or enhancement pipelines.

---

## 2. Scope of claims

This preregistration concerns text existence detection, defined as:

> The presence or absence of recoverable signal corresponding to writing in a digitized image, independent of recognition or transcription.

It does not concern:

- OCR accuracy,

- semantic correctness,

- paleographic interpretation,

- or historical attribution.

---

## 3. Primary theoretical claim

### Claim 1 (Nyquist Text Existence):

If stroke-scale spatial frequencies or intensity gradients corresponding to writing fall below the Nyquist limit imposed by sampling resolution, bit depth, or compression, then the signal corresponding to text ceases to exist in the digitized image.

Once this occurs, no downstream method—human, neural, or generative—can recover that signal as evidence of original inscription.

---

## 4. Derived predictions

From Claim 1, we pre-register the following predictions:

### Prediction 1: Abrupt failure under downsampling

There exists a resolution threshold below which text existence transitions from recoverable to undecidable, and this transition is abrupt, not gradual.

Failure to detect text below this threshold reflects information-theoretic loss rather than model inadequacy.


---

## Prediction 2: Model-agnostic failure

Below the sampling threshold, diverse model classes (e.g., CNNs, vision transformers, VLMs) will fail to detect text existence in similar ways, despite differences in architecture or training data.

Any retained confidence reflects priors or global structure, not stroke-level evidence.


---

## Prediction 3: Human–machine parity after signal loss

Once sampling destroys stroke-scale information, human observers will not reliably outperform machine systems in determining text existence, except via perceptual interpolation or contextual inference.

Such inference does not constitute access to evidentiary signal.

---

## 5. Image-specific anchor (Image B)

Image B is designated as a thematic anchor, not a cherry-picked success case.

### Prediction for Image B:

- At native resolution, stroke-scale structure is recoverable.

- After routine downsampling or compression, the same region becomes undecidable with respect to text existence.

- This change is attributable solely to sampling decisions.

---

## 6. Cross-script extension (Japanese diacritic challenge)

We pre-register the expectation that writing systems with small, information-critical diacritics (e.g., Japanese dakuten / handakuten) will violate sampling limits at different thresholds than Latin scripts.

### Prediction:

- Semantic distinctions carried by diacritics will be lost before base glyph structure collapses.

- Text existence may persist after semantic distinction fails, or may collapse simultaneously depending on script geometry.

---

## 7. Role of super-resolution and enhancement

Super-resolution and enhancement methods may generate visually plausible reconstructions below the Nyquist limit.

### Pre-registered position:

- Such outputs introduce information.
- They are not treated as evidence of original inscription.
- Increased human or model confidence based on such reconstructions does not imply recoverability of signal.

---

## 8. What is considered confirmatory vs. exploratory

### Confirmatory analyses:

Tests of the predictions listed above against controlled resampling conditions.


### Exploratory analyses:

- Visualization choices,

- model selection,

- enhancement techniques,

- or qualitative inspections used to refine intuition.


Exploratory work is allowed and expected, but will be labeled as such.


---

## 9. Deviations and addenda

Any deviation from this preregistration will be documented as an addendum, not a replacement.

Addenda may clarify scope, refine predictions, or add new hypotheses, but will not retroactively alter pre-registered claims.


---

## 10. Intended use

This preregistration is intended to:

- support transparent collaboration,
- protect negative results,
- and serve as a stable reference for workshops, arXiv preprints, and related discussion.

It does not assert priority, ownership, or completeness.

---

*End of preregistration.*
