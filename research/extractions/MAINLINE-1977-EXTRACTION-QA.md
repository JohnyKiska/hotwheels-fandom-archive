# Mainline 1977 Extraction QA

## Source provenance
- Source: `ALLHW/1977/List of 1977 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Archive branch: `archive/historical-html-1968-2026`
- Git blob SHA: `4cc171bfe55e5dbb14485ec2aa5afd5827ab378e`
- Git tree size: 495,751 bytes
- Manifest SHA-256: `7d737b216a2988b30371e5bc7dd28e6d4f5c04ce3a52955bf69105d51b7bc75d`
- Fandom revision: 782818

## Extraction
- One product table, source table index 0.
- One additional yearly-navigation table was excluded.
- Source headers: Toy #, Casting, Series Name / #, Versions / Notes, Wheel Type, Photo / Color.
- Product rows: **103**.
- Source schema: 6 columns throughout.
- Rows preserved in source order. No rows merged or deduplicated.
- Original source headers and all six source cell values are retained in the CSV.

## Identifier and duplicate QA
- Unique nonblank Toy #: **69**.
- Blank Toy #: **1**.
- Repeated Toy # groups: **25**.
- Repeated casting-name groups: **29**.
- Unique casting names: **67**.
- No Collector # or Series # columns in the source.

Repeated Toy # groups:
- 6976: 3 rows
- 7621: 2 rows
- 7630: 2 rows
- 7661: 3 rows
- 7670: 2 rows
- 8240: 2 rows
- 8258: 2 rows
- 8259: 2 rows
- 9119: 2 rows
- 9185: 2 rows
- 9203: 2 rows
- 9205: 2 rows
- 9208: 3 rows
- 9210: 2 rows
- 9505: 5 rows
- 9638: 2 rows
- 9639: 2 rows
- 9640: 2 rows
- 9641: 2 rows
- 9642: 4 rows
- 9644: 2 rows
- 9646: 2 rows
- 9648: 2 rows
- 9649: 2 rows
- 9793: 2 rows

## Source-specific observations
- The table combines 1977 Flying Colors entries, Super Chromes, a Flying Colors entry without a numbered suffix, and Thrill Drivers Corkscrew Track Set entries. The exact source Series Name / # values are retained without normalizing them into a collection taxonomy.
- All 103 Wheel Type cells are blank.
- The Photo / Color column contains 96 blank cells and 7 color labels: Light Blue, Dark Blue, Light Green, Red, Gray, Plum, Yellow. These are retained as Color, not interpreted as photo references.
- Versions / Notes carries distinctions such as 1st/2nd/3rd Version and wheel-related descriptions. These are retained as source Notes.
- One row has a blank Toy #; it remains present as a source row.
- Duplicate Toy # and casting-name groups are source-level observations only, not evidence that rows represent the same release or casting identity.

## Output
- `research/extractions/MAINLINE-1977.csv`
- `research/extractions/MAINLINE-1977-EXTRACTION-QA.md`
