\[Header/Explanation\]


---

## Question/Start of Reply Restating Question

```
“Excellent question. The question was: Did you actually test this against modern vision models, 
like ResNet, or is this purely theoretical?”
```

### Clarifications

This question would be in relation to part in the Conclusion/Scope Section

> **Model behavior under information loss.**<br/>
> We note that modern convolutional vision models may continue to produce confident high-level
> classifications (e.g., “document,” “contains text”) even when stroke-scale information is
> provably absent at the resolution presented to the model. This behavior reflects the use of
> global structure, layout cues, and learned priors rather than access to evidentiary text
> signal. Such outputs are therefore not treated here as measurements of text existence.
> Instead, they serve to illustrate a potential divergence between model confidence and
> information-theoretic availability of evidence once sampling limits are violated. For this
> reason, model behavior is discussed only qualitatively and is not used as a primary anchor
> or experimental endpoint in this work.

## Answer (at least points)

```
That’s an excellent question. We did look at ResNet-style behavior, because it would have been irresponsible not to. What we observed was consistent with the theoretical framing: models can remain confident about document-level or layout-level properties even when the specific textual evidence is no longer present at the resolution they actually receive.
However, that observation is not what this paper is claiming. The goal here is not to evaluate model performance, but to establish a prior boundary: when sampling removes stroke-scale information, text existence is no longer a well-posed question. Model confidence beyond that point reflects inference around missing information, not access to it.
For that reason, we intentionally treat model behavior as a secondary illustration rather than a primary experimental anchor.
```

### Defusing remarks and other ideas

> I would have disappointed my younger, I-want-to-be-a-scientist self if i hadn't at last checked.
