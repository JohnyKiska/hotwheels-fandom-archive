# 2007 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2007 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `4d92af5a63cec926750370ff5dbce96aad29c5b4`
- Manifest file size: 403,448 bytes
- Manifest SHA-256: `A0C89F2B300114404DE573B47E8349DBEF57E961F146B9AB8B1FDD466F3DFB72`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 4
- Product rows: 82
- Export columns: 21
- Excluded tables: 1 (collapsible navigation table)

## Product tables
- Monster Trucks: 57 rows, 5 source columns.
- Circuit Crashers: 7 rows, 5 source columns.
- Cyclone Spin-Outs: 10 rows, 4 source columns.
- Multipacks: 8 rows, 5 source columns.

## QA notes
- Source table order and row order are retained.
- Raw source headers and cells are preserved in the final two columns.
- Bundle contents and notes are retained as source notes, not expanded into inferred individual releases.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2007-MONSTER-JAM-SERIES.csv`
