# 2001 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2001 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `2d57bf517e6f7d44b79ca4c26563e07d626837d8`
- Manifest file size: 332,194 bytes
- Manifest SHA-256: `3E83AF505845167A7DC121DB73553D3430B43CFDE27DF85924A11D59B312D6E2`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 15
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible tables or non-product structures)

## Product tables
- Monster Trucks [ ]: 15 rows, 4 source columns. Headers: Toy # | Truck | Subset | Photo Carded

## QA notes
- Source table order and row order are retained.
- Raw source headers and cells are preserved in the final two columns.
- Fields not mapped to the normalized schema remain preserved in raw source data.
- Bundle contents and notes are retained as source notes, not expanded into inferred individual releases.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2001-MONSTER-JAM-SERIES.csv`
