# Mainline 2017: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2017/List of 2017 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `650229c87be1404fa0451899b268748d0368bc58`
- File size: 777,520 bytes
- Manifest SHA-256: `ed6c540d57548f9cce6a47eb0e0760137c159fbba82847ea4d89f7561b4af709`
- Fandom revision: 781777

Machine-readable export: [MAINLINE-2017.csv](MAINLINE-2017.csv). It preserves source table index, section heading, row position, all six source columns, and raw Collector-column labels.

## Extraction method

Extracted all 10 product tables independently, preserving source order and table boundaries. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Empty Photo cells were retained.

## QA results

| Scope | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|
| Mainline #1–365 | 365 | 365 | 365 numeric values, 001–365 |
| Additional sections | 85 | 85 | `No #` on all rows |
| Total source rows | 450 | 450 | 366 distinct raw values including `No #` |

Mainline table:

- 365 rows, unique Toy # and Collector # values 001–365.
- 119 rows marked `(2nd Color)`.
- No missing Toy #, Collector #, Model Name, Series or Series #.
- All Photo cells empty.

Additional sections (85 rows):

- Hot Wheels Treasure Hunts [ ]: 15 rows
- Hot Wheels Super Treasure Hunts [ ]: 15 rows
- Target Red Editions [ ]: 12 rows
- Walmart Exclusive Zamac [ ]: 18 rows
- Kmart Exclusives [ ]: 12 rows
- Kroger Exclusives [ ]: 4 rows
- Toys R Us Exclusive [ ]: 3 rows
- Walgreens Exclusive [ ]: 1 rows
- Digital Circuit Chase Variants [ ]: 5 rows

The additional tables include separate Treasure Hunt and Super Treasure Hunt sections (15 rows each), Red Edition, retailer exclusives, and HW Digital Circuit. These rows use `No #` in Collector # and must not be appended to the numeric 001–365 Mainline sequence.

## Interpretation notes

- Section headings carry semantic information not necessarily present in the Series cell. For example, TH/STH identity is indicated by separate table headings, not by the row's Series value.
- Keep source table/section scope when storing records. Do not infer TH/STH solely from Series text.
- Toy # is unique within this page's extracted rows, but this does not establish global uniqueness across years/programs.
- Color labels are source text and do not prove casting identity.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
