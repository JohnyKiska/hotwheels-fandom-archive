# Hot Wheels Collectibles 1:43 Scale extraction QA

## Source
- Path: `Modern Special Series/100% Hot Wheels/Hot Wheels Collectibles 1_43 Scale _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `3d4675e8c30ed6c8e6cc94153ae1e734a45b82cb`
- Manifest SHA-256: `E8AAF5049F0C4D5BD30D1158A35595BFDCD58E4151576A4603FB4C41125CDB6D`
- Source size: 361,894 bytes
- HTML content length: 361,884 characters
- Fandom revision ID: 812244

## Extraction summary
- Product tables extracted: 3 (source table indices: 0, 1, 2)
- Product rows: 23
- Separate standard `wikia-gallery-item` gallery items: 0
- Embedded image references in product rows: 46
- Empty Photo/Image cells without an image element: 0
- Populated Toy # values: 23; distinct Toy # values: 23; repeated Toy # groups: 0
- Distinct casting-name labels: 19; repeated casting-name groups: 4

## Table details
### Table 0: 1999 [ ]
- Product rows: 10
- Source columns (6): `Toy #`, `Casting Name`, `Color`, `Notes`, `Photo Loose`, `Photo Boxed`
- Embedded image references: 20
- Empty Photo/Image cells without an image element: 0
### Table 1: 2000 [ ]
- Product rows: 11
- Source columns (7): `Toy #`, `Series`, `Casting Name`, `Color`, `Notes`, `Photo Loose`, `Photo Boxed`
- Embedded image references: 22
- Empty Photo/Image cells without an image element: 0
### Table 2: 2000 Ferrari [ ]
- Product rows: 2
- Source columns (6): `Toy #`, `Casting Name`, `Color`, `Notes`, `Photo Loose`, `Photo Boxed`
- Embedded image references: 4
- Empty Photo/Image cells without an image element: 0

## Repeated Toy # values
- None detected.

## Repeated casting-name labels
- `'32 Ford`: 2 rows, retained separately
- `1971 Plymouth GTX`: 2 rows, retained separately
- `456 GT`: 2 rows, retained separately
- `Studebaker Funny Car`: 2 rows, retained separately

## Notes
- Original table boundaries, source table indices, section headings, source row order, raw row HTML, raw cell HTML, source headers, decoded cell values, links, image filenames, image links, lazy-loaded image URLs, and per-cell image metadata are retained.
- Separate Gallery assets are individual CSV records, not merged into product rows.
- Navigation tables without product headers and data rows were excluded.
- No row merging, product inference, Toy # normalization, or casting identity resolution was performed.
