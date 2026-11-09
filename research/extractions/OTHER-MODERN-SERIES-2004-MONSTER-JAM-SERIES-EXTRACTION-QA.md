# 2004 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2004 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `60aa37476df80f1a446713ece7e7aa759da317ce`
- Manifest file size: 415,133 bytes
- Manifest SHA-256: `7C402127E30F3981B95A51978C36DFE61ABA93D2B439929EBE3A98B17F3CB29A`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 5
- Product rows: 67
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible tables or non-product structures)

## Product tables
- Monster Trucks [ ]: 23 rows, 5 source columns. Headers: Toy # | Series # | Truck | Subset | Photo
- Monster Trucks [ ]: 33 rows, 5 source columns. Headers: Toy # | Series # | Truck | Subset | Photo
- Crash & Smash [ ]: 8 rows, 5 source columns. Headers: Toy # | Truck | Series | Set # | Photo Carded
- Multipacks [ ]: 1 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo
- Playsets [ ]: 2 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo

## QA notes
- Source table order and row order are retained.
- Raw source headers and cells are preserved in the final two columns.
- Fields not mapped to the normalized schema remain preserved in raw source data.
- Bundle contents and notes are retained as source notes, not expanded into inferred individual releases.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2004-MONSTER-JAM-SERIES.csv`
