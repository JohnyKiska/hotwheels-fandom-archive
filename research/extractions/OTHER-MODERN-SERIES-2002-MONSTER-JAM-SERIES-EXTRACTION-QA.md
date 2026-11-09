# 2002 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2002 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `64eb25847101bee7ac04b7dd1af6d5c5abcb0656`
- Manifest file size: 365,494 bytes
- Manifest SHA-256: `739F896BEDFB56903A68325747C63B62631BC1E840447503E2322CE401C19E71`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 3
- Product rows: 33
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible tables or non-product structures)

## Product tables
- Monster Trucks [ ]: 24 rows, 4 source columns. Headers: Toy # | Truck | Subset | Photo Carded
- Multipacks [ ]: 7 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo
- Playsets [ ]: 2 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo

## QA notes
- Source table order and row order are retained.
- Raw source headers and cells are preserved in the final two columns.
- Fields not mapped to the normalized schema remain preserved in raw source data.
- Bundle contents and notes are retained as source notes, not expanded into inferred individual releases.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2002-MONSTER-JAM-SERIES.csv`
