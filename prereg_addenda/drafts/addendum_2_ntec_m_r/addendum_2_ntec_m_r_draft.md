# Addendum 2 — Regional and Measurement-Dependent NTEC

*This addendum is expected to inform a future appendix in the manuscript version. Numbering here follows addendum order rather than projected appendix numbering.*

---

## 2.1 Motivation

In this work, image-based text existence claims are evaluated relative to specific measurements. However, both **measurement conditions** and **spatial location within an image** can materially affect whether stroke-level signal is recoverable.

To make this dependence explicit, we introduce a regional form of the criterion and illustrate it using representative examples.

---

## 2.2 Formalization

We write:

- $M$ — a measurement (imaging condition, including exposure, modality, and processing pipeline)
- $R$ — a region (spatial subset of an image)

We define:

$$
\mathrm{NTEC}(M,R)
$$

as the Nyquist Text Existence Criterion evaluated on region $R$ of an image produced under measurement $M$.

This makes explicit that:

- NTEC is **not invariant under measurement** (depends on $M$)
- NTEC is **not spatially uniform across an image** (depends on $R$)

The underlying artifact is held fixed; only the measurement and region vary.

---

## 2.3 Filename Conventions

Figure filenames follow the structured schema documented in `FIGURE_FILENAME_SCHEMA.md`, encoding source, phenomenon family, measurement instance, region, and crop status.

---

## 2.4 Paired-Measurement Example: Ink Spill and Clean Regions

We consider two measurements of the same manuscript page:

- $M_{\text{dark}}$ — lower-light digitization
- $M_{\text{light}}$ — higher-light digitization

From these, we define regions:

- $R_{\text{ink,large}}$, $R_{\text{ink,small}}$ — regions within an ink spill
- $R_{\text{clean,large}}$, $R_{\text{clean,small}}$ — regions outside the spill

### 2.4.1 Overview

| Measurement | Full page |
|:--|:--|
| $M_{\text{dark}}$ | ![](M_dark_overview.png) |
| $M_{\text{light}}$ | ![](M_light_overview.png) |

---

### 2.4.2 Ink Spill Regions

| Region | $M_{\text{dark}}$ | $M_{\text{light}}$ |
|:--|:--|:--|
| $R_{\text{ink,large}}$ | ![](M_dark_R_ink_large.png) | ![](M_light_R_ink_large.png) |
| $R_{\text{ink,small}}$ | ![](M_dark_R_ink_small.png) | ![](M_light_R_ink_small.png) |

**Observation.** In the ink regions, stroke-level structure is heavily suppressed under $M_{\text{dark}}$, while partial recovery is visible under $M_{\text{light}}$.

This yields cases where:

- $\mathrm{NTEC}(M_{\text{dark}},R)$ plausibly fails
- $\mathrm{NTEC}(M_{\text{light}},R)$ plausibly holds

---

### 2.4.3 Clean Regions

| Region | $M_{\text{dark}}$ | $M_{\text{light}}$ |
|:--|:--|:--|
| $R_{\text{clean,large}}$ | ![](M_dark_R_clean_large.png) | ![](M_light_R_clean_large.png) |
| $R_{\text{clean,small}}$ | ![](M_dark_R_clean_small.png) | ![](M_light_R_clean_small.png) |

**Observation.** In clean regions, the dependence is subtler but still present.

Notably, fine-scale regions may exhibit **threshold-sensitive behavior**, where faint but structured strokes remain visible under one measurement while the same region under another approaches uniformity.

In particular, $R_{\text{clean,small}}$ may provide a case where:

- $\mathrm{NTEC}(M_{\text{dark}},R)$ weakly holds
- $\mathrm{NTEC}(M_{\text{light}},R)$ plausibly fails

---

## 2.5 Sequential-Measurement Example: Marginally Visible Manuscript Reuse

We next consider a sequence involving marginally visible manuscript reuse.[1] This example is useful because both apparent measurement quality and effective physical separation from the reused surface vary across the image sequence.

### 2.5.1 Exploratory Region Judgments for `tbrrgt`

The following judgments are rapid exploratory assessments based on visual inspection while developing operational definitions for NTEC. They are **not** final adjudications, thresholded measurements, or formal criterion outputs. Rather, they are provisional judgments intended to guide later formalization, region selection, and hypothesis refinement.

