# Landmarks and coordinates for crops

Started making official 2026-04-22. NOTE THAT NOT ALL FILENAMES LISTED HERE WILL HAVE BEEN CREATED/UPLOADED UNTIL I REMOVE THIS MESSAGE!

## Ink spill image

### DGS: 008105019

### Image identifiers

| Image Number (on DGS) | Characteristic | Measurement ID |
|:--- |:--- |:---            |
| `01920` | Dark (lower light for exposure) | `M01920` |
| `01921` | Light (higher light for exposure) | `M01921` |

### Region crops:

**Overview = complete, full-resolution image**
- `M01920` (Dark)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `2083×2730`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008105019_01920.jpg`
- `M01921` (Light)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `2184×2815`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008105019_01921.jpg`

**Ink, large region (`R_big_01`)**
- `M01920` (Dark)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:     
  - Image top-left `(x,y)` and `(w, h)` pixel coordinates in relation to full image
    - `@TODO x=#, y=#, w=#, h=#`
  - Filename
    - `fs008105019_inkovr_M01920_R_big_01_officialcrop.png`
- `M01921` (Light)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:     
  - Image top-left `(x,y)` and `(w, h)` pixel coordinates in relation to full image
    - `@TODO x=#, y=#, w=#, h=#`
  - Filename
    - `fs008105019_inkovr_M01921_R_big_01_officialcrop.png`

**Ink, small region (`R01_01`)**
- `M01920` (Dark)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:     
  - Image top-left `(x,y)` and `(w, h)` pixel coordinates in relation to full image
    - `@TODO x=#, y=#, w=#, h=#`
  - Filename
    - `fs008105019_inkovr_M01920_R01_01_officialcrop.png`
- `M01921` (Light)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:     
  - Image top-left `(x,y)` and `(w, h)` pixel coordinates in relation to full image
    - `@TODO x=#, y=#, w=#, h=#`
  - Filename
    - `fs008105019_inkovr_M01921_R01_01_officialcrop.png`

**Clean, large region (`R_big_02`)**
- `M01920` (Dark)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:     
  - Image top-left `(x,y)` and `(w, h)` pixel coordinates in relation to full image
    - `@TODO x=#, y=#, w=#, h=#`
  - Filename
    - `fs008105019_inkovr_M01920_R_big_02_officialcrop.png`
- `M01921` (Light)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:     
  - Image top-left `(x,y)` and `(w, h)` pixel coordinates in relation to full image
    - `@TODO x=#, y=#, w=#, h=#`
  - Filename
    - `fs008105019_inkovr_M01921_R_big_02_officialcrop.png`

**Clean, small region (`R02_01`)**
- `M01920` (Dark)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:     
  - Image top-left `(x,y)` and `(w, h)` pixel coordinates in relation to full image
    - `@TODO x=#, y=#, w=#, h=#`
  - Filename
    - `fs008105019_inkovr_M01920_R02_01_officialcrop.png`
- `M01921` (Light)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:     
  - Image top-left `(x,y)` and `(w, h)` pixel coordinates in relation to full image
    - `@TODO x=#, y=#, w=#, h=#`
  - Filename
    - `fs008105019_inkovr_M01921_R02_01_officialcrop.png`


## One repeated region with writing, different images with different depths of folio stacks between folio of focus and ROI reused writing surface

### DGS: 008105019

### Image identifiers

#### Tool 1: approximate folio depth

Here, for convenience in giving the characteristics, I introduce the definition: 

$$
d\left(M_i\right) = 723 - M_i
$$

where $d\left(M_i\right)$ is approximate folio depth from ???exposure??? for measurement / image $i$.

Then:
- $d\left(00723\right) = 0$
- $d\left(00706\right) = 17$
- $d\left(00697\right) = 26$

with obvious limitations and inexactitudes, not the least of which is that the number of pages in the codex is finite, and there are several codices in the DGS. Image `00662` is an image of a pair of folio from a different codex, so the result of the measurement, $d\left(00662\right)$, is not only inaccurate but meaningless in our context.

This mapping is provisional rather than exact. In general, for a microfilmed or otherwise measured codex, unimaged blank or visually uninformative leaves may exist, or an opening showing the verso of one folio and the recto of another may have been imaged twice due to an error with the first attempt or due to differences in the character of one surface as compared to another (a situation well illustrated by the previous example,) so image-number offset should be treated as an approximate physical-depth proxy rather than a guaranteed folio count. Image `00655` is the first we have of any opening of the codex in question showing a pair of folia divided by a book gutter, but it is highly unlikely that the measured $d\left(655\right) = 68$ corresponds to exactly 68 folia (not counting that on the left hand side of the image) existing in the folio stack.

#### Tool 2: Writing Line IDs

To identify the smallest regions, which are also the regions on which we desire to provisionally evaluate NTEC, I use vertical position within `R_big_01`along with the portions of words which are seen from the reused-as-binding manuscript, usually visible in the measurements (~~`675`~~, `685`, `697`, `701`, `706`, `711`, `717`, `719`, ~~`723`~~, where the strikethroughs are meaningful in showing that the letters creating the line ID either don't exist in the image (`675`) or have additional contextual parts (`723`). I leave in square brackets those letters which are hidden in all but `M00723`. Visible-but-uncertain letters are placed in parentheses with a question mark, e.g. `(n?)`.

The transcription convention&mdash;breaking as it does the conventions of paleography simultaneously with those of regular expressions&mdash;and the transcriptions themselves are the author's (Dave Black's), and responsibility for any errors (and the lack of clarity they may cause) lie solely with him.

