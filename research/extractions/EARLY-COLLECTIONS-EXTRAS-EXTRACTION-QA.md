# Extras extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`, branch `main`
- Source: `Early Collections/Extras _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `e2a591a06e8ae39a455dc264e8cb8c6543c6536b`
- Manifest size: 332,471 bytes
- Manifest SHA-256: `D348DC5A136C715B5C5DE7DE3289ECDCAE3DEEE91DE49523B4FF8005F4F65A66`
- Fandom revision ID: 765024
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 9
- Source columns: 11
- Distinct model names: 7
- Distinct Toy # values: 7
- Repeated Toy # groups: [["4342",2],["5905",2]]
- Year values: 1983, 1984
- Loose photo references: 9
- Carded photo references: 9
- Gallery sections: none detected

## Preservation notes
- All nine source rows are retained in source order.
- Original table fields, including `Notes / Variations` and `Extra`, remain distinct.
- Loose and carded image filenames, alt text and file links are captured separately.
- Repeated Toy # values remain separate records; no deduplication or identity resolution was performed.
- No years or missing product attributes were inferred.

## QA
- 9 product records exported from the sole product table.
- 9 loose and 9 carded photo references captured.
- Empty cells retained.

## Output
- `research/extractions/EARLY-COLLECTIONS-EXTRAS.csv`
