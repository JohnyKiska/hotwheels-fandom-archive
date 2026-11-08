# Mainline 2016: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2016/List of 2016 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `e60ced5627d7d227f3a2f94a1a696b8ac6d960b6`
- File size: 847,876 bytes
- Manifest SHA-256: `b4deb2f3e2e96c6bac67801331d5b5d6251687fbac94da94a7ea876dd95efc36`
- Fandom revision: 724947

Machine-readable export: [MAINLINE-2016.csv](MAINLINE-2016.csv). It preserves table index, section heading, row position, all six source columns, and the original Collector-column label.

## Extraction method

Extracted all 33 product tables separately, preserving table boundaries and source order. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Invisible Unicode characters were not stripped; they remain in the CSV.

## QA results

| Scope | Tables | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|---:|
| Mainline series tables | 31 | 433 | 433 | 250 numeric values, 001–250 |
| Special Edition tables | 2 | 8 | 8 | `No #` on all rows |
| Total | 33 | 441 | 441 | 251 distinct raw values including `No #` |

Mainline table checks:

- 137 rows marked `(2nd Color)`.
- 15 Treasure Hunt and 15 Super Treasure Hunt rows (Series-label counts).
- No missing Toy #, Collector #, Model Name, Series or Series #.
- All Photo cells empty.

Additional sections:

- Kroger Exclusive Special Editions: 4 rows.
- Target-exclusive Special Editions: 4 rows.
- Both use `No #` and remain separate from the numeric Collector # sequence.

## Source text anomalies

397 of 441 Series # cells contain zero-width Unicode characters. This affects 389 Mainline rows and all 8 Special Edition rows. The CSV preserves these raw code points. A normalized comparison value may remove them, but the source value must remain unchanged in the archival record.

## Interpretation notes

- The 2016 annual Mainline data is distributed across 31 series-specific tables; do not assume one HTML table equals one year or one assortment.
- The 433 Mainline rows represent 250 Collector # positions with color/release variants, not 433 unique castings.
- TH/STH labels are present in the Series text for this page, unlike years where those categories are indicated by table headings. Preserve the original source representation rather than imposing one universal parsing rule.
- The 8 Special Edition rows have `No #` and separate source headings; do not add them to the numeric Mainline sequence.
- Toy # uniqueness within this page does not establish global uniqueness across years/programs.
