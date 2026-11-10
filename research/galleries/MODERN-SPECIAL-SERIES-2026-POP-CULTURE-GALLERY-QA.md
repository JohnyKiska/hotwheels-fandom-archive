# Gallery extraction QA: 2026 Pop Culture

- Source path: `Modern Special Series/Pop Culture/2026 Pop Culture _ Hot Wheels Wiki _ Fandom.html`
- Source Git blob SHA: `4d3f7706cf44b26ac1491e7112446560dbc20c19`
- MANIFEST.csv inventory size: 388929 bytes
- MANIFEST.csv SHA-256: `852DE68E243B30577ADF35853032DE2C01F2E49CEEC3CD861A4DE4CE5B716079`
- Fandom revision ID: 816093
- Gallery headings detected: 1
- Dedicated `wikia-gallery` containers: 1
- `wikia-gallery-item` markers: 5
- Gallery items extracted: 5
- General HTML `<img>` elements observed: 74
- Output CSV: `research/galleries/MODERN-SPECIAL-SERIES-2026-POP-CULTURE-GALLERY.csv`
- Schema: 15 columns, matching the consolidated Gallery extraction schema.
- Duplicate key check: passed (`source_file + gallery_id + gallery_item_index`).
- Consolidation note: five pre-existing records used synthetic IDs (`gallery-1` through `gallery-5`) and incorrect section indices; replaced with source-accurate records using actual Gallery ID `gallery-0` and section index 1.
- Raw item markup retained for all five records.
- Result: five dedicated Gallery items. General article/product images remain outside this extraction.
