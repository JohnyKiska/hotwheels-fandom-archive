# Gallery extraction QA: 2024 Pop Culture

- Source path: `Modern Special Series/Pop Culture/2024 Pop Culture _ Hot Wheels Wiki _ Fandom.html`
- Source Git blob SHA: `d7ba5432cd34f14aaffe1d3b7eaca20a84ee9c4c`
- MANIFEST.csv inventory size: 382411 bytes
- MANIFEST.csv SHA-256: `15D0CD4F5B2FBBC3DE2617D795612B6E57403ADF5C30EB5959ACC0BCA12FF2EE`
- Fandom revision ID: 795063
- Gallery headings detected: 1
- Dedicated `wikia-gallery` containers: 1
- `wikia-gallery-item` markers: 4
- Gallery items extracted: 4
- General HTML `<img>` elements observed: 70
- Output CSV: `research/galleries/MODERN-SPECIAL-SERIES-2024-POP-CULTURE-GALLERY.csv`
- Schema: 15 columns, matching the consolidated Gallery extraction schema.
- Duplicate key check: passed (`source_file + gallery_id + gallery_item_index`).
- Consolidation note: four pre-existing records for this source used synthetic IDs (`gallery-1` through `gallery-4`); these duplicate records were replaced by the four source-accurate records using the actual Gallery ID (`gallery-0`).
- Raw item markup retained for all four records.
- Result: four dedicated Gallery items. General article/product images remain outside this extraction.
