# Addendum 2 — Regional and Measurement-Dependent NTEC

Note that this will likely become an appendix to the eventual, published paper, which is why the section identifications have 'A' prepended.

## A2.1 Motivation

Text existence in this work is evaluated in a measurement-dependent manner.  
However, both **measurement conditions** and **spatial location within an image** can materially affect whether stroke-level signal is recoverable.

To make this dependence explicit, we introduce a regional form of the criterion and illustrate it using paired measurements of the same artifact under differing imaging conditions.

---

## A2.2 Formalization

We write:

- $M$ — a measurement (imaging condition, including exposure, modality, and processing pipeline)
- $R$ — a region (spatial subset of an image)

We define:

$$
\mathrm{NTEC}(M, R)
$$

as the Nyquist Text Existence Criterion evaluated on region $R$ of an image produced under measurement $M$.

This makes explicit that:

- NTEC is **not invariant under measurement** ($M$)
- NTEC is **not uniform across an image** (depends on $R$)

The underlying artifact is held fixed; only the measurement and region vary.

---

## A2.3 Filename conventions

Figure filenames follow the structured schema documented in `FIGURE_FILENAME_SCHEMA.md`, encoding source, phenomenon family, measurement instance, region, and crop status.

---

## A2.4 Empirical Illustration

We consider two measurements of the same manuscript page:

- $M_{\text{dark}}$ — lower-light digitization  
- $M_{\text{light}}$ — higher-light digitization  

From these, we define regions:

- $R_{\text{ink, large}}$, $R_{\text{ink, small}}$ — regions within an ink spill  
- $R_{\text{clean, large}}$, $R_{\text{clean, small}}$ — regions outside the spill  

### Overview

| Measurement | Full page |
|------------|----------|
| $M_{\text{dark}}$ | ![](M_dark_overview.png) |
| $M_{\text{light}}$ | ![](M_light_overview.png) |

---

### Ink spill regions

| Region | $M_{\text{dark}}$ | $M_{\text{light}}$ |
|-------|------------------|-------------------|
| $R_{\text{ink, large}}$ | ![](M_dark_R_ink_large.png) | ![](M_light_R_ink_large.png) |
| $R_{\text{ink, small}}$ | ![](M_dark_R_ink_small.png) | ![](M_light_R_ink_small.png) |

**Observation.**  
In the ink regions, stroke-level structure is heavily suppressed under $M_{\text{dark}}$, while partial recovery is visible under $M_{\text{light}}$.

This yields cases where:

- $\mathrm{NTEC}(M_{\text{dark}}, R)$ plausibly fails  
- $\mathrm{NTEC}(M_{\text{light}}, R)$ plausibly holds  

---

### Clean regions

| Region | $M_{\text{dark}}$ | $M_{\text{light}}$ |
|-------|------------------|-------------------|
| $R_{\text{clean, large}}$ | ![](M_dark_R_clean_large.png) | ![](M_light_R_clean_large.png) |
| $R_{\text{clean, small}}$ | ![](M_dark_R_clean_small.png) | ![](M_light_R_clean_small.png) |

**Observation.**  
In clean regions, the dependence is more subtle but still present.

Notably, fine-scale regions exhibit **threshold-sensitive behavior**, where:

- faint but structured strokes are visible under one measurement
- while the same region under another measurement approaches uniformity

In particular, $R_{\text{clean, small}}$ provides a case where:

- $\mathrm{NTEC}(M_{\text{dark}}, R)$ may weakly hold  
- $\mathrm{NTEC}(M_{\text{light}}, R)$ may fail  

---

## A2.5 Interpretation

These examples demonstrate:

1. **Measurement dependence.**  
   $\mathrm{NTEC}(M, R)$ can differ for the same region under different measurements.

2. **Spatial dependence.**  
   Within a single image, some regions may satisfy NTEC while others do not.

3. **Non-monotonicity.**  
   Improved visibility in one regime (e.g., lighter exposure) does not guarantee improvement across all regions.

Taken together, this shows that text existence, as evaluated from images, is not a global property of a digitization but a **localized, measurement-dependent property**.

---

## A2.6 Consequences for Transcription

A transcription derived from image data must distinguish between:

- **Evidentiary content** — supported by $\mathrm{NTEC}(M, R)$  
- **Conjectural content** — not supported under that measurement  

Under a single measurement:

- some regions may require conjectural interpretation

Across multiple measurements:

- the union of evidentiary regions may expand  
- reducing or eliminating conjectural components

This does not imply that information is added; rather, different measurements preserve different aspects of the underlying signal.

---

## A2.7 Note (for later): Physical Text Existence (PTEC)

Throughout this appendix, we evaluate text existence in a measurement-dependent manner using $\mathrm{NTEC}(M, R)$.

We briefly note a related, more general concept: $\mathrm{PTEC}(R)$, referring to text existence as a property of the underlying artifact rather than any single measurement.

Intuitively, $\mathrm{PTEC}(R)$ concerns whether structured material differences corresponding to writing exist in the artifact in a manner that is, in principle, recoverable under physically realizable measurement conditions.

This perspective may be approached by considering multiple measurements of the same region and asking whether any such measurement preserves recoverable stroke-level signal. However, the available set of measurements may be incomplete. In particular, it is possible for $\mathrm{NTEC}(M, R)$ to fail across all observed measurements while $\mathrm{PTEC}(R)$ nevertheless holds, due to limitations in imaging conditions.

This concept is introduced only to clarify the relationship between measurement-dependent detectability and artifact-level structure. It is not used for confirmatory claims in this work.

---

_End of Addendum 2_
