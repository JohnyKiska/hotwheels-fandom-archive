# 100% Hot Wheels 40th Anniversary extraction QA

## Source
- Path: `Modern Special Series/100% Hot Wheels/100% Hot Wheels 40th Anniversary _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `ecf952b0e06c79c1f2a6b30feef3a9d25dd273f0`
- Manifest SHA-256: `421A637A37D12968DA905EDDE3776864F302279808826E306518A3B38E22E57C`
- Source size: 396,986 bytes
- HTML content length: 396,942 characters
- Fandom revision ID: 803409

## Extraction summary
- Product tables extracted: 10 (source table indices: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
- Product rows: 39
- Separate standard `wikia-gallery-item` gallery items: 0
- Embedded image references in product rows: 58
- Empty Photo cells without an image: 1
- Populated Toy # values: 20; distinct Toy # values: 20
- Distinct casting-name labels: 35
- Repeated casting-name labels: 4

## Table details
### Table 0: Single Cars
- Product rows: 20
- Source columns (5): `Toy #`, `Casting Name`, `Color`, `Photo Loose`, `Photo Carded`
- Embedded image references: 40
- Empty Photo cells without image: 0

### Table 1: Retro Racing 2-Car Set
- Product rows: 3
- Source columns (3): `Casting Name`, `Color`, `Photo`
- Embedded image references: 3
- Empty Photo cells without image: 0

### Table 2: Boulevard Burners 2-Car Set
- Product rows: 2
- Source columns (3): `Casting Name`, `Color`, `Photo`
- Embedded image references: 1
- Empty Photo cells without image: 1

### Table 3: Motown Metal 2-Car Set
- Product rows: 2
- Source columns (3): `Casting Name`, `Color`, `Photo`
- Embedded image references: 2
- Empty Photo cells without image: 0

### Table 4: Gilmore Special 2-Car Set
- Product rows: 2
- Source columns (3): `Casting Name`, `Color`, `Photo`
- Embedded image references: 2
- Empty Photo cells without image: 0

### Table 5: Volkswagen Flashback 2-Car Set
- Product rows: 2
- Source columns (3): `Casting Name`, `Color`, `Photo`
- Embedded image references: 2
- Empty Photo cells without image: 0

### Table 6: Drive-In 2-Car Set
- Product rows: 2
- Source columns (3): `Casting Name`, `Color`, `Photo`
- Embedded image references: 2
- Empty Photo cells without image: 0

### Table 7: Car Show 2-Car Set
- Product rows: 2
- Source columns (3): `Casting Name`, `Color`, `Photo`
- Embedded image references: 2
- Empty Photo cells without image: 0

### Table 8: Truck Show 2-Car Set
- Product rows: 2
- Source columns (3): `Casting Name`, `Color`, `Photo`
- Embedded image references: 2
- Empty Photo cells without image: 0

### Table 9: Mopar Muscle 2-Car Set
- Product rows: 2
- Source columns (3): `Casting Name`, `Color`, `Photo`
- Embedded image references: 2
- Empty Photo cells without image: 0

## Repeated casting-name labels
- `Volkswagen Truck`: 2 rows, retained separately
- `'69 Chevy Chevelle`: 2 rows, retained separately
- `'66 Pontiac GTO`: 2 rows, retained separately
- `'56 Ford F-100`: 2 rows, retained separately

## Notes
- The page contains separate single-car and named 2-car-set tables. Their source boundaries and headings are preserved.
- Navigation tables at source indices 10 and 11 were excluded.
- Raw row HTML, raw cell HTML, decoded cell values, source headers, model/file links, image filenames, image links, lazy-loaded image URLs, and per-cell image metadata are retained.
- No row merging, product inference, or Toy # normalization was performed.
