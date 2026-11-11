# Pro Racing 1:43 pilot staging report

Date: 2026-11-10  
Status: SOURCE SEED EXECUTED IN TEMPORARY SQLITE VALIDATION; RECONCILIATION SEED ADDED, UPDATED VALIDATION PENDING

## Source inputs

| Dataset | Rows staged | Source |
|---|---:|---|
| Product table | 41 | `research/extractions/LARGER-SCALE-PRO-RACING-1-43-SCALE.csv` |
| Gallery evidence | 55 | `research/galleries/GALLERY-EXTRACTION-08.csv`, filtered to the Pro Racing 1:43 source page |

Source blob fingerprints used by the seed:
- Product CSV: `2b15492feb9c2bd725415bc1e811bc3752522cbd`
- Gallery shard: `fedfbc041f12294039fda313bf341517f9b57cfb`
- Gallery source page revision: `815866`

## Output

The source SQL seed in this directory inserts:
- 2 staged import batches;
- 2 source-document records;
- 41 source-preserving product-table rows;
- 55 source-preserving Gallery rows;
- 55 image metadata records.

All raw product cell JSON and Gallery row fields are retained. Gallery metadata includes filename, image key, URL, file-page URL, alt, title, and caption HTML.

The reconciliation seed adds 55 idempotent group-level `evidence_claim` records across 18 reviewed groups. It records the match disposition, candidate source rows, evidence basis, and unresolved questions. It does not create canonical entities or image relations.

## What is deliberately not done

- No casting, variant, release, or assortment identities are created yet.
- No Gallery image is automatically linked to a product.
- No claim is made that image binaries have been downloaded or visually inspected.
- `Image Not Available` placeholders are retained as source values, not treated as real images.
- Prototype, package, set, sample, and advertising imagery remain evidence until a reviewer resolves the subject.

## How to use

1. Create an empty SQLite database.
2. Apply `database/schema.sql`.
3. Apply `database/pilot/pro-racing-1-43-seed.sql`.
4. Apply `database/pilot/pro-racing-1-43-reconciliation-seed.sql`.
5. Check the counts:
   - `SELECT COUNT(*) FROM source_row WHERE source_document_id='doc-pr143-products';` → 41
   - `SELECT COUNT(*) FROM source_row WHERE source_document_id='doc-pr143-gallery';` → 55
   - `SELECT COUNT(*) FROM image_asset WHERE source_document_id='doc-pr143-gallery';` → 55
   - `SELECT COUNT(*) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition';` → 55
   - `SELECT COUNT(DISTINCT subject_id) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition';` → 18

The source-seed SQLite execution passed in the temporary validation workflow. The updated workflow now also validates the reconciliation seed; its new run is pending. Import batches deliberately remain `staged`.
