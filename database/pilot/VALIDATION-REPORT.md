# Pro Racing 1:43 pilot validation status

Date: 2026-11-11

## Source staging validation

The original schema and source seed were executed in SQLite using GitHub Actions. The successful run verified the 2 import batches, 2 source documents, 41 product source rows, 55 Gallery source rows, 55 image assets, foreign keys, integrity, idempotency, and absence of canonical entities/image relations. The machine-readable report from that run is `SQLITE-EXECUTION-REPORT.json`.

## Reconciliation evidence staging

A second idempotent seed, `pro-racing-1-43-reconciliation-seed.sql`, now adds 55 group-level evidence claims across 18 review groups. The validator has been extended to verify:

- 55 reconciliation evidence claims;
- 18 distinct review groups;
- 43 `cross_checked` claims and 12 `hypothesis` claims;
- every reconciliation claim is group-level;
- no canonical castings, variants, releases, or image relations are created;
- both source and reconciliation seeds remain idempotent;
- foreign-key and database integrity checks pass.

**Status:** updated SQLite execution is pending a manual run of `.github/workflows/validate-pro-racing-sqlite.yml`. Do not mark import batches validated or committed until that run passes and a separate approval step is completed.