**Writing Lines and IDs, from vertically 1st to 7th**

| Vertical Position | Writing Line ID | Shorthand ID |
| :--- | :--- | :--- |
| 1st | [regn]ab | ab1 |

#### Actual metadata

| Image Number (on DGS) | Characteristic | Measurement ID |
|:--- |:--- |:--- |
| `00675` | $d\left(685\right) = 48$,<br/>the region of interest, part of the reused writing surface, is not visible under/next to the folio stack, so no provisional comments about NTEC as it pertains to that region will nor should be given | `M00675` |
| `00685` | $d\left(685\right) = 38$,<br/>first time the reused writing surface is visible in the image, next to/under the folio stack | `M00685` |
| `00697` | $d\left(697\right) = 26$ | `M00697` |
| `00701` | $d\left(701\right) = 22$ | `M00701` |
| `00706` | $d\left(706\right) = 17$ | `M00706` |
| `00711` | $d\left(711\right) = 12$ | `M00711` |
| `00717` | $d\left(717\right) = 6$ | `M00717` |
| `00719` | $d\left(719\right) = 4$ | `M00719` |
| `00723` | $d\left(723\right) = 0$,<br/>reused writing surface is imaged as the surface of focus, not simply next to/under a folio stack | `M00723` |

### Region crops:

**Overview = complete, full-resolution image**
- M00675 (folio stack height value highest, 1st highest stack out of 9)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `4072×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00675.jpg`
- M00685 (folio stack height value highest out of those showing the reused writing surface but second-highest overall, 2st highest stack out of 9)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `4044×2797`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00685.jpg`
- M00697 (folio stack height value third highest, 3rd highest stack out of 9)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `4061×2813`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00697.jpg`
- M00701 (folio stack height value fourth highest, 4nd highest stack out of 9)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `4045×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00701.jpg`
- M00706 (folio stack height value fifth highest, 5th highest stack out of 9)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `4064×2782`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00706.jpg`
- M00711 (folio stack height value sixth highest, 6th highest stack out of 9)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `4047×2801`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00711.jpg`
- M00717 (folio stack height value seventh highest, 7th highest stack out of 9)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `4048×2804`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00717.jpg`
- M00719 (folio stack height value eighth highest, 8th highest stack out of 9)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `4040×2792`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00719.jpg`
- M00723 (folio stack height value of zero&mdash;this image shows the manuscript reuse as binding, specifically the real flyleaf and it now appears though possibly in the paste-down or ending inner cover originally, as the focal right-hand-side surface being imaged and thus the main recto folio in the image, making its folio attach height the seventh highest, stack, 9th highest stack out of 9 as well as the minimum value corresponding to zero-height)
  - Landmarks
    - Not applicable
  - Image dimensions
    - `4101×2847`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00723.jpg`

**Large region including several lines from the reused writing surface (`R_big_01`)**
- M00675 (stack height value 1st largest out of 9)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:
  - Image dimensions
    - `a×b`
  - Filename
    - Locally / Internally: `fs008835608_tbrrgt_M00675_R_big_01_unofficialcrop.png`

> **Warning!** This image (`M00685`) is shown _only_ to illustrate that the measurement dependence of NTEC can be tied to the regional dependence. This is an extreme case, where the specific measurement means that what will be the region of interest in later images is occluded from view by the approximate folio depth from ???exposure???, $d\left(685\right) = 48$; in other words, approximately 48 folios not only separate the reused manuscript from the supposed focus of the main leaf being imaged, but approximately 48 folios block the reused manuscript surface from any imaging light that might reflect off of it back to the camera. Trigonometry of the stack is being ignored.

- M00701 (folio stack height value fourth highest, 4nd highest stack out of 9)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:
  - Image dimensions
    - `4045×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00701.jpg`
- M00701 (folio stack height value fourth highest, 4nd highest stack out of 9)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:
  - Image dimensions
    - `4045×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00701.jpg`
- M00701 (folio stack height value fourth highest, 4nd highest stack out of 9)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:
  - Image dimensions
    - `4045×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00701.jpg`
- M00701 (folio stack height value fourth highest, 4nd highest stack out of 9)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:
  - Image dimensions
    - `4045×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00701.jpg`
- M00701 (folio stack height value fourth highest, 4nd highest stack out of 9)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:
  - Image dimensions
    - `4045×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00701.jpg`
- M00701 (folio stack height value fourth highest, 4nd highest stack out of 9)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:
  - Image dimensions
    - `4045×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00701.jpg`
- M00701 (folio stack height value fourth highest, 4nd highest stack out of 9)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:
  - Image dimensions
    - `4045×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00701.jpg`
- M00701 (folio stack height value fourth highest, 4nd highest stack out of 9)
  - Landmarks
    - Top-left:     
    - Top-right:    
    - Bottom-left:  
    - Bottom-right:
  - Image dimensions
    - `4045×2783`
  - Filename
    - _File_ not included in repo as per the policy of not rehosting full images
    - Locally / Internally: `FamilySearch_-_DGS008835608_00701.jpg`


