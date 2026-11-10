# Gallery extraction QA: DC Character Cars

- Source path: `Modern Special Series/Character Cars/DC Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Source Git blob SHA: `b4080ceff464506538f94188019519a674eb479f`
- MANIFEST.csv inventory size: 684688 bytes
- MANIFEST.csv SHA-256: `1CBB5A4B6C4F6F41DAFD1C2D9763E5C859B2644881CBD26D8F1044289AFAED0F`
- Fandom revision ID: 725098
- Gallery headings detected: 2 (Gallery [ ]; Batman & Rogue Gallery [ ])
- Gallery containers detected: 2
- Gallery items extracted: 4
- General HTML `<img>` elements observed: 366
- Output CSV: `research/galleries/MODERN-SPECIAL-SERIES-DC-CHARACTER-CARS-GALLERY.csv`
- Schema: 15 columns, matching the established Gallery extraction schema.
- Gallery container details: `gallery-0` (1 items; preceding heading: 2016 [ ]); `gallery-1` (3 items; preceding heading: Gallery [ ])
- Scope: dedicated Gallery extraction only. Other article/product/infobox images remain candidates for the separate Inline Image extraction stage.
- Integrity note: source blob SHA and manifest inventory metadata are recorded separately. Fetched text character length differs from the manifest byte-size field, so this pass does not assert byte-for-byte or SHA-256 verification.
- Result: 4 Gallery item(s) extracted. A zero-item result does not mean the source page contains no images.
