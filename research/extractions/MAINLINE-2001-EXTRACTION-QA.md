# Mainline 2001: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2001/List of 2001 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `eccc12e667d7884da95240864ca613c17e351539`
- File size: 602,576 bytes
- Manifest SHA-256: `7b07b0758d216d1535e8a53cd0eb3582d61acc884f6b7772b6817e4bc6ab4f2d`
- Fandom revision: 806211

Machine-readable export: [MAINLINE-2001.csv](MAINLINE-2001.csv). It preserves table index, section heading, row position, original column count, and raw source headers.

## Extraction method

Extracted all 17 product tables separately. Fields are mapped by header name; the 2001 Hot Wheels and Final Run tables use five-column schemas without Series #. Store Exclusives has six columns but leaves Toy #, Collector # and Series # blank in all four rows.

## QA results

| Scope | Tables | Rows | Identifier scope |
|---|---:|---:|---|
| 2001 annual Mainline | 15 | 240 | Toy # and Collector # unique; Collector # 001–240 |
| 2001 Final Run | 1 | 12 | Separate Final Run program; Toy # 26992–27003, Collector # 001–012 |
| 2001 Store Exclusives | 1 | 4 | Toy # / Collector # / Series # blank in source |
| Total source rows | 17 | 256 | Preserve all three scopes |

Mainline checks:

- Collector # sequence 001–240 is continuous, no gaps.
- 12 Treasure Hunt rows.
- No `(2nd Color)` or Super Treasure Hunt rows identified.
- The 2001 Hot Wheels table has 144 rows and five columns, without Series #.
- All 240 Mainline rows have Toy # and Collector # populated.

Final Run:

- 12 rows, Collector # 001–012 and separate Final Run scope.
- These Collector # values overlap the Mainline numeric range but are not Mainline release identifiers.

Store Exclusives:

- Four rows: Vulture and Cabbin' Fever (Costco); Deora II and Shoe Box (Sam's Club).
- The archived table leaves Toy #, Collector # and Series # blank. Do not infer identifiers from nearby tables or assign them Mainline numbers.

## Interpretation notes

- Scope Collector # by program/year/source. The same numeric value may appear in both Mainline and Final Run.
- Preserve the five-column schemas for 2001 Hot Wheels and Final Run.
- Preserve Store Exclusives as source assertions with blank identifiers until independent evidence is found.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
