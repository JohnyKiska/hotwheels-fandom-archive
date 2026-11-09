# Gran Toros Extraction QA

- Source: `Early Special Series/Gran Toros _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `9f3a177f5e5f926c919cb8adb45acfc75dca05de`
- Source size (bytes): 375096
- Fandom revision ID: 814941
- Top-level HTML tables scanned: 2
- Product rows extracted: 29
- Embedded table image references: 29
- Links retained from product cells: 55
- Source manifest SHA-256: `6B637A41BED3A768100937DF85BF20EDE3E556408FA2823A3BDD9FE27AD12379`
- CSV: `research/extractions/EARLY-SPECIAL-SERIES-GRAN-TOROS.csv`

## Table-level review

| Table | Product rows | Images | Links | Headers |
|---:|---:|---:|---:|---|
| 1 | 25 | 25 | 50 | Number; Name; Color; Country; Photo |
| 2 | 4 | 4 | 5 | Number; Name; Car(s) included; includes; Photo |

## Extraction checks

- Rows retained in source order; table/row positions, nearest preceding section heading, headers, raw row HTML, cell HTML/text, links and image metadata preserved.
- Header-only rows excluded, including legacy bold-cell headers.
- Separate product tables retained without merging; no normalization or deduplication.
- Separate gallery entries are not extracted in this pass.
