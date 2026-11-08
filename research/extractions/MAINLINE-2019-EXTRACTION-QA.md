# Mainline 2019: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2019/List of 2019 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `10c880e19a0a3eb972f9ae408e1d3b2c0a2f0e9c`
- File size: 827,965 bytes
- Manifest SHA-256: `132f5044b1663b3e660eaa3c8eccd9d67be0aa6a0d8d70e8523ca9ac5f9d0b71`
- Fandom revision: 812200

Machine-readable export: [MAINLINE-2019.csv](MAINLINE-2019.csv). The export preserves table index, section heading, row position, all six source columns, and the original Collector-column label.

## Extraction method

Extracted both product tables separately, preserving source order and table boundaries. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Empty Photo cells were retained.

## QA results

| Scope | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|
| Mainline annual table | 447 | 447 | 250 numeric values, 001–250 |
| Special Edition rows | 2 | 2 | `No #` on both rows |
| Total source rows | 449 | 449 | 251 distinct raw values including `No #` |

Mainline table checks:

- 154 rows marked `(2nd Color)`.
- 15 Super Treasure Hunt rows and 15 Treasure Hunt rows (Series-label counts).
- No missing Toy #, Collector #, Model Name, Series or Series #.
- All 449 Photo cells are empty.
- 186 Collector # values have multiple rows; Collector # is not a unique release key.

The two additional `No #` rows are special-edition entries: Tesla Greetings from Space Special Edition (GFJ71) and Barbie 60th Anniversary Special Edition (GJN99). Preserve these as separate source scope, not as additional numeric Mainline Collector # records.

First Mainline row: `FYB74 | 001 | Nissan Skyline GT-R (BNR32) | Nissan New for 2019! | 4/5`.

Last Mainline row: `FYB61 | 250 | Mod Rod | Factory Fresh New for 2019! | 8/10`.

## Interpretation notes

- Toy # is unique within this source snapshot, but not a universal global key.
- Collector # is scoped to the annual Mainline table; `No #` is retained literally for special-edition records.
- Color labels and TH/STH series labels are source assertions, not proof of casting identity.
- Photo is empty in every source row.
- This archived Fandom page does not independently verify Mattel release status or tooling identity.
