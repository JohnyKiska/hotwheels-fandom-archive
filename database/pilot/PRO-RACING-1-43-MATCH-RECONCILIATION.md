# Pro Racing 1:43 visual-to-catalog match reconciliation

Date: 2026-11-11  
Source page revision: 815866  
Source product table: 41 rows  
Gallery evidence: 55 images in 18 logical groups  
Visual review: 55/55 inspected

## Method

This crosswalk combines the archived page's product-table rows, Gallery captions/filenames, and the completed visual review. Product-table row numbers refer to the 1-based `Row within source` field in `LARGER-SCALE-PRO-RACING-1-43-SCALE.csv`.

A group-level association is not automatically an image-to-release relationship. The decision field deliberately distinguishes candidate group links, set-level links, subject references, and unresolved evidence. No canonical image-to-entity relations are inserted by this review.

## Results

| Disposition | Groups | Meaning |
|---|---:|---|
| Candidate group link accepted | 7 | Strong page-record match, while exact release/authenticity may remain unverified |
| Set-level only | 2 | Gallery evidence depicts an assortment/set, not individual product photos |
| Family/group-level only | 2 | Association is credible, but item-to-row mapping remains unresolved |
| Subject reference only | 1 | Digital/promotional asset, not physical-product evidence |
| Hold unlinked | 3 | Insufficient or conflicting evidence |
| Ancillary unlinked | 2 | Figure/helmet evidence, not a vehicle product image |
| Scope exception | 1 | Ford-captioned prototype has no corresponding Ford row in the page table |

## Important controls

- G09 is one four-pack image. Rows 26-29 are the four content/model records; do not create four image links from the single Gallery item.
- G17 is one six-car set with 14 evidence images. Candidate annual model rows are 6, 11, 14, 22, 33 and 37. This corrects the earlier draft's erroneous first two row references. These are content candidates, not proof that each view maps to a particular row.
- G11 remains group-level because the two Williams/Compaq images cannot yet be assigned reliably to #5 versus #6.
- G12 remains family-level because the Bahrain/Sakhir views cannot yet be split between rows 35 and 41.
- G16 is website/card artwork. It may reference the Ferrari F1-2000 subject but is not proof of a physical release.
- G01 is deliberately not auto-matched: the third image visibly carries an F1 2000 marking while the source grouping says Ferrari package prototype. That is not enough to choose between the F399 and F1-2000 rows.
- G02 is a scope/identity exception. The source caption says Ford, but the 41-row vehicle table contains no Ford entry and the inspected thumbnails do not resolve the make/model.
- G04 and G15 are ancillary figure/helmet subjects and remain outside vehicle product relations.
- G18 retains only a low-confidence F399-family candidate because the source caption itself says “Ferrari?”.

## Database disposition

The reconciliation is encoded in `pro-racing-1-43-reconciliation-seed.sql` as 55 idempotent `evidence_claim` records, one per Gallery source row, grouped under 18 review-group subjects. Accepted group/family/set/subject-reference dispositions are `cross_checked` with `probable` confidence; confirmed ancillary classifications are `cross_checked` with `verified` confidence; unresolved holds and the scope exception remain `hypothesis` with `unverified` confidence. These records preserve candidate rows, evidence basis, and unresolved questions in `value_text`. They do not create castings, variants, releases, assortments, or `image_relation` records. The SQLite validation script now executes both seeds twice and checks 55 claims across 18 groups, including the 43/12 cross-checked/hypothesis split. The updated workflow must be run manually to execute the new checks.

## Files

- `MATCH-RECONCILIATION.csv`: machine-readable 18-group crosswalk.
- `MATCH-RECONCILIATION.md`: method, decisions, and safeguards.
- `pro-racing-1-43-reconciliation-seed.sql`: 55 group-level evidence claims, no canonical entities or image relations.
