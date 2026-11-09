# La Storia extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Larger Scale/La Storia _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `12d5ee8703f2239c5339e659e66e52ac1803111a`
- Manifest file size: 350517 bytes
- Manifest SHA-256: `89886A363968969D2954AE40CCE8682BCC47F9574893A0893DC438F8FA3CDC56`
- Fandom revision ID: 787414
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 5
- Export columns: 21
- Other HTML tables excluded: 1

## Product tables
- La Storia: 5 rows, 5 source columns. Headers: Toy # | Casting Name | Color | Notes | Photo

## QA notes
- Product tables identified by toy-number and casting/model-name headers; navigation and collapsible gallery tables excluded.
- Source table and row order retained.
- Raw source headers and cell text/image filenames preserved in the final two columns.
- Matching toy numbers, collection numbers, series labels, body colors, wheel types and notes mapped where source headers support them; remaining fields are retained in raw source data.
- Gallery extraction deferred.

## Output
- `research/extractions/LARGER-SCALE-LA-STORIA.csv`
