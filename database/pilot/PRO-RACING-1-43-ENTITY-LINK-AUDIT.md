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
| `pr143-assortment-b7022-3-pack` | 30, 31, 32 | 3 |
| `pr143-assortment-b6223-f2004-constructors-champions-2-pack` | 38, 39 | 2 |

Interpretation:
- World Champions 2-Pack rows 17-18: two distinct component candidates, not two pack entities.
- Constructors Champions 4 Pack rows 26-29: four distinct car candidates, one set-level candidate.
- Hot Wheels Racing B7022 rows 30-32: catalog item number, JAN, three contents, and retail display-box photographs cross-checked. The group is identified at commercial assortment level; source-row provenance and sample-to-individual-car links remain unverified.
- Hot Wheels Racing B6223 F2004 Constructors Champions 2-Pack rows 38-39: complementary #1/#2 source rows match the cataloged 1:43 Schumacher/Barrichello set, EAN 0027084044867, with documented Ferrari-shield package. This remains a strong candidate, not a source-proven package link.

## Review gates still open

1. Resolve 13 rows whose Variant candidates are on hold before promoting their Release candidates.
2. Verify whether named pack/release labels correspond to retail releases, prototypes, samples, or catalog-only references.
3. Retain B7022 and B6223 as staged candidate assortments until source-specific package provenance is established.
4. Keep Bahrain/Sakhir rows 35 and 41 linked only as a shared provisional Variant candidate; do not merge Release candidates. The known Hot Wheels B6222 Bahrain/Sakhir F2004 is 1:18, while B6206/B6207 are generic 1:43 F2004 #1/#2 references. No 1:43 Bahrain/Sakhir retail item is corroborated by current evidence.
5. Keep image-to-entity relations uncreated until individual physical-item evidence supports them.
6. For rows 35 and 41, inspect the distinct product-table photos `Ferrari_Bahrain_2004_Terry_Sample_(2).png` and `2004_Ferrari_Terry_Sample_(1).jpg`. The three separate Gallery views (items 26–28, group `PR143-G12`) support the Bahrain/Sakhir sample family but do not prove exact row-to-image or row-to-retail-item mapping.
