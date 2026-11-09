# Steering Rigs Extraction QA

- Source: `Early Special Series/Steering Rigs _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `ce3a05a93b130526cb65fd83fe323c0970a50b9f`
- Source size (bytes): 420696
- Fandom revision ID: not present in source HTML
- Top-level HTML tables scanned: 2
- Product rows extracted: 34
- Embedded table image references: 90
- Links retained from product cells: 124
- Source manifest SHA-256: unavailable in current index/source metadata; left blank in CSV.
- CSV: `research/extractions/EARLY-SPECIAL-SERIES-STEERING-RIGS.csv`

## Table-level review

| Table | Product rows | Images | Links | Headers |
|---:|---:|---:|---:|---|
| 1 | 22 | 66 | 88 | Year; Toy #; Name; Cab Color; Trailer Color; Country; Notes; Cab Photo; Full Photo; Boxed Photo |
| 2 | 12 | 24 | 36 | Toy #; Name; Color; Notes; Photo Loose; Photo Carded |

## Extraction checks

- Rows retained in source order; table/row positions, nearest preceding section heading, headers, raw row HTML, cell HTML/text, links and image metadata preserved.
- Header-only rows excluded, including legacy bold-cell headers.
- Separate product tables retained without merging; no normalization or deduplication.
- Separate gallery entries are not extracted in this pass.
