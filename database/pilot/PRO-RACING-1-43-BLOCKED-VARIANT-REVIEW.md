# Pro Racing 1:43: blocked Variant review queue

**Scope:** the 13 product rows currently marked `hold` in `PRO-RACING-1-43-VARIANT-CANDIDATES.csv`.

## Audit result

- 13 held rows mapped one-to-one to the original product source rows.
- No evidence in the source CSV justifies changing any of the 13 casting labels.
- The hold reasons are not all casting problems. They comprise possible second-version claims, missing variant attributes, prototype/sample provenance, assortment-only context, a Bahrain/Sakhir identity question, and a year/package anomaly.
- The source photo column contains asset names or placeholders, not automatically verified visual evidence. Named assets must be inspected before they can support a variant decision.
- No canonical Variant was created and no source value was overwritten.

## Priority order

1. **Rows 3 and 6:** source notes explicitly say “Might be a 2nd version”. The missing information is what the alleged second version is, not proof that the casting label is wrong.
2. **Rows 35 and 41:** compare the Bahrain package clue and Sakhir/Bahrain sample reference. Keep separate Release candidates until item-level evidence establishes their relationship. Row 41 is not in the 13-row hold set, but is the essential comparison row.
3. **Rows 31 and 32:** the commercial set is now identified as Hot Wheels Racing B7022 (JAN 0027084052251). Its three contents and original black/red display box are supported by a catalog record and actual package photographs. The remaining gap is whether Terry Choy's source rows depict these exact retail cars/box, and whether any sample image can be linked to an individual car. Do not infer that link from assortment membership alone.
4. **Rows 9, 12, 13, 24 and 33:** inspect named website/sample assets. Treat prototype/sample provenance as provenance, not as a Variant attribute.
5. **Rows 10 and 19:** obtain independent physical/catalog evidence; the source provides only casting label and year.
6. **Row 36:** resolve the “Represents 1994” book-package note against the source year 2004. Preserve both as separate source facts until the nature of each field is established.

## Data handling rules

- Do not promote a held row to a canonical Variant based only on a casting name or year.
- Do not infer livery, race number, color, or packaging from an asset filename.
- Do not merge rows 35 and 41 into one Release because they share a Bahrain/Sakhir clue.
- Do not interpret a sample/prototype label as proof of a retail release.
- Retain source values verbatim; add normalized interpretations only as separately evidenced claims.

The companion CSV records one actionable evidence request per held row. B7022 is resolved at commercial assortment/package level, but rows 31–32 remain held at individual Variant/source-item level. This is a review queue, not a correction pass.


## Bahrain / Sakhir source-photo comparison (rows 35 and 41)

Direct inspection of the archived page HTML establishes that the two product-table rows point to **different source-photo files**:

- Row 35, “Bahrain 2004 package”: `Ferrari_Bahrain_2004_Terry_Sample_(2).png` ([source image](https://static.wikia.nocookie.net/hotwheels/images/e/e6/Ferrari_Bahrain_2004_Terry_Sample_%282%29.png/revision/latest?cb=20251009122856)).
- Row 41, “Sakhir / Bahrain”: `2004_Ferrari_Terry_Sample_(1).jpg` ([source image](https://static.wikia.nocookie.net/hotwheels/images/c/c7/2004_Ferrari_Terry_Sample_%281%29.jpg/revision/latest?cb=20251015124518)).

These are product-table image assets, not the three Gallery images already downloaded and reviewed. They therefore remain an explicit visual-inspection task.

The separate Gallery images 26–28 are already grouped under `PR143-G12` (“Bahrain / Sakhir Ferrari sample views”). Visual review records an F2004-branded presentation box, a red Ferrari F1 car in display packaging, and a red Ferrari under a clear cover with Sakhir/Bahrain-style presentation branding. Gallery item 28 carries the caption “2004 Sakhir / Bahrain Sample piece”. This supports a shared **sample-family** interpretation, but it does not establish which product row corresponds to which Gallery view or prove that the two product rows represent the same exact physical sample/release.

**Decision:** retain the shared provisional Variant-candidate group, keep Release candidates 035 and 041 separate, and do not create canonical entities or image-to-entity links. The direct product-table images must be retrieved and inspected before reconsidering the hold. Existing catalog research still finds B6222 as a 1:18 Bahrain/Sakhir item; no matching 1:43 retail SKU is confirmed.
