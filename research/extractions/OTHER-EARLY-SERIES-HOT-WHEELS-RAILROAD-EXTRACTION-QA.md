# Hot Wheels Railroad Extraction QA

- Source: `Other Early Series/Hot Wheels Railroad _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `366d954a1fa747c5d19b8bd6460351826fa0a7f8`
- Source size (bytes): 357350
- Fandom revision ID: 
- Top-level HTML tables scanned: 3
- Product rows extracted: 31
- Embedded table image references: 31
- Links retained from product cells: 98
- Source manifest SHA-256: `BB963E057728779024516D2A4F7BF925B62C40DD9748E568BB41E3E9B7CEC85E`
- CSV: `research/extractions/OTHER-EARLY-SERIES-HOT-WHEELS-RAILROAD.csv`

## Table-level review

| Table | Product rows | Images | Links | Headers |
|---:|---:|---:|---:|---|
| 1 | 14 | 14 | 42 | Year; Model Name; Color; Railroad/Company Represented; Base Color / Type; Country; Number; Photo |
| 2 | 5 | 5 | 20 | Year; Bundle name; Car 1; Car 2; Car 3; Number; Photo |
| 3 | 12 | 12 | 36 | Year; Name; Cars included; Notes; Number; Photo |

## Extraction checks

- Rows retained in source order with table/row positions, nearest preceding section heading, headers, raw row HTML, cell HTML/text, links and image metadata.
- Header-only rows excluded, including legacy bold-cell headers.
- Separate product tables retained without merging; no normalization or deduplication.
- Separate gallery entries are not extracted in this pass.
