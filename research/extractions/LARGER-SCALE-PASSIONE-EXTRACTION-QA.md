# Passione extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Larger Scale/Passione _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `21f9bef221b7448556b80a10c685cbd37000cf7b`
- Manifest file size: 349596 bytes
- Manifest SHA-256: `2343C58D57D9A84229C2BF648FA24C816DA046308224B9107376601DB715407C`
- Fandom revision ID: 787645
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 7
- Export columns: 21
- Other HTML tables excluded: 1

## Product tables
- 2001: 7 rows, 5 source columns. Headers: Toy # | Casting Name | Color | Notes | Photo

## QA notes
- Product tables identified by toy-number and casting/model/name headers; navigation and collapsible gallery tables excluded.
- Source table and row order retained.
- Raw source headers and cell text/image filenames preserved in the final two columns.
- Matching toy numbers, collection numbers, year, series labels, body colors, wheel types, country and notes mapped where source headers support them; remaining fields are retained in raw source data.
- Gallery extraction deferred.

## Output
- `research/extractions/LARGER-SCALE-PASSIONE.csv`
