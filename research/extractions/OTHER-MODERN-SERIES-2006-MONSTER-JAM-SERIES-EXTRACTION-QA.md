# 2006 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2006 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `c502887d3ad41439ecc8540068649f7feabb4589`
- Manifest file size: 377,353 bytes
- Manifest SHA-256: `2234F0274E5F4D4D1BE39FCB89587796E770EB64045524C61B691980A70398AD`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 3
- Product rows: 57
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible tables or non-product structures)

## Product tables
- Monster Trucks [ ]: 50 rows, 5 source columns. Headers: Toy # | Series # | Truck | Subset | Photo
- Multipacks [ ]: 6 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo
- Playsets [ ]: 1 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo

## QA notes
- Source table order and row order are retained.
- Raw source headers and cells are preserved in the final two columns.
- Fields not mapped to the normalized schema remain preserved in raw source data.
- Bundle contents and notes are retained as source notes, not expanded into inferred individual releases.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2006-MONSTER-JAM-SERIES.csv`
