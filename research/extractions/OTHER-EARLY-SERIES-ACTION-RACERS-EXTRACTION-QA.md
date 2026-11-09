# Action Racers Extraction QA

- Source: `Other Early Series/Action Racers _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `2a204aee5df7394d298dd2891b8e2bb38f3b3ed5`
- Source size (bytes): 623368
- Fandom revision ID: 
- Top-level HTML tables scanned: 2
- Product rows extracted: 67
- Embedded table image references: 67
- Links retained from product cells: 109
- Source manifest SHA-256: `3289E12DDDF4C778B29B6231BB7B203DBE7EF926F990E98BE145D1D4FA154B45`
- CSV: `research/extractions/OTHER-EARLY-SERIES-ACTION-RACERS.csv`

## Table-level review

| Table | Product rows | Images | Links | Headers |
|---:|---:|---:|---:|---|
| 1 | 65 | 65 | 105 | Toy #; Name; Series; Color; Photo |
| 2 | 2 | 2 | 4 | Toy #; Name; Series; Color; Photo |

## Extraction checks

- Rows retained in source order with table/row positions, nearest preceding section heading, headers, raw row HTML, cell HTML/text, links and image metadata.
- Header-only rows excluded, including legacy bold-cell headers.
- Separate product tables retained without merging; no normalization or deduplication.
- Separate gallery entries are not extracted in this pass.
