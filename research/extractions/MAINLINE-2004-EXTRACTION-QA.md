# Mainline 2004: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2004/List of 2004 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `ef236a900471c55b016492ee3ac3481a704e1518`
- File size: 624,640 bytes
- Manifest SHA-256: `08b541d67ae2252fa09609f2da8cb0b907f82c0db30b775a984026d5a77d3b4c`
- Fandom revision: 811756

Machine-readable export: [MAINLINE-2004.csv](MAINLINE-2004.csv). It preserves table index, section heading, row position, original column count and raw headers. Optional fields are mapped by header name.

## Extraction method

Extracted all 16 product tables independently. Tables 1–12 use six columns; tables 13–16 use five columns and omit Series #. The CSV preserves the schema variation instead of treating Series # as a missing value.

## QA results

| Check | Result |
|---|---:|
| Product tables | 16 |
| Source rows | 268 |
| Unique Toy # | 213 |
| Unique Collector # | 213 |
| Numeric Collector # range | 001–212, continuous |
| Special Collector # | 000 (First Editions Mail-In) |
| Rows marked `(2nd Color)` | 48 |
| T-Hunt rows | 12 |
| Missing values in fields present in each table | 0 |
| Photo cells empty | 268 / 268 |
| Series # cells containing zero-width Unicode | 101 |

The 268 source rows represent 213 Collector # values because multiple color entries share identifiers. Toy # is not a unique row/release key.

## Table structure and scope

- 2004 First Editions: 155 rows, including standard First Editions, Zamac exclusives, Kmart exclusives and a mail-in entry.
- T-Hunt: 12 rows, Collector # 101–112.
- Series tables #113–162: Cereal Crunchers, Tat Rods, Star Spangled 2, Ferrari Heat, Final Run, Tag Rides, Crank Itz, Demonition, Scrapheads and Wastelanders.
- Series tables #163–212: Pride Rides, Roll Patrol, Track Aces and Wastelanders. These four tables use a five-column schema without Series #.

The First Editions table includes these Series labels: 106 standard `2004 First Editions`, 35 `2004 First Editions Zamac Exclusive`, 12 `2004 First Editions Kmart Exclusive`, one `Realistics Zamac Exclusive`, and one `2004 First Editions Mail-In` (Collector #000, Series #101/100). Keep these labels and scopes intact.

## Interpretation notes

- Numeric Collector # is continuous 001–212; Collector #000 is a separate mail-in record, not part of the numeric annual sequence.
- The 5-column tables do not have Series #; do not infer it.
- 101 Series # cells contain zero-width Unicode. Preserve raw values and normalize separately.
- T-Hunt is the source's literal category label; do not silently rename it to Treasure Hunt or Super Treasure Hunt.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
