# Hypothesis Pre-Registration (Why and What)

Hypothesis pre-registration is the practice of recording core claims before running confirmatory analyses, 
in order to clearly distinguish between:

- confirmatory work (testing a stated claim), and
- exploratory work (discovering patterns, refining questions).

For this project, pre-registration serves three specific purposes.


---

## Why We Are Pre-Registering

### 1. Clarifying epistemic boundaries

Pre-registration makes explicit which failures are predicted by sampling theory (e.g., Nyquist limits) 
rather than discovered after experimentation.

This is especially important for claims about non-recoverability. Without pre-registration, negative
results can be misinterpreted as implementation failures rather than theoretical confirmations.


---

### 2. Protecting negative results

If the hypothesis predicts that text existence becomes undecidable below a specific sampling threshold,
then failure to detect text is not an embarrassment or limitation — it is an expected and informative
outcome.

Pre-registration allows negative results to function as evidence, rather than as something that must be
explained away.


---

### 3. Preventing hindsight bias

Pre-registration prevents the impression that thresholds, crops, examples, or model choices were selected
post hoc to fit observed outcomes.

This is particularly important when working with visually compelling examples, where it is easy to
unconsciously optimize presentation after seeing results.


---

## What We Intend to Pre-Register

We pre-register claims, not implementations.

Specifically, we pre-register:

- information-theoretic claims about recoverability and non-recoverability under sampling constraints,
- qualitative and quantitative boundaries at which text existence is predicted to fail,
- and the distinction between evidence of signal and plausibility of reconstruction.


We do not pre-register specific architectures, filters, enhancement pipelines, or visualization choices.

Exploratory image processing is allowed and expected, but must be clearly labeled as exploratory rather 
than confirmatory.


---

## What Pre-Registration Does Not Restrict

Pre-registration does not:

- forbid exploratory analysis,
- prevent iteration on experimental design,
- or constrain model choice during discovery phases.


It simply requires that confirmatory tests be evaluated against pre-stated claims, and that exploratory work 
be identified as such.


---

## Where This Will Live

Pre-registration will be recorded in at least one and probably both of the following forms:

- a short `preregistration.md` file in the repository, or
- a public pre-registration platform (e.g., OSF) referenced from the repo.


The document will be:

- theory-forward and acquisition-level,
- written before _confirmatory_ experiments,
- updated only via addenda, **not overwritten**.


This keeps the process lightweight, transparent, and compatible with arXiv and workshop publication norms.


---

## Why Pre-Registration Helps This Collaboration

Pre-registration helps by giving all collaborators a shared reference point for what we believe should
happen before we see what actually happens.

It reduces ambiguity, protects intellectual honesty, and makes it easier to divide work between exploration
and confirmation without talking past one another.

Most importantly, it ensures that when results are surprising—or when nothing happens at all—we can say with
confidence whether the outcome challenges the theory, confirms it, or lies outside its scope.

