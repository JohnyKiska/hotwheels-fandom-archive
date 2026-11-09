# Small Shots Extraction QA

- Source: `Early Special Series/Small Shots _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `4da6e277464d3bb2bc4196b0d650376dea29c774`
- Source size (bytes): 415616
- Fandom revision ID: not present in source HTML
- Top-level HTML tables scanned: 4
- Product rows extracted: 14
- Embedded table image references: 26
- Links retained from product cells: 54
- Source manifest SHA-256: unavailable in current index/source metadata; left blank in CSV.
- CSV: `research/extractions/EARLY-SPECIAL-SERIES-SMALL-SHOTS.csv`

## Table-level review

| Table | Product rows | Images | Links | Headers |
|---:|---:|---:|---:|---|
| 1 | 4 | 8 | 16 | Toy #; Name; Year; Country; Notes; Photo; Photo |
| 2 | 2 | 2 | 6 | Toy #; Name; Year; Country; Notes; Photo |
| 3 | 4 | 8 | 16 | Toy #; Name; Year; Country; Notes; Photo; Photo |
| 4 | 4 | 8 | 16 | Toy #; Name; Year; Country; Notes; Photo; Photo |

## Extraction checks

- Rows retained in source order; table/row positions, nearest preceding section heading, headers, raw row HTML, cell HTML/text, links and image metadata preserved.
- Header-only rows excluded, including legacy bold-cell headers.
- Separate product tables retained without merging; no normalization or deduplication.
- Separate gallery entries are not extracted in this pass.
