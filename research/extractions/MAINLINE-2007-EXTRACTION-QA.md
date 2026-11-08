# Mainline 2007: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2007/List of 2007 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `d037ecab5d706d7891248e4044c2f1547ec70230`
- File size: 658,121 bytes
- Manifest SHA-256: `8475ffba8415f3f288ebaf6c5b8d11170ca2213c85b2e139326df7130fb01185`
- Fandom revision: 804327

Machine-readable export: [MAINLINE-2007.csv](MAINLINE-2007.csv). It preserves table index, section heading, row position, all six source columns, and raw values.

## Extraction method

Extracted all 18 product tables separately, preserving source order and table boundaries. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Zero-width Unicode characters were retained in the raw Series # field.

## QA results

| Check | Result |
|---|---:|
| Product tables | 18 |
| Source rows | 315 |
| Unique Toy # | 193 |
| Unique Collector # | 180 |
| Collector # range | 001–180, no gaps |
| Rows marked `(2nd Color)` | 80 |
| Treasure Hunt rows | 12 |
| Super Treasure Hunt rows | 13 (12 regular section entries + 1 Toys R Us Promo) |
| Missing values in first five source fields | 0 |
| Photo cells empty | 315 / 315 |
| Series # cells containing zero-width Unicode | 315 / 315 |

The 315 rows represent 180 Collector # positions. Toy # is repeated across color variants; 78 Toy # values occur more than once in the annual source tables.

## Table structure

The page contains 18 separate tables, including 2007 New Models, Pop-Offs, Camaro, Hot Wheels Design, Taxi Rods, Gold Rides, Engine Revealers, Hummer, Street Beast II, X-Raycers, Aerial Attack, Hot Wheels Racing, Ragtops & Roadsters, Code Car, Track Stars, Treasure Hunts, All Stars, and Mystery Car.

The 2007 New Models table includes both standard entries and Kmart-exclusive entries in the Series field. The All Stars table includes Kmart and Walmart exclusive labels. Treasure Hunt entries include a separate Toys R Us Promo STH row.

## Interpretation notes

- Collector # is continuous 001–180; do not manufacture 181–250.
- Toy # is not unique to a row/release in 2007; repeated Toy # values are present across color variants.
- The Series field contains retailer exclusivity and promo qualifiers. Preserve the literal Series text.
- All Series # values contain zero-width Unicode characters. Keep the raw value and create a separate normalized value for matching.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
