# Evil Weevil extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Early Collections/Evil Weevil _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `1f58c9c929ca5529421d7e689e5fadcf1ce487ec`
- Manifest file size: 397,979 bytes
- Manifest SHA-256: `A2EDF78C5FD36806E25888CC4B2FF5E4C509AF8D4C51F5F5E6051BC7A4F54C91`
- Fandom revision ID: 772324
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 2
- Original Versions: 8 rows, 12 columns.
- Retooled Versions: 5 rows, 12 columns.
- Product rows total: 13
- Separate gallery entries: 24
- Combined CSV records: 37
- Year values: 1971, 2004, 2005, 2006, 2008, 2009
- Distinct Toy # values: 6
- Repeated Toy # groups: [["6471",8]]
- Distinct Series labels: 6

## Preservation and interpretation
- Original Versions and Retooled Versions retain separate source table identities and original headers.
- Original Versions uses a `Stickers` column; Retooled Versions uses `Tampo`. These have not been conflated.
- All raw cell text and image metadata are retained. Gallery entries remain separate from product rows.
- Repeated Toy # values are preserved as separate rows. No deduplication or identity resolution was performed.
- Years are source table values, not inferred.

## QA
- 13 product rows exported from 2 tables; 24 gallery entries exported separately.
- Source order retained within each table and gallery.
- Empty cells preserved.

## Output
- `research/extractions/EARLY-COLLECTIONS-EVIL-WEEVIL.csv`
