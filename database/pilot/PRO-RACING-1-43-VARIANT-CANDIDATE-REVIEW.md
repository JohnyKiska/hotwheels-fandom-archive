# Pro Racing 1:43 variant-candidate review

Status: staged review proposal only. No canonical variants or releases are created.

## Scope

- 41 product-table source rows reviewed.
- 18 source casting-name candidates retained from the prior casting-candidate stage.
- Each row is assigned a provisional variant-candidate group, a same-candidate grouping, or a hold.
- Source year, color, tampo, notes, toy number, and packaging clues are not interchangeable. Packaging/set context belongs at release or assortment level unless it independently proves a deco difference.
- A candidate group is not an approved Variant identity. No records were inserted into canonical `variant`, `release`, `assortment`, or `image_relation` tables.

## Review outcomes

- 24 rows marked `candidate_variant`.
- 4 rows marked `same_variant_candidate`.
- 13 rows held for insufficient or conflicting evidence.
- 37 provisional variant-candidate groups across the 41 rows.

## Important decisions and cautions

1. Williams FW21 rows 1-2 differ by recorded color. Rows 20-21 have Compaq livery and #5/#6 tampo, but the source's 2001 year against the FW21 label needs independent review.
2. Stewart SF3 rows 4-5 are split only as source-derived #17 and #18 deco candidates.
3. McLaren MP4/15 rows 7-8 have David/Mika in the tampo field and remain separate candidates.
4. Ferrari F2001 rows 14 and 17 share #1 and are grouped as one variant candidate despite different pack context. Rows 15 and 16 remain separate provisional deco candidates; row 18 (#2), row 28 (Chrome), and row 31 (3-Pack, unspecified) are not collapsed into them.
5. Ferrari F1-2000 rows 11 and 30 are grouped as the same unspecified variant candidate. Row 27 is separate because Chrome is explicitly recorded.
6. Ferrari F2002 rows 22, 23, 29, and 32 are kept apart where a commemorative treatment, Chrome finish, or unresolved 3-Pack context may matter.
7. Ferrari F2004 rows 35 and 41 share a provisional Bahrain/#1 candidate group, but the exact image-to-row and release identity remain unresolved. Rows 37-38 share an unspecified #1 candidate; row 38's 2-Pack is packaging context, not by itself a new variant. #2 and King of the Desert remain separate candidates.
8. Ferrari 412 T1 row 36 is retained as a source label, with its 2004 page placement and “represents 1994” book-package note flagged as an anomaly.
9. Rows with no variant-defining source detail are held rather than inventing a baseline variant.

## Next validation needed

- Compare physical deco, base, wheel and interior details where actual product photos or reliable documentation exist.
- Resolve source anomalies and packaging context independently.
- Only after review should candidate groups be promoted into canonical Variant records and mapped to Release/Assortment records.
- Keep all Gallery relations uncreated until the corresponding subject and evidence level are established.

Detailed row-level proposal: `PRO-RACING-1-43-VARIANT-CANDIDATES.csv`.
