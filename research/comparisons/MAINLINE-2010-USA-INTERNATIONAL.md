# Mainline 2010: USA and International comparison

## Source provenance

Both files are from `JohnyKiska/hotwheels`, branch `archive/historical-html-1968-2026`.

| Source | Path | Git blob SHA | Size | Fandom revision | Manifest SHA-256 |
|---|---|---|---:|---:|---|
| USA | `ALLHW/2010/List of 2010 Hot Wheels _ Hot Wheels Wiki _ Fandom.html` | `26c08a2134f9c4df6b4c634a2cf9b3c4e941966c` | 808,271 bytes | 815649 | `08de99b8152225a6c44eabec762fa2d82e094e6b559a1befbf4b34037ea362d7` |
| International | `ALLHW/2010/List of 2010 Hot Wheels (International) _ Hot Wheels Wiki _ Fandom.html` | `2ef979cd1dda8236096ed4eb9c490aff5b6ce8e1` | 593,595 bytes | 815650 | `005479a8abb31b038071b1699146e27806416e4319d75b81109db68ed0d91644` |

Machine-readable row exports preserve table index, section heading, row position, all six source columns, and the source's Collector-column label:

- [MAINLINE-2010-USA.csv](MAINLINE-2010-USA.csv)
- [MAINLINE-2010-INTERNATIONAL.csv](MAINLINE-2010-INTERNATIONAL.csv)

## Extraction and structural QA

| Check | USA | International |
|---|---:|---:|
| Data tables | 28 | 24 |
| Extracted source rows | 440 | 228 |
| Unique Toy # values | 252 | 226 |
| Unique Collector # values | 240 | 214 |
| Collector # span | 001–240 | 001–214 |
| Rows missing one of the first five fields | 0 | 0 |
| Photo cells empty | all | all |

### USA page structure

The USA page has 26 principal tables (422 rows) plus two separately headed tire-exclusive sections:

- Goodyear Tire Exclusives: 8 rows
- BF Goodrich Tire Exclusives: 10 rows

The 18 tire-exclusive rows must be preserved with their section provenance. They overlap with records in the principal tables; 16 exact six-column row values recur elsewhere on the page. The remaining rows may represent alternate color/section presentations. Do not flatten these sections and deduplicate by Toy # or text alone.

Across all 440 source rows, 122 Toy # values occur more than once, producing 188 row appearances beyond the unique Toy # count. This is partly due to multiple color entries under a shared Toy # and partly due to the separately listed tire-exclusive sections. For example, R0916 is listed for three color labels in the 2010 New Models table.

### International page structure

The International page has 24 principal tables and 228 source rows. It has 226 unique Toy # values. R7504 occurs three times in the Muscle Mania section, with the base, second-color, and third-color labels. All 214 Collector # values from 001 through 214 are represented.

## Cross-page comparison

Comparing unique Toy # sets:

- Shared Toy # values: 213
- USA-only Toy # values: 39
- International-only Toy # values: 13

For the 213 shared Toy # values, comparing the first source occurrence per Toy # (a preliminary index comparison, not release adjudication):

- 192 have the same normalized Model Name.
- 21 have different Model Name text.
- Only 11 have the same Collector #.
- 202 have different Collector # values.

The different Collector # values show that Collector # numbering is not interchangeable between these two page scopes. The two pages also use different top-level series labels and numbering conventions: USA begins with `2010 New Models` (44 positions), while International begins with `2010 HW Premiere` (52 positions). Subsequent section offsets differ. Do not map Collector # across the pages without an explicit cross-source relation.

### Shared Toy # with differing first-occurrence Model Name

These are text discrepancies to investigate, not proof of different physical products:

| Toy # | USA first occurrence | International first occurrence |
|---|---|---|
| R0957 | 037 — Nissan 370Z | 042 — '09 Nissan 370Z |
| R6455 | 040 — '86 Monte Carlo SS | 048 — '73 Ford Falcon XB |
| R7440 | 051 — Ford GTX1 | 059 — Ford GTX-1 |
| R7452 | 051 — Ford GTX1 | 059 — Ford GTX-1 |
| R7469 | 068 — Dieselboy | 076 — Diesel Boy |
| R7498 | 073 — '40s Woodie | 081 — '40's Woodie |
| R7506 | 081 — '69 Cougar Eliminator | 089 — '69 Mercury Cougar Eliminator |
| R7509 | 084 — '69 Pontiac GTO Judge | 092 — '69 Pontiac GTO |
| R7519 | 094 — '70 Plymouth Road Runner | 102 — '70 Roadrunner |
| R7525 | 100 — Dodge Challenger SRT8 | 108 — '08 Dodge Challenger SRT8 |
| R7532 | 107 — '56 Ford F-100 | 115 — '56 Ford |
| R7538 | 113 — Hummer H2 | 121 — Hummer H2 SUT |
| R7539 | 114 — '09 Ford F-150 | 122 — 2009 Ford F-150 |
| R7557 | 132 — Ford Mustang Fastback | 130 — '65 Mustang Fastback |
| R7558 | 133 — C6 Corvette | 131 — Corvette C6 Convertible |
| R7561 | 136 — '70 Chevy Chevelle | 134 — '70 Chevelle Convertible |
| R7563 | 138 — '07 Ford Shelby GT500 | 136 — '07 Shelby GT-500 |
| R7566 | 141 — '37 Ford | 139 — '37 Ford Woodie |
| R7571 | 146 — '40 Ford Pickup | 144 — '40 Ford |
| R7618 | 189 — Toyota Off-Road Truck | 187 — Toyota Baja Truck |
| R7642 | 213 — Corvette Stingray | 211 — Monster Vette |

**High-priority anomalies:** R6455 and R7642 have substantially different model names across the two pages. R7557, R7558, R7561, R7566, R7571 and R7618 also have body/model wording that may be materially different rather than simple punctuation. These need direct source-row/image/packaging review before assigning a shared release or casting identity.

## Interpretation boundaries

- Toy # is not unique to a single source row in 2010. Color-labelled rows may share Toy # and Collector #.
- Collector # is also not a universal cross-region identifier. It is page-scope-specific and shifts substantially between USA and International.
- The 2010 USA tire-exclusive tables are separate source sections. Preserve each row occurrence and section context; do not silently merge with the principal list.
- A shared Toy # is a useful cross-source candidate key, not proof that all associated rows describe the same color variant, release, packaging or tooling.
- Differences in model names may reflect naming conventions, source errors, regional products or genuine product differences. This comparison alone cannot decide which.
- The CSV exports preserve row-level provenance, including repeated rows, so later normalization can adjudicate without losing source structure.

## Remaining 2010 work

- [ ] Inspect all 21 shared-Toy# name discrepancies, prioritizing R6455 and R7642.
- [ ] Determine whether the 13 International-only and 39 USA-only Toy # values reflect region-exclusive products, page coverage differences, or source omissions.
- [ ] Adjudicate the 18 USA tire-exclusive section rows against principal table rows and packaging evidence.
- [ ] Verify color labels and repeated Toy # behavior against packaging/catalog evidence before modelling release identity.
