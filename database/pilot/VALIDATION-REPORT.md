# Pro Racing 1:43 pilot seed validation

Date: 2026-11-10  
Status: STATIC VALIDATION PASSED; SQLite execution still pending

## Inputs checked

- Schema: `database/schema.sql`
- Seed: `database/pilot/pro-racing-1-43-seed.sql`
- Product source: `research/extractions/LARGER-SCALE-PRO-RACING-1-43-SCALE.csv`
- Gallery source shard: `research/galleries/GALLERY-EXTRACTION-08.csv`

## Static checks

| Check | Result |
|---|---:|
| Tables declared in schema | 11 |
| INSERT statements in seed | 155 |
| Import batches | 2 |
| Source documents | 2 |
| Source rows | 96 |
| Image metadata rows | 55 |
| INSERT targets exist in schema | PASS |
| INSERT column names exist in target tables | PASS |
| Foreign-key target tables exist | PASS |
| Every INSERT has a terminating semicolon | PASS |
| Canonical casting/variant/release/set rows inserted | 0 |
| Automatic image-to-entity relations inserted | 0 |

Source-row breakdown is 41 product-table rows and 55 Gallery evidence rows. The seed deliberately stages evidence and metadata only; it does not assert product identity from captions or filenames.

## Correction made during validation

The two import-batch statements were normalized to use standard single-quoted SQL string literals for the importer version, status and notes. The seed was then fetched again from `main` and rechecked. Its source-row and image-asset INSERT counts remain unchanged.

## What this validation does not prove

This was a structural/static inspection of the SQL text against the schema. It was **not** execution in a SQLite engine. Runtime constraint enforcement, successful transaction completion, and the expected post-load SELECT counts remain to be tested when a SQLite runtime is available.

The pilot remains **STAGED, NOT LOADED**. Source CSV files remain the system of record.
