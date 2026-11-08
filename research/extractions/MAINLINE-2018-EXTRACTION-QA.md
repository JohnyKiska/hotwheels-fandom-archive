# Mainline 2018: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2018/List of 2018 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `b69ee08e2c12059b523f79735d36dae0de2f525c`
- File size: 796,103 bytes
- Manifest SHA-256: `597b01ba03aa0b7867a13ac48c28a9d53ba455314beecf2a1ff70eed3cb7f85c`
- Fandom revision: 811760

Machine-readable export: [MAINLINE-2018.csv](MAINLINE-2018.csv). It preserves source table index, section heading, row position, all six source columns, and the raw Collector-column label.

## Extraction method

Extracted all 11 product tables separately, preserving table boundaries and source row order. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. The six source columns were retained. Empty Photo cells were preserved.

## QA results

| Scope | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|
| Mainline #1–365 | 365 | 365 | 365 numeric values, 001–365 |
| All additional sections | 104 | 104 | `No #` on all rows |
| Total source rows | 469 | 469 | 366 distinct raw values including `No #` |

Mainline table checks:

- 112 rows marked `(2nd Color)`.
- No missing Toy #, Collector #, Model Name, Series or Series #.
- All Photo cells are empty.

Additional section breakdown:

| Section | Rows |
|---|---:|
| Hot Wheels Treasure Hunts | 15 |
| Hot Wheels Super Treasure Hunts | 15 |
| HW 50th Race Team Super Ultimate Chase | 1 |
| Target Red Editions | 12 |
| Walmart Exclusive Zamac | 18 |
| Kmart Exclusives | 12 |
| Kroger Exclusives | 7 |
| Toys R Us Exclusive | 3 |
| Walgreens Exclusive | 1 |
| Daredevil Chase Variants | 20 |
| **Total additional rows** | **104** |

All additional rows use `No #` in the Collector # column. They are separately headed assortments/exclusive sections, not extra entries in the numeric 001–365 sequence. Preserve their source scopes.

## Source text anomalies

Six Series # cells contain zero-width Unicode characters (for example, a visually displayed `9/10` may include a trailing invisible code point). These characters are retained in the CSV export. Normalize for comparison only in a derived field; preserve the raw source value.

## Interpretation notes

- The annual Mainline table is 001–365. Do not combine all 469 source rows into one undifferentiated annual Mainline sequence.
- The additional TH/STH, Super Ultimate Chase, Red Editions, Zamac, retailer exclusives and Daredevil Chase sections have separate source context and `No #` Collector # values.
- Toy # is unique across this page's extracted rows, but this does not establish global uniqueness across years or other programs.
- Color labels are source text and do not prove casting identity.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
