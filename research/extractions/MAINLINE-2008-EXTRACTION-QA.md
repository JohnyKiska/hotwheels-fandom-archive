# Mainline 2008: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2008/List of 2008 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `7ae49f41959fa60151ee249045dc37b8b25f3701`
- File size: 696,053 bytes
- Manifest SHA-256: `fa2aa5fa55ff7f1ea1374b85519da6fb23be3659e3f8a795b8bb417e756405ea`
- Fandom revision: 803369

Machine-readable export: [MAINLINE-2008.csv](MAINLINE-2008.csv). It preserves source table index, section heading, row position, all six source columns, and raw values.

## Extraction method

Extracted all 18 product tables separately, preserving table boundaries and source order. HTML tags were removed from cell text, common entities decoded, and whitespace normalized. Empty Photo cells were retained.

## QA results

| Check | Result |
|---|---:|
| Product tables | 18 |
| Source rows | 358 |
| Unique Toy # | 208 |
| Unique Collector # | 196 |
| Collector # range | 001–196, no gaps |
| Rows marked `(2nd Color)` | 91 |
| Treasure Hunt rows | 12 |
| Super Treasure Hunt rows | 12 |
| Missing values in first five source fields | 0 |
| Photo cells empty | 358 / 358 |

The 358 rows represent 196 Collector # positions, not 358 unique releases. Toy # is repeated across color entries: 88 Toy # values occur more than once in the annual tables.

## Table structure

The annual page is split across:

- 2008 New Models
- All Stars
- Web Trading Cars
- Track Stars
- Team assortments (Exotics, Surf's Up, Jet Rides, Rat Rods, Volkswagen, Muscle Mania, Hot Trucks, Ford Racing, Hot Wheels Racing, Custom Bikes, Engine Revealers, Drag Racing)
- Treasure Hunts
- Mystery Cars

These are all part of the same annual list, but their table boundaries and local Series # scopes must be retained.

## Interpretation notes

- Collector # is continuous 001–196; do not manufacture 197–250.
- Toy # is not unique to a row/release in 2008. Multiple color entries can share a Toy #.
- TH/STH are indicated in Series text.
- Preserve the table/assortment scope for local Series # values, especially the 1/4 Team tables.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
