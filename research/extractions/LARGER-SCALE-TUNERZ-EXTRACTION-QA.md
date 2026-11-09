# Tunerz extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Larger Scale/Tunerz _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `aa26352018def547a39e4c594d7452d7c7b0a0b5`
- Manifest file size: 381382 bytes
- Manifest SHA-256: `71006133A94B5CFC7C0EA9B8ECD3E98AF27EA1276CF817F68D92032AB314751B`
- Fandom revision ID: 787594
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 21
- Export columns: 21
- Other HTML tables excluded: 1

## Product tables
- Models: 21 rows, 6 source columns. Headers: Year | Toy # | Casting Name | Color | Notes | Photo

## QA notes
- Product tables identified by toy-number and casting/model/name headers; navigation and collapsible gallery tables excluded.
- Source table and row order retained.
- Raw source headers and cell text/image filenames preserved in the final two columns.
- Matching toy numbers, year, body colors, tampo, base color/type, wheel type, country and notes mapped where source headers support them; remaining fields are retained in raw source data.
- Gallery extraction deferred.

## Output
- `research/extractions/LARGER-SCALE-TUNERZ.csv`
