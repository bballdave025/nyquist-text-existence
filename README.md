# nyquist-text-existence

This repository explores fundamental constratints on detecting the presence of writing in digitized manuscript imagery.

The central claim is that the existence of text in an image depends on representational thresholds imposed during acquisition, sampline, and subsequent digital derivation. These thresholds become especially visible in model behavior: many apparent failures to detect peripheral, low–pixel-footprint, or faint writing reflect information-theoretic absence rather than deficiencies in architecture or training.

In particular, the work distinguishes between:

- **text existence** vs. **text recognition**,  
- **model uncertainty** vs. **information-theoretic absence**, and  
- **recoverable** vs. **unrecoverable** historical signal.

See the [preregistration document](PREREGISTRATION_NTEC_2026-03-02.md) for preregistered claims, hypotheses, falsification clarification, and scope of the study and forthcoming publication. It has been submitted to OSF. ~~and is serving as the base for a presentation at the [Family History Technology Workshop](https://fhtw.byu.edu/), [2026](https://docs.google.com/document/d/1UKWjL9LTcZqTyATYb1-eTa6NnC7jR-u9yzcrWyczWms); the Workshop location and schedule didn't allow for presentation.~~

See [`thematic_image_info.md`](thematic_image_info.md) for discussion of representative images and their role in motivating the Nyquist text-existence argument.

---

## Contents

This repository includes:

- [vision](IP_Plus_Vision_-_Nyquist_rev-2026-01-07.md) and [scope](IP_Plus_Vision_-_Nyquist_rev-2026-01-07.md) documents,
- Nyquist-based technical notes,
- experimental design scaffolding,
- and thematic examples linking theory to manuscript reuse contexts.

The emphasis is on clarifying *what cannot be recovered* once sampling limits are exceeded, rather than on proposing new recognition pipelines.

---

## License and attribution

### Code

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The code in this project is licensed under the **MIT License**.

---

### Content, preregistration, etc.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

If you reuse material from this repository, please provide attribution in a standard **TASL** format (Title, Author, Source, License).  
See [`LICENSE`](LICENSE) or <https://creativecommons.org/licenses/by/4.0/> for details.
