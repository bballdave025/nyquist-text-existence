# nyquist-text-existence

This repository explores fundamental constraints on detecting the *presence* of writing in digitized manuscript imagery.

The central claim is that many failures to detect faint, peripheral, or low–pixel-footprint text are not due to model choice or insufficient training data, but to irreversible information loss introduced by upstream decisions about spatial resolution, bit depth, or compression.

In particular, the work distinguishes between:

- **text existence** vs. **text recognition**,  
- **model uncertainty** vs. **information-theoretic absence**, and  
- **recoverable** vs. **unrecoverable** historical signal.

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

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

If you reuse material from this repository, please provide attribution in a standard **TASL** format (Title, Author, Source, License).  
See [`LICENSE`](LICENSE) or <https://creativecommons.org/licenses/by/4.0/> for details.
