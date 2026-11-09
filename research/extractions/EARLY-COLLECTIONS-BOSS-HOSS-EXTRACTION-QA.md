# Boss Hoss extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Early Collections/Boss Hoss _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `3a7cb7b9e5e4e65c0a9e6a0d671fc6422014119f`
- Manifest file size: 419,070 bytes
- Manifest SHA-256: `A84EF7E02BB4A05426369C3F09089B113C4DB3B01CFDCE2F1FD447DB7A5266B0`
- Fandom revision ID: 815490
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 2
- Original Versions: 23 data rows, 12 source columns.
- Retooled Versions: 10 data rows, 13 source columns.
- Product rows total: 33.
- Gallery items: 22.
- Export rows total: 55.
- Distinct Toy # values: 11.
- Year values: 1970, 1971, 2005, 2006, 2008, 2013, 2017, 2022.
- Repeated Toy # groups: 1.
  - Toy # 6499: 23 rows

## Important source structure
- Original Versions uses the source columns: Year, Series, Color, Sticker, Base Color / Type, Window Color, Interior Color, Wheel Type, Toy #, Country, Notes, Photo.
- Retooled Versions adds Col # and Tampo and has a different column order. Both original schemas are preserved verbatim in each row's Raw source headers and Raw source cells.
- The 23 Original Versions rows all carry Toy # 6499. They are retained as 23 distinct source variants, not collapsed into one record.
- Retooled Versions has separate later rows with their own Toy # values. These are not merged with the original rows.
- Gallery captions, image filenames, and alt text are retained separately from product-table records.
- No casting identity or release equivalence has been inferred.

## QA notes
- All source product rows and all detected gallery items were exported.
- Table and gallery source order is retained.
- Empty cells remain empty.
- No automatic merging by Toy #, model name, color, or year.
- This is a source extraction, not a claim that every row represents a unique casting.

## Output
- `research/extractions/EARLY-COLLECTIONS-BOSS-HOSS.csv`
