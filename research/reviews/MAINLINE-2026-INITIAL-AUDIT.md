# Mainline 2026: initial catalog audit and visual review queue

## Scope and provenance

- Source: `research/extractions/MAINLINE-2026.csv`
- Source SHA at audit time: `442229bb7ae2883201d4b8b7a03b588e00704834`
- Source rows: 440
- Source columns retained without modification: Toy #, Collector #, Model Name, Series, Series #, Photo
- Review queue: `research/reviews/MAINLINE-2026-VISUAL-REVIEW-QUEUE.csv`
- Queue preserves every source row and adds a stable row ID, review class, priority, pending status, collector-group size, warning, and reason.
- No casting, variant, release, or packaging identity is promoted to canonical status.

## Inventory checks

| Check | Result |
|---|---:|
| Source rows | 440 |
| Unique Toy # | 440 |
| Unique Collector # | 250 |
| Collector numbers with multiple rows | 163 |
| Collector numbers with 3 rows | 27 |
| Rows explicitly marked 2nd Color | 148 |
| Rows explicitly marked 3rd Color | 27 |
| Treasure Hunt rows | 15 |
| Super Treasure Hunt rows | 15 |
| Retailer/channel-exclusive rows | 39 |
| Collector groups with differing base model names | 2 |
| Rows in flagged collector groups | 4 |

## Visual review priority

| Priority | Rows | Meaning |
|---|---:|---|
| P1 | 73 | TH/STH, retailer/channel exclusives, and collector-group naming conflicts |
| P2 | 186 | Explicit color variants and source-marked 2026 debuts |
| P3 | 181 | Remaining standard entries |

Priority is a work-order suggestion, not a confidence score or a statement that a release is confirmed.

## Specific data-quality flags

- **084:** `Polestar TRX` (JJJ47) versus `Polestar` (JJL49, marked 2nd Color). Do not normalize these names or assume the same casting from the table alone.
- **093:** `Coupé Clip` (JJJ55) versus `El Segundo Coupé Clip` (JJL05, marked 2nd Color). The source's own naming is inconsistent; physical comparison is required.

## Interpretation guardrails

- A Collector # groups source entries but is not a unique release or variant identifier.
- The source's `(2nd Color)` / `(3rd Color)` wording is retained as a source assertion, not accepted as proof of identical casting or a distinct release.
- Retailer-exclusive wording is a lead for packaging research. It does not by itself prove distribution, card revision, or a specific physical package.
- TH/STH labels are preserved from the source table; visual features and packaging still require inspection.
- All 440 source Photo cells are empty. This queue therefore identifies what to inspect, not what has already been visually verified.
- No physical sample images were available in this task, so no image-based conclusions are made.

## Next action

Start with P1 rows. For each available physical blister sample, record front/back card, barcode, copyright/base codes where visible, blister geometry, model deco/wheels, country of manufacture, and any retailer markings. Keep packaging evidence separate from casting and color-variant conclusions.
