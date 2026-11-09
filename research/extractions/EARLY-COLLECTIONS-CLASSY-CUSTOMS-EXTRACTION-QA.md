# Classy Customs extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Early Collections/Classy Customs _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `e6abb91ef7ee6140ac65220a5aaef8b33a07f72a`
- Manifest file size: 343,179 bytes
- Manifest SHA-256: `07E1C1AF03D7D807AD4CD5BB1B0C00F2BC638F79F4BDCC3C1BAE80B9662CACF7`
- Fandom revision ID: 767675
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 12
- Source columns: 9
- Separate gallery entries: 2
- Combined CSV records: 14
- Distinct Toy # values: 12
- Distinct Collector # values: 12
- Toy # values: 2511, 6976, 6980, 2510, 9211, 6966, 6964, 2018, 9644, 2503, 9641, 2020
- Collector # values: 60, 6, 8, 55, 41, 3, 2, 47, 24, 7, 16, 13
- Loose-photo filenames: 12
- Carded-photo filenames: 12

## Preservation and interpretation
- Original table columns preserved: Toy #, Collector #, Vehicle Name, Color, Tampo, Wheel Type, Notes, Photo Loose, Photo Carded.
- No Year column exists in the source; no year was inferred.
- Loose/card images and the two separate gallery images (patch-card front/back references) are retained separately.
- Raw source cell text and image metadata are preserved. No rows merged or discarded.
- Toy # and Collector # remain distinct source identifiers.

## QA
- 12 source product rows exported; 2 gallery entries exported separately.
- Source order retained; empty cells preserved.

## Output
- `research/extractions/EARLY-COLLECTIONS-CLASSY-CUSTOMS.csv`
