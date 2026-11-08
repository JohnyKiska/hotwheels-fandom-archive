# Mainline 2024: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2024/List of 2024 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `5fa827146511beb8281cbaba4c2afdd4c49f494d`
- File size from Git tree: 824,601 bytes
- Manifest SHA-256: `04a77cf6212208cae5cd999637e8bd7825e8368581943291992ce388240239a5`
- Manifest blob SHA: `1a5933422177fa94fb09b1e9357e3a41c37094d6`

## Extraction method

The first full data table in the archived HTML was selected. Its header is:

`Toy # | Col.# | Model Name | Series | Series # | Photo`

All data rows were extracted in original document order. HTML tags were removed from cell text, common HTML entities decoded, whitespace normalized, and values retained as text. The Photo cell was retained as an empty field where the source cell is empty. No rows were deduplicated or merged.

Machine-readable export: [MAINLINE-2024.csv](MAINLINE-2024.csv).

## QA results

| Check | Result |
|---|---:|
| Data rows | 441 |
| Unique Toy # | 441 |
| Duplicate Toy # | 0 |
| Unique Collector # | 250 |
| Collector # range | 001–250 |
| Collector # values represented | 250 |
| Collector # with 2 rows | 125 |
| Collector # with 3 rows | 33 |
| Rows marked `(2nd Color)` in Model Name | 132 |
| Super Treasure Hunt rows (Series label) | 15 |
| Treasure Hunt rows excluding STH (Series label) | 15 |
| Rows with missing Toy #, Collector #, Model Name, Series or Series # | 0 |
| Rows with expected six columns | 441 / 441 |
| Duplicate Toy # values | None |
| Collector # order | Nondecreasing |
| Photo cells empty | 441 / 441 |

First data row: `HRY51 | 001 | Mazda Autozam | HW Dream Garage New for 2024! | 3/5`.

Last data row: `HRY93 | 250 | Ford Mustang Dark Horse | Then and Now New for 2024! | 10/10`.

## Interpretation and caveats

- 441 rows are not 441 unique castings. The table includes multiple release/color/treatment rows under the same Collector #.
- Collector # is not a unique release key. There are 158 Collector # values with multiple rows (125 with two rows and 33 with three rows).
- Toy # is unique within this extracted 2024 table, but should remain scoped to the relevant year/program/source rather than treated as a universal global identifier.
- `(2nd Color)` is retained in the Model Name field as a source label; it should not be used alone to infer casting identity or exact release relationship.
- STH and TH counts are derived from the Series text labels. They are row counts, not necessarily counts of distinct casting families.
- The Photo column is empty in all 441 source rows. This is source-page structure, not an extraction omission.
- This extraction is an archived Fandom page transcription. It does not independently verify Mattel release status, physical casting identity, tooling lineage, or regional distribution.

## Relationship to the earlier 2024 comparison

The prior research note records 49 exact normalized-name row matches between Car Culture 2016–2026 and a 2024 Mainline anchor. Those are name-match candidates, not confirmed casting/tooling identities. This extraction establishes a canonical source path and QA counts for the 2024 Mainline table. The comparison should be treated as an existing candidate run whose provenance is now anchored to this archived source; individual matches still require adjudication.
