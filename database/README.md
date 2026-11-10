# HW Catalog database and visual layer

Status: architecture proposal / implementation foundation  
Date: 2026-11-10

## Current state

The repository currently stores the working catalog as source-preserving CSV extractions and research artifacts. It does not currently contain a live database service or a separate frontend application.

Important existing inputs:
- `research/extractions/*.csv`: product-table extractions, with source table/section context and raw source-cell metadata.
- `research/galleries/GALLERY-EXTRACTION-01.csv` through the numbered shards: Gallery image evidence.
- `research/galleries/GALLERY-SCAN.csv`: page-level scan inventory and source fingerprints.
- `MANIFEST.csv`: archived source-file inventory and SHA-256 values.
- `research/CSV-AUDIT-MANIFEST.csv`: structural CSV QA results.
- `research/DATA-MODEL-VALIDATION.md`: ongoing validation of entity boundaries and source semantics.

The consolidated `research/galleries/GALLERY-EXTRACTION.csv` is present in the repository, but the GitHub contents endpoint did not return its text body during this inspection. The numbered shards are readable and must be treated as the inspectable import source until the consolidated file is verified by a reproducible local parser.

## Non-negotiable data rules

1. Never overwrite or destructively normalize the source CSVs.
2. Import raw source rows and source fingerprints before creating canonical records.
3. Keep Casting, Variant, Release, and Assortment/Set separate.
4. Treat Toy #, Series position, racing number, team number, and item number as different typed concepts.
5. Keep source assertions separate from visually verified facts.
6. A Gallery item is an image/evidence record, not automatically a product photograph or product identity.
7. Preserve image filename, file-page URL, image URL, alt, title, caption HTML, source page, Fandom revision, and source blob/hash where available.
8. Never auto-link an image to a product solely because filenames or captions look similar. Store a proposed link with its basis and confidence for review.

## Proposed ingestion pipeline

1. **Inventory**: enumerate every CSV and read its header, encoding, row count, source scope, and audit status.
2. **Stage**: load each original row into a source-preserving staging table. Keep raw headers/cells/HTML and row order.
3. **Validate**: compare import counts and keys against CSV-AUDIT-MANIFEST, GALLERY-SCAN, and Gallery shard totals.
4. **Resolve**: generate candidate Casting/Variant/Release/Assortment records without deleting source rows.
5. **Evidence**: import image metadata independently. Download/store image binaries only when permitted and when stable source URLs/checksums can be recorded.
6. **Link review**: create explicit image-to-entity relations with confidence, rationale, and review status.
7. **Publish**: expose only approved canonical records to the public visual catalog; retain probable/unverified evidence in the review interface.

## Initial relational entities

- `source_document`, `source_row`, `import_batch`: immutable provenance and repeatable imports.
- `casting`: base casting/mold identity.
- `variant`: visual/configuration variant of a casting.
- `release`: specific issue/release with year, scale, Toy #, country, packaging, and assortment context.
- `assortment`, `assortment_component`: multipacks and set membership.
- `image_asset`: image metadata and source references.
- `image_relation`: reviewed relation between an image and one catalog entity.
- `evidence_claim`: atomic claims with source and verification status.

A SQLite reference schema is provided in `database/schema.sql`. It is a portable starting point, not a claim that a production database has already been provisioned. It can be migrated to PostgreSQL when a hosted backend is selected.

## Visual catalog

The visual layer should read from the canonical database/API, never directly from research CSV files.

### Public catalog
- Search and filters: casting, year, series/assortment, scale, Toy #, country.
- Casting page: known variants and related releases.
- Release card: characteristics, packaging, identifiers, and source-backed facts.
- Image gallery: full-size image, available views, captions, source page, and evidence type.
- Provenance panel: source, revision/checksum, verification status, and confidence.

### Review workspace
- Queue of unassigned Gallery images.
- Side-by-side image and candidate release/casting.
- Accept, reject, or defer a proposed relation.
- Show the exact evidence used for each proposed match.
- Keep source caption and reviewer conclusion in separate fields.

## Safe first pilot

Start with one bounded, well-audited dataset rather than bulk-importing the entire archive:
- Pilot source: Larger Scale / Pro Racing 1:43 product table.
- Image evidence: its 55 Gallery items plus its inline image evidence audit.
- Reconciliation: existing Pro Racing Gallery classification and item-level reconciliation notes.
- Import raw rows first, then resolve only high-confidence links; leave ambiguous sample/prototype/set imagery unassigned or probable.

The pilot is deliberately narrow and can test image handling, provenance, duplicate prevention, and the review UI before the remaining catalog is loaded.

## Not yet decided

A live database host, authentication, image storage/CDN, frontend framework, and deployment target have not been configured in this repository. Do not silently select paid infrastructure or expose a public write endpoint. The next implementation decision is the deployment target; the relational model and ingestion rules are designed to remain portable.
