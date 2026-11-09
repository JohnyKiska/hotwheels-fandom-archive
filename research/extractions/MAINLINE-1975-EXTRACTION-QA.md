# Mainline 1975 Extraction QA

## Source and provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Source path: `ALLHW/1975/List of 1975 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `9fef56a70d6b0dbcc01b189e00a3cfd5d97ef516`
- Git tree / Contents API size: 396,881 bytes
- Manifest SHA-256: `489184abad54206982a3da79b73d63760fc2f8797a69e09744971b57e86ee3c5`
- Fandom revision: 717417

## Extraction result

- HTML tables found: 2
- Product tables extracted: 1 (table index 0)
- Navigation table excluded: table index 1
- Source columns: Toy # | Casting | Series Name / # | Notes | Wheel Type | Photo / Color
- Extracted product rows: 31
- Source column count observed: 6
- Unique nonblank Toy #: 31
- Blank Toy #: 0
- Repeated Toy # groups: 0
- Unique casting names: 31
- Repeated casting-name groups: 0
- Collector # / Series # columns: absent
- Series values: `1975 Flying Colors` (31)
- Nonblank Notes: `MotoCross`: VHTF; `Street Eater`: VHTF
- Nonblank Wheel Type metadata: 31 rows
- Nonblank Photo metadata: 31 rows

## Structural observations

The page contains one six-column product table and a separate yearly-navigation table. The product table's Wheel Type and Photo cells are predominantly image-only. Their visible text is empty, so image `alt` labels and `data-image-name` filenames were captured into the corresponding export fields. This preserves useful source metadata without pretending that it was ordinary cell text.

The Wheel Type image labels vary. Most rows use a Redline image label; exceptions include RWSP Wheel, MW - 7035bf, and the Porsche Carrera row with two wheel-image labels. The Photo column contains per-row image labels / filenames.

The Porsche Carrera casting cell contains a two-line source note: `Porsche Carrera org / P-911 changed to`. The Wheel Type cell contains two image labels separated by a slash. Both were retained as source-derived text/metadata. This is not normalized into a definitive casting rename.

## Duplicate and identifier checks

- Repeated Toy # groups: []
- Repeated casting-name groups: []
- No rows were deduplicated or merged.

## Output

- `research/extractions/MAINLINE-1975.csv`
- `research/extractions/MAINLINE-1975-EXTRACTION-QA.md`

All source rows are retained in source order. Raw source headers and per-cell text/image metadata are included in the CSV.
