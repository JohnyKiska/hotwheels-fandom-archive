# Mainline 2020: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2020/List of 2020 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `83b3020fb5bfca14070b0e0ec04afa6d62c75b60`
- File size: 825,837 bytes
- Manifest SHA-256: `23c0a8bb9a922bfb5c1c4d42018485dfa93d0be50c735315595243490ea728f0`
- Fandom revision: 812218

Machine-readable export: [MAINLINE-2020.csv](MAINLINE-2020.csv). It preserves source table index, section heading, row position, all six cells, and the source Collector-column label.

## Extraction method

Extracted both product tables independently, preserving source order and table boundaries. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Photo-cell filenames were retained where present.

## QA results

| Scope | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|
| Mainline annual table | 447 | 447 | 250 numeric values, 001–250 |
| Hot Wheels id table | 8 | 8 | `No #` on all 8 rows |
| Total source rows | 455 | 455 | 251 distinct raw values including `No #` |

Mainline table checks:

- 145 rows marked `(2nd Color)`.
- 15 Super Treasure Hunt rows and 15 Treasure Hunt rows (Series-label counts).
- No missing Toy #, Collector #, Model Name, Series or Series #.
- Two Photo cells contain filename placeholders: `File:GHD85 01.jpg` (Mainline row 201, Toy # GHD85) and `File:1996ce3a-55ce-466f-8e28-92c05bc2d121 large.jpg` (Mainline row 213, Toy # GHF27). Both are broken-media placeholders in the archived HTML, not usable image assets. The other 453 Photo cells are empty.
- 175 Collector # values have multiple rows across the combined source rows; within the annual Mainline sequence, Collector # remains non-unique because color variants share it.

Hot Wheels id table checks:

- 8 rows, Collector # is `No #` on all rows.
- Keep this as a separate Hot Wheels id scope; do not force these rows into the numeric Mainline Collector # sequence.

First Mainline row: `GHB45 | 001 | 2 Jet Z | HW Dream Garage New for 2020! | 1/10`.

Last Mainline row: `GHD10 | 250 | '10 Pro Stock Camaro | HW Race Team | 3/5`.

## Interpretation notes

- Toy # is unique within each extracted table, but not a universal global key.
- Collector # is scoped to the annual Mainline table; `No #` in Hot Wheels id remains a literal non-numeric identifier.
- Color labels and TH/STH series labels are source assertions and do not prove casting identity.
- The two Photo filenames are preserved for provenance but point to broken-media placeholders in this archived HTML.
- This archived Fandom page does not independently verify Mattel release status or tooling identity.
