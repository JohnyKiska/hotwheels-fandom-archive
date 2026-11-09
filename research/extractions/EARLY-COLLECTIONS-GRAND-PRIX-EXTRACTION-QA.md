# Grand Prix extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`, branch `main`
- Source: `Early Collections/Grand Prix _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `d23ef8f6f24209353e1c8e9af4c8861fd5d7c25a`
- Manifest size: 326,614 bytes
- Manifest SHA-256: `undefined`
- Fandom revision ID: 787981
- Extraction date: 2026-11-09

## Extraction results
- HTML tables: 1
- The Cars image-layout table: 8 rows, 3 columns in the first six rows and 2 columns in the last two rows.
- Vehicle caption/product references: 11
- Associated source image references: 11
- Separate Gallery entries: 1
- Gallery reference exported: 35 Years of Speed Randy Leffingwell (60).JPG
- Product labels retain source spelling and year text exactly as displayed. No Toy #, release year, or package data was inferred.

## Vehicle captions in source order
1. Brabham Repco F1 (1969) | image: Brabham Repco F! Purp.jpg
2. Chapparral 2G (1969) | image: Chapparal.jpg
3. Indy Eagle (1969) | image: Indyeagle.jpg
4. Ferrari 312P (1970) | image: Brabham Repco F! Purp.jpg
5. Ford J-Car (1968) | image: Chapparal.jpg
6. Ford Mark IV (1969) | image: Indyeagle.jpg
7. Lola GT70 (1969) | image: Brabham Repco F! Purp.jpg
8. Lotus Turbine (1969) | image: Chapparal.jpg
9. McLaren M6A (1969) | image: Indyeagle.jpg
10. Porsche 917 (1970) | image: Brabham Repco F! Purp.jpg
11. Shelby Turbine (1969) | image: Chapparal.jpg

## Preservation notes
- The page's only HTML table is a visual image-and-caption grid, not a conventional product-data table.
- Each vehicle caption is exported as a separate `product` source record with its paired image filename, alt text, and image URL in dedicated source-image columns.
- The single Gallery item is retained as a separate `gallery_reference` record. Its caption, filename, alt text and file-page link are preserved.
- No Toy #, collector number, casting identity, package configuration, or release chronology was invented.
- No deduplication or entity resolution was performed.

## QA
- 11 product-caption records and 1 gallery reference record exported (12 CSV records total).
- All 11 grid image filenames retained.
- Source order retained. Source page and Git provenance are recorded above.

## Output
- `research/extractions/EARLY-COLLECTIONS-GRAND-PRIX.csv`
