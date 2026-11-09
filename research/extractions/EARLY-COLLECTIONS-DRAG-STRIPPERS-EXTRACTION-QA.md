# Drag Strippers extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Early Collections/Drag Strippers _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `4a562feebe3ee01403ae956cae9ba6757081f205`
- Manifest file size: 351,156 bytes
- Manifest SHA-256: `A752A325B728240B9F62AD5139638C51965E6CE8747EFC4D6593B5E7B21E9125`
- Fandom revision ID: 767718
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 17
- Source columns: 9
- Separate gallery entries: 2
- Combined CSV records: 19
- Distinct Toy # values: 15
- Distinct Collector # values: 15
- Distinct vehicle names: 15
- Repeated Toy # groups: [["2508",2],["9646",2]]
- Repeated Collector # groups: [["30",2],["34",2]]
- Loose-photo filenames: 17
- Carded-photo filenames: 17

## Preservation and interpretation
- Original table columns preserved: Toy #, Collector #, Vehicle Name, Color, Tampo, Wheel Type, Notes, Photo Loose, Photo Carded.
- Toy # and Collector # retained independently.
- Repeated identifiers and same-name variants remain separate; no deduplication.
- The final Vetty Funny row has a carded image entry named `Image Not Available.jpg`; this source value is preserved.
- Two gallery entries (mail-away patch-card image and card reverse) are stored separately.
- No Year column exists in this source table; no year was inferred.

## QA
- 17 source product rows exported, plus 2 gallery entries.
- Source order retained; empty cells preserved.

## Output
- `research/extractions/EARLY-COLLECTIONS-DRAG-STRIPPERS.csv`
