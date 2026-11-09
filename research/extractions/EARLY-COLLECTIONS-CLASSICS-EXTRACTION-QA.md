# Classics extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Early Collections/Classics _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `81cdb2bcc7ce2505b2ce3b11f2a533475401e8a7`
- Manifest file size: 361,417 bytes
- Manifest SHA-256: `5507F2B9D4E6443ABF7F36D2E63F7EA0FD23D5FEC50A3CD899B5324848867084`
- Fandom revision ID: 757207
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 25
- Source columns: 9
- Unique model names: 14
- Distinct Toy # values: 17
- Year values: 1987, 1988, 1989
- Rows with loose-photo filenames: 25
- Rows with carded-photo filenames: 25
- Gallery section: none detected as a separate Fandom gallery.
- Repeated Toy # groups: 8
  - 1473: 2 rows
  - 1538: 2 rows
  - 2526: 2 rows
  - 4741: 2 rows
  - 5142: 2 rows
  - 7672: 2 rows
  - 7673: 2 rows
  - 9638: 2 rows

## Preservation and interpretation
- The page contains one product table with 25 data rows.
- Source columns are preserved in their original order: Toy #, Model Name, Color, Year, Wheel Type, Country, Notes, Photo Loose, Photo Carded.
- Loose and carded photo filenames and alt labels are stored separately.
- All source cell text and image metadata are retained in Raw source cells.
- Repeated Toy # values are preserved as separate rows. They may represent distinct colors, variants, or production details; no identity resolution or merging was attempted.
- The page is treated as a source page named Classics, not proof of a single canonical release group or a casting-level entity.

## QA
- Export row count matches source table data rows: 25.
- Source order retained.
- Empty cells preserved.
- No rows discarded or merged.

## Output
- `research/extractions/EARLY-COLLECTIONS-CLASSICS.csv`
