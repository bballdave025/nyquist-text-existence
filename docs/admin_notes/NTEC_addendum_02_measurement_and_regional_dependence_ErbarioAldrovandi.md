# NTEC Addendum 2: Measurement and regional dependence in an Aldrovandi cover

## Source image

RMMFB filename:

`UnivBologna-SistemaMusealeDAteneo-AlmaMaterStudiorum_-_ErbarioAldrovandi-Vol-VI-60001_orc.jpg`

Reviewed while reconstructing provenance in the frozen RMMFB 3,331-image
dataset.

The image shows a decorated manuscript leaf reused as part of a binding.
The working description here is a high-quality parchment/vellum leaf, though
the exact material and codicological history have not been independently
verified for this note.

## Why this is useful for NTEC

This image is a particularly clean example of **regional dependence** in the
Nyquist Text Existence Criterion.

Different regions of the same physical leaf appear to occupy different
positions relative to the NTEC disqualification boundary.

For discussion, divide the writing into three conceptual regions:

1. **Primary manuscript text**
   - The original, relatively large and regular text.
   - For present purposes it may be imagined as something like biblical text;
     that identification is illustrative, not a claim about the manuscript.
   - At the current digitization quality, this region should clearly
     **fail to be disqualified as text under NTEC**.

2. **Commissioned commentary or secondary book text**
   - Smaller writing incorporated into the production of the manuscript.
   - For illustration, one might imagine a commentary associated with a writer
     such as Jerome; again, this is not an attribution.
   - Despite its smaller scale, enough writing-specific structure appears to
     remain that this region should also **fail to be disqualified as text**.

3. **Later reader annotations**
   - Much smaller, less regular writing added after production of the book.
   - The annotator might hypothetically have been Aldrovandi, Bede, or anybody
     else; the identity is irrelevant to the NTEC question.
   - At the present measurement quality, some of these marks may be
     **disqualified as text**, or may lie near the boundary where the
     mathematical observables associated with textual structure begin to
     weaken.

## Regional dependence

The important point is that there is no single NTEC result for the whole image.

Within one reused manuscript leaf:

- the primary text may clearly retain sufficient textual structure;
- the smaller commissioned commentary may still retain sufficient structure;
- the finest reader annotations may lose enough measurable structure to cross,
  or approach, the NTEC disqualification boundary.

Thus NTEC should be evaluated on a **region and scale**, not merely on an
entire image treated as a homogeneous object.

The same physical artifact can simultaneously contain regions that are:

- clearly fail-to-disqualify,
- borderline,
- and disqualified.

## Measurement dependence

This image also illustrates **measurement dependence**.

The present digital image is only one measurement of the physical artifact.
A higher-resolution or otherwise higher-quality digitization would provide a
different measurement.

My expectation is that improved measurement would preserve or recover more of
the spatial structure in the smallest annotations. With sufficient image
quality, all three regions could plausibly move into the
**fail-to-disqualify-as-text** category.

That would not represent a change in the artifact.

It would represent a change in the information available from the
measurement.

In NTEC terms, therefore, a statement such as

> this region is disqualified as text

must be understood as conditional on at least:

- the selected spatial region;
- the sampling/resolution;
- the imaging quality and preprocessing;
- and the particular mathematical observables used by NTEC.

## NTEC takeaway

This image provides a useful counterexample to treating "text existence" as a
single intrinsic binary property of an image.

A better formulation is closer to:

> Given this measurement of this region, is enough writing-specific
> information recoverable that NTEC cannot disqualify the region as text?

The Aldrovandi cover is useful precisely because different regions of the same
physical manuscript leaf appear capable of producing different answers, and
because a better measurement could change those answers without changing the
underlying object.

Retain this example regardless of the eventual numerical result.
It directly tests both **regional dependence** and **measurement dependence**
of NTEC.

## Preliminary images

The preliminary images, as usual, are committed directly to the `main` branch, 
though they should be shared with the branch representing addendum 2. They are 
on the `main` branch at

`nyquist-text-existence/img/prereg_addenda/addendum_2/drafts_ideas/Aldronavi_NTEC_Regions.png`

and

`nyquist-text-existence/img/prereg_addenda/addendum_2/drafts_ideas/Aldronavi_many.png`
