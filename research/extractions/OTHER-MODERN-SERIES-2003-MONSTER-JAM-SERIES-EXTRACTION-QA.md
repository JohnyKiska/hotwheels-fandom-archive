# 2003 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2003 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `515740f8a044bd3421cce60c40d5d6eb591c2b05`
- Manifest file size: 378,354 bytes
- Manifest SHA-256: `1BD2E90B65644A80CCA5B11CFA99D303A50B088F9C8C99852982F3C142A57603`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 2
- Product rows: 47
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible tables or non-product structures)

## Product tables
- Monster Trucks [ ]: 40 rows, 5 source columns. Headers: Toy # | Series # | Truck | Subset | Photo Carded
- Multipacks [ ]: 7 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo

## QA notes
- Source table order and row order are retained.
- Raw source headers and cells are preserved in the final two columns.
- Fields not mapped to the normalized schema remain preserved in raw source data.
- Bundle contents and notes are retained as source notes, not expanded into inferred individual releases.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2003-MONSTER-JAM-SERIES.csv`