| M | R | Judgment | Notes |
|:--|:--|:--|:--|
| 00723 | 01 | pass | strong visibility near upper zone |
| 00723 | 02 | pass | clear retained structure |
| 00723 | 03 | pass | readable / undisqualified |
| 00723 | 04 | pass | still strong |
| 00723 | 05 | pass | moderate retained structure |
| 00723 | 06 | pass | weaker but plausible |
| 00721 | 01 | pass | still clear |
| 00721 | 02 | pass | moderate structure |
| 00721 | 03 | pass | plausible retained evidence |
| 00721 | 04 | pass | weakening begins |
| 00721 | 05 | borderline | reduced local clarity |
| 00721 | 06 | borderline | lower confidence |
| 00719 | 01 | pass | upper region preserved |
| 00719 | 02 | pass | visible structure |
| 00719 | 03 | pass | plausible |
| 00719 | 04 | borderline | weaker than above |
| 00719 | 05 | borderline | diminished evidence |
| 00719 | 06 | fail | little evident structure |
| 00717 | 01 | pass | upper zone still plausible |
| 00717 | 02 | pass | moderate structure |
| 00717 | 03 | borderline | fading |
| 00717 | 04 | borderline | weak |
| 00717 | 05 | fail | no clear local evidence |
| 00717 | 06 | fail | likely below threshold |
| 00706 | 01 | borderline | degraded |
| 00706 | 02 | pass | retained structure |
| 00706 | 03 | pass | still plausible |
| 00706 | 04 | borderline | transition zone |
| 00706 | 05 | fail | weak evidence |
| 00706 | 06 | fail | likely below threshold |
| 00701 | 03 | borderline | less undisqualified |
| 00701 | 04 | borderline | collapsing structure |
| 00701 | 05 | fail | likely below threshold |
| 00701 | 06 | fail | likely below threshold |
| 00697 | 01 | fail | insufficient visible structure |
| 00697 | 02 | pass | clearer than 0701 |
| 00697 | 03 | pass | retained evidence |
| 00697 | 04 | borderline | weak chance |
| 00697 | 05 | fail | no evident structure |
| 00697 | 06 | uncertain | region boundary itself unclear |

---

### 2.5.2 Preliminary Observations

Across successive measurements, subregions of the same physical reuse strip exhibit progressive loss of inscription-evidentiary structure. Smaller regions that remain plausible under one measurement become borderline or implausible under another, illustrating joint measurement- and region-dependence.

Across successive measurements, local recoverability is heterogeneous rather than monotonic. Adjacent subregions may differ sharply, and analyst-defined region boundaries can materially affect criterion judgments.

---

### 2.5.3 Measurement Index Interpretation

For this `tbrrgt` sequence, measurement $M_{00723}$ corresponds to the exposed reuse instance (i.e., the back pastedown image in which the phenomenon is directly visible).

Earlier measurements in the sequence are interpreted approximately as progressively deeper views through an overlying folio stack. Under this working assumption, measurement $M_{00723-n}$ corresponds approximately to the reuse instance viewed with $n$ codex folios above it.

This mapping is provisional rather than exact. Undetected blank or visually uninformative leaves may exist, so image-number offset should be treated as an approximate physical-depth proxy rather than a guaranteed folio count.

Due to its utility, I define: 

$$
d\left(M_i\right) = 723 - M_i
$$

where $d\left(M_i\right)$ is approximate folio depth from exposure.

So:
- $d\left(723\right) = 0$
- $d\left(706\right) = 17$
- $d\left(697\right) = 26$

with obvious limitations and inexactitudes, not the least of which is that the number of pages in the codex is finite, and there are several codices in the DGS.

---

## 2.6 Interpretation

These examples demonstrate:

1. **Measurement dependence.**  
   $\mathrm{NTEC}(M,R)$ can differ for the same region under different measurements.

2. **Spatial dependence.**  
   Within a single image, some regions may satisfy NTEC while others do not.

3. **Non-monotonicity.**  
   Improved visibility in one regime does not guarantee improvement across all regions.

Taken together, this shows that text existence, as evaluated from images, is not a global property of a digitization but a **localized, measurement-dependent property**.

---

## 2.7 Consequences for Transcription

A transcription derived from image data should distinguish between:

- **Evidentiary content** — supported by local recoverable signal under $\mathrm{NTEC}(M,R)$
- **Conjectural content** — supplied through inference, contextual completion, or unsupported interpretation

Under a single measurement:

- some regions may remain conjectural

Across multiple measurements:

- the union of evidentiary regions may expand
- reducing or eliminating conjectural components

This does not imply that information is added. Rather, different measurements may preserve different aspects of the underlying signal.

---

## 2.8 Note for Later: Physical Text Existence (PTEC)

Throughout this appendix, we evaluate text existence in a measurement-dependent manner using $\mathrm{NTEC}(M,R)$.

We briefly note a related artifact-level concept:

$$
\mathrm{PTEC}(R)
$$

referring to text existence as a property of the underlying artifact rather than any single measurement.

Intuitively, $\mathrm{PTEC}(R)$ concerns whether structured material differences corresponding to writing exist in the artifact in a manner that is, in principle, recoverable under physically realizable measurement conditions.

This perspective may be approached by considering multiple measurements of the same region and asking whether any such measurement preserves recoverable stroke-level signal. However, the available set of measurements may be incomplete.

Accordingly, it is possible for $\mathrm{NTEC}(M,R)$ to fail across all observed measurements while $\mathrm{PTEC}(R)$ nevertheless holds, due to limitations in imaging conditions.

This concept is introduced only to clarify the relationship between measurement-dependent detectability and artifact-level structure. It is not used for confirmatory claims in this work.

---

## Notes

[1] Background examples of reused information-bearing writing surfaces, including manuscript fragments reused in bindings (RMFB), together with a working classification schema used during exploratory dataset construction, are documented in the associated reference repository:

https://github.com/bballdave025/congenial-chainsaw-rmfb-html

---

_End of Addendum 2_
