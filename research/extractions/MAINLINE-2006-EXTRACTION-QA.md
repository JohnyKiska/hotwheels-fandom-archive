# Mainline 2006: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2006/List of 2006 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `f2b019243c51a63039fbbe6eaef5eef7fca805a0`
- File size: 675,172 bytes
- Manifest SHA-256: `15a88afc3efb8322a04a522ae825b97e2f88c8efd8a818545578fdd446643572`
- Fandom revision: 811755

Machine-readable export: [MAINLINE-2006.csv](MAINLINE-2006.csv). It preserves table index, section heading, row position, original column count, and all source columns. Optional fields are mapped by header name.

## Extraction method

Extracted all 17 product tables separately. Tables 1–15 and 17 use six columns; the `2006 Open Stock` table (table 16) uses five columns and has no Series # column. The CSV preserves this schema difference rather than inventing blank Series # source cells.

## QA results

| Scope | Tables | Rows | Collector # |
|---|---:|---:|---:|
| Mainline tables other than Open Stock | 16 | 222 | 127 numeric values across 001–122 and 219–223 |
| 2006 Open Stock | 1 | 141 | 96 numeric values, 123–218 |
| Total | 17 | 363 | 223 numeric values, 001–223 |

Overall checks:

- 223 unique Toy # values and 223 unique Collector # values.
- Collector # sequence 001–223 is continuous with no gaps.
- 74 rows marked `(2nd Color)`.
- 12 Treasure Hunt rows; no Series-label Super Treasure Hunt rows found.
- 90 Toy # values occur more than once, reflecting multiple source rows/color variants.
- No missing values in columns present in each table.
- Photo cells are empty.

## 2006 Open Stock schema

- 141 source rows, Collector # 123–218.
- The table header is `Toy # | Col.# | Model Name | Series | Photo`; Series # is absent, not missing.
- The 141 rows represent 96 Collector # positions, with multiple variants under some positions.
- Do not infer Series # from row order or adjacent tables.

## Interpretation notes

- Preserve the 2006 Open Stock table as a distinct source schema within the annual Mainline dataset.
- Toy # is not a unique row/release key in 2006; multiple color variants may share it.
- Collector # remains a continuous annual sequence from 001 through 223.
- TH is indicated in Series text; no STH row was identified by the Series label in this extraction.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
