# Flippers Extraction QA

- Source: `Early Special Series/Flippers _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `6b55836c7505ffe72d93bd0305004857668ef827`
- Source manifest SHA-256: `9C4722F54F9FEAB3618698F8ACD8A7E5D1AABA7A879664AD4DE6FCE18DE56428`
- Source size (bytes): 467036
- Fandom revision ID: 796617
- Top-level HTML tables scanned: 4
- Product rows extracted: 37
- Embedded table image references: 142
- Links retained from product cells: 216
- CSV: `research/extractions/EARLY-SPECIAL-SERIES-FLIPPERS.csv`

## Table-level review

- Table 1: 32 data rows; headers: Toy #, Name, Year, Country, Notes, Photo, Photo, Photo
- Table 2: 1 data rows; headers: Toy #, Name, Year, Country, Notes, Photo
- Table 3: 3 data rows; headers: Toy #, Name, Year, Country, Notes, Photo, Photo, Photo, Ad Photo
- Table 4: 1 data rows; headers: Toy #, Name, Year, Country, Notes, Photo

## Extraction checks

- Rows retained in source order; table/row positions, nearest preceding section heading, headers, raw row HTML, cell HTML/text, links and image metadata preserved.
- Header-only rows excluded. No-header tables retained for later semantic review.
- Separate gallery entries are not extracted in this pass.
- Source-preserving extraction only; no normalization or deduplication.
