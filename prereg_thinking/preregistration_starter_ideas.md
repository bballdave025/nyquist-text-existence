# Preregistration — Nyquist Text Existence

**Project:** Nyquist Text Existence

**Authors:**  
David Black (GitHub @bballdave025)  
Keith Prisbrey (GitHub @keithprisbrey)

**Date of preregistration:** TBD

**Status:** Pre-experimental (confirmatory phase not yet begun)

---

_Confirmatory analysis begins at the first execution of a pre-registered test on the locked image set and locked resampling procedure._

---

## 1. Purpose of this preregistration

This preregistration records the core theoretical claims, predictions, and evaluation boundaries of the Nyquist Text Existence project prior to confirmatory experimentation.

The primary goal is to clearly distinguish:

- predictions derived from sampling theory and information-theoretic limits, and
- exploratory analyses conducted to refine intuition, visualization, or experimental design.

This document is theory-forward. It intentionally avoids commitment to specific model architectures, training regimes, enhancement pipelines, or optimization procedures.

---

## 2. Scope of claims

This preregistration concerns **text existence detection**, defined as:

> The presence or absence of recoverable signal corresponding to writing in a digitized image, independent of recognition, transcription, or interpretation.

The scope explicitly excludes:

- OCR accuracy,
- semantic correctness,
- paleographic interpretation,
- historical attribution,
- or claims about authorial intent.

The focus is strictly on whether evidentiary signal corresponding to writing exists in the sampled image data.

---

## 3. Primary theoretical claim

### Claim 1 (Nyquist Text Existence)

If stroke-scale spatial frequencies or intensity gradients corresponding to writing fall below the Nyquist limit imposed by sampling resolution, bit depth, or compression, then the signal corresponding to text ceases to exist in the digitized image.

Once this occurs, no downstream method—human, neural, or generative—can recover that signal as evidence of original inscription.

---

## 4. Derived predictions

From Claim 1, we pre-register the following predictions.

### Prediction 1: Abrupt failure under downsampling

There exists a sampling threshold below which text existence transitions from recoverable to undecidable, and this transition is abrupt rather than gradual.

Failure to detect text below this threshold reflects information-theoretic loss, not model inadequacy or insufficient training.

---

### Prediction 2: Model-agnostic failure

Below the sampling threshold, diverse model classes (e.g., CNNs, vision transformers, VLMs) will fail to detect text existence in qualitatively similar ways, despite architectural or training differences.

Any retained confidence reflects priors, layout cues, or global structure, not access to stroke-level evidentiary signal.

---

### Prediction 3: Human–machine parity after signal loss

Once sampling destroys stroke-scale information, human observers will not reliably outperform machine systems in determining text existence, except via perceptual interpolation or contextual inference.

Such inference does not constitute access to evidentiary signal and is not treated as evidence of text existence under this framework.

---

## 5. Image-specific anchor (Image B)

Image B is designated as a **thematic anchor**, not a cherry-picked success case.

### Pre-registered expectations for Image B:

- At native resolution, stroke-scale structure corresponding to writing is recoverable.
- After routine downsampling or compression, the same region becomes undecidable with respect to text existence.
- The transition is attributable solely to sampling decisions, not enhancement, denoising, or model choice.

Image B serves to concretize the Nyquist boundary under realistic digitization practices.

---

## 6. Cross-script extension (Japanese diacritic challenge)

We pre-register the expectation that writing systems with small, information-critical diacritics (e.g., Japanese dakuten / handakuten) violate sampling limits at different thresholds than Latin scripts.

### Prediction:

In cross-script contexts, we distinguish between two related but non-identical limits: (i) loss of semantic distinction within a writing system, and (ii) loss of text existence proper, defined as the presence of recoverable writing signal at all.

- Semantic distinctions carried by diacritics are expected to be lost before full base glyph structure collapses.
- Depending on script geometry and stroke distribution, text existence may persist after semantic distinction fails, or may collapse simultaneously with base glyph structure.

This extension is intended to test generality across writing systems without asserting universality.

---

## 7. Fingerprints and non-text surface traces (exploratory analysis)

This project includes **exploratory but serious analysis** of fingerprints and related non-text surface traces frequently observed in manuscript imagery.

These analyses are intended to:

- clarify similarities and differences between text and non-text signals under sampling loss,
- test whether Nyquist-based collapse applies consistently to other fine-grained, human-produced surface structures,
- and refine conceptual boundaries between “writing,” “trace,” and “texture.”

Fingerprint analyses are **not** treated as primary anchors and do not generate confirmatory claims about text existence. They are used to sharpen intuition, contrast signal geometries, and contextualize the text-specific results.

All such analyses will be explicitly labeled as exploratory.

---

## 8. Role of super-resolution and enhancement

Super-resolution and enhancement methods may generate visually plausible reconstructions below the Nyquist limit.

### Pre-registered position:

- Such outputs introduce information.
- They are not treated as evidence of original inscription.
- Increased human or model confidence based on such reconstructions does not imply recoverability of signal.

Super-resolution results may be shown illustratively but are not used to support confirmatory claims.

---

## 9. Confirmatory vs. exploratory analyses

### Confirmatory analyses

- Tests of the predictions listed above
- Conducted under locked image regions and locked resampling procedures
- Evaluated against pre-registered criteria

### Exploratory analyses

- Visualization choices
- Model selection
- Enhancement techniques
- Qualitative inspection (including fingerprints and surface traces)

Exploratory work is allowed and expected, but will be explicitly labeled as such and separated from confirmatory results.

---

## 10. Deviations and addenda

Any deviation from this preregistration will be documented as an addendum, not a replacement.

Addenda may clarify scope, refine predictions, or introduce new hypotheses, but will not retroactively alter pre-registered claims or evaluation criteria.

---

## 11. Intended use

This preregistration is intended to:

- support transparent collaboration,
- protect negative results,
- and serve as a stable reference for workshops, arXiv preprints, and related discussion.

It does not assert priority, ownership, or completeness.

---

*End of preregistration.*
