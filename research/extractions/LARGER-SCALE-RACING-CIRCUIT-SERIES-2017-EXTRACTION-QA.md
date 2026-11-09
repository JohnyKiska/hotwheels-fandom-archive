# Racing Circuit Series (2017) extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Larger Scale/Hot Wheels Racing Series/Racing Circuit Series (2017) _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `7f08f2c3c1a094ca128c6bbdc0fc85402764ae36`
- Manifest file size: 332441 bytes
- Manifest SHA-256: `91B991FC7099B3A95DEFCDE2537E3E87F1FBC3B107B517C85A134892BAE3173E`
- Fandom revision ID: 752881
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 10
- Export columns: 21
- Other HTML tables excluded: 0

## Product tables
- Racing Circuit: 10 rows, 8 source columns. Headers: Col # | Toy # | Casting Name | Body Color | Wheel Type | Notes | Photo 1 Loose | Photo 2 Card

## QA notes
- Product tables identified by toy-number and casting/model-name headers; navigation and collapsible gallery tables excluded.
- Source table and row order retained.
- Raw source headers and cell text/image filenames preserved in the final two columns.
- Matching toy numbers, collection numbers, series labels, body colors, wheel types and notes mapped where source headers support them; remaining fields are retained in raw source data.
- Gallery extraction deferred.

## Output
- `research/extractions/LARGER-SCALE-RACING-CIRCUIT-SERIES-2017.csv`
