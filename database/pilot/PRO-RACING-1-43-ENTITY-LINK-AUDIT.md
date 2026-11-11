# Pro Racing 1:43 entity-link and staging audit

Status: read-only consistency audit of the staged candidate CSVs. No canonical entities or links were created.

## Referential checks

- Variant candidate rows: 41.
- Release candidate rows: 41.
- Unique source row IDs in both files: 41.
- Every release candidate points to the variant candidate for the same source row: PASS.
- Missing variant candidate mappings: 0.
- Duplicate source row IDs: 0.
- Canonical Release/Assortment flags remain `no` on every row.

## Dependency gate

A Release candidate cannot be considered ready for canonical promotion while its Variant candidate is held.

- `staged_candidate_only`: 28 rows.
- `blocked_pending_variant_review`: 13 rows.

The dependency status is informational and does not promote any record.

## Assortment membership audit

| Candidate group | Source rows | Count |
|---|---|---:|
| `pr143-assortment-world-champions-2-pack` | 17, 18 | 2 |
| `pr143-assortment-constructors-champions-4-pack` | 26, 27, 28, 29 | 4 |
| `pr143-assortment-unspecified-3-pack` | 30, 31, 32 | 3 |
| `pr143-assortment-f2004-2-pack` | 38, 39 | 2 |

Interpretation:
- World Champions 2-Pack rows 17-18: two distinct component candidates, not two pack entities.
- Constructors Champions 4 Pack rows 26-29: four distinct car candidates, one set-level candidate.
- Unspecified 3-Pack rows 30-32: membership grouping only; title and complete pack identity unresolved.
- F2004 2-Pack rows 38-39: membership grouping only; package identity and any additional context unresolved.

## Review gates still open

1. Resolve 13 rows whose Variant candidates are on hold before promoting their Release candidates.
2. Verify whether named pack/release labels correspond to retail releases, prototypes, samples, or catalog-only references.
3. Resolve the 3-Pack and F2004 2-Pack identities and full contents.
4. Keep Bahrain/Sakhir rows 35 and 41 linked only as a shared provisional Variant candidate; do not merge Release candidates.
5. Keep image-to-entity relations uncreated until individual physical-item evidence supports them.
