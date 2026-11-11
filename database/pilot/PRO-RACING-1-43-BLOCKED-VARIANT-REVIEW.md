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

The separate Gallery images 26–28 are already grouped under `PR143-G12` (“Bahrain / Sakhir Ferrari sample views”). Visual review records an F2004-branded presentation box, a red Ferrari F1 car in display packaging, and a red Ferrari under a clear cover with Sakhir/Bahrain-style presentation branding. Gallery item 28 carries the caption “2004 Sakhir / Bahrain Sample piece”. The user’s visual comparison of the two Fandom product-table photos additionally reports differences in packaging and visible dirt/weathering marks on the car body. This is useful row-level visual evidence that the pictured samples are not identical in presentation and/or condition. The dirt marks must not yet be treated as a confirmed factory tampo/deco variation: they could reflect sample handling, display condition, or a deliberate finish. The packaging difference strengthens the case for keeping the two source Release candidates separate. It does not, by itself, prove distinct castings or retail SKUs.

**Decision:** retain the shared provisional Variant-candidate group only as a family-level hypothesis; keep Release candidates 035 and 041 separate. Record the user-observed packaging and body-condition differences as visual comparison evidence, but do not infer a separate Variant from dirt marks without close inspection of the finish and base markings. Do not create canonical entities or image-to-entity links yet. Existing catalog research still finds B6222 as a 1:18 Bahrain/Sakhir item; no matching 1:43 retail SKU is confirmed.


## Bahrain/Sakhir weathering clue: intentional finish confirmed at 1:18, not yet at 1:43

A new catalog cross-check materially changes how the body marks should be treated. Hot Wheels B6222 is independently catalogued as a 1:18 Ferrari F2004 “SAKHIR/BAHRAIN 04/04/04” #1. Specialist sources explicitly describe it as weathered: airbrushed dust, used tyres, and Bahrain sand/air-filter details. Suruga-ya likewise states that the model has weathering applied. Sources:

- [Eurospec: B6222, 1:18 Sakhir/Bahrain](https://eurospecdiecast.com/product/hot-wheels-1-18-ferrari-f1-gp-f-2004-sakhir-bahrain-michael-schumacher-b6222/)
- [Schumacher Fan Club: B6222 “King of the Desert”, airbrush dust and used tyres](https://www.schumacher-fanclub.com/hot-wheels-diecast-model-cars/michael-schumacher/b6222-hot-wheels-michael-schumacher-king-of-the-desert.php)
- [House of Modelcars: B6222 “Dirty Version”, 1:18, EAN 0027084044850](https://www.houseofmodelcars.com/eng/product/ferrari/9146)
- [Suruga-ya: B6222, 1:18, weathering applied](https://www.suruga-ya.jp/kaitori/kaitori_detail/770306617)

This establishes that deliberate factory weathering is part of Hot Wheels’ documented Bahrain F2004 treatment at 1:18. It makes intentional weathering a credible hypothesis for the dirt marks reported on the two 1:43 Fandom sample photos. However, B6222 is a different scale and cannot be assigned to either 1:43 row. No 1:43 Bahrain/Sakhir SKU has been corroborated. The actual 1:43 source-table photos still need direct inspection; the weathering pattern must be compared for placement, density, and repeatability before treating it as a variant identifier.

**Updated interpretation:** keep packaging differences as direct evidence of distinct sample presentations. Treat the dirt pattern as a potentially intentional design fingerprint, not merely incidental dirt, but keep its status unverified at 1:43. If the same pattern recurs on another independently photographed sample or is explicitly tied to a 1:43 item code, it may help identify a distinct release/deco. Do not create a canonical Variant, Release, or image link yet.


## Independent 1:43 Bahrain F2004 weathering comparator (BBR)

A second, independent-scale clue has been found: BBR Models catalogues a Ferrari F2004 Bahrain GP 2004 #1 Michael Schumacher “Dirty Version” in 1:43 resin, limited to 300 pieces and described as an end-of-race dirty finish. This is not a Hot Wheels product and must not be confused with either Pro Racing source row. It is nevertheless useful evidence that the Bahrain F2004 was deliberately represented with race grime in the 1:43 collector-model market.

Sources:
- [Motorsport Maranello Store, BBR 1:43 Ferrari F2004 Bahrain Dirty Version](https://store.motorsportmaranello.com/shop/f1-bbr-models-1-43-ferrari-f2004-gp-bahrain-2004-1-m-schumacher-dirty-version/)
- [Motorsport Italia, same BBR listing](https://store.motorsportitalia.it/prodotto/modellino-f1-bbr-models-1-43-ferrari-f2004-gp-bahrain-2004-1-m-schumacher-dirty-version/)

Combined with Hot Wheels B6222 (1:18, factory weathering explicitly stated), this makes intentional weathering on the 1:43 Hot Wheels sample more plausible. It remains unconfirmed until the actual Hot Wheels sample photos can be inspected closely and compared for weathering placement/pattern, base markings, and packaging. Do not transfer the BBR SKU or any B6222 identity to rows 35/41.


## Independent 1:43 Bahrain F2004 weathering comparator (BBR)

BBR Models separately catalogues a Ferrari F2004 Bahrain GP 2004 #1 Michael Schumacher “Dirty Version” in 1:43 resin, limited to 300 pieces and described as an end-of-race dirty finish. The listing gives manufacturer code **BG263** and barcode **8011984012631**. This is not a Hot Wheels product and must not be confused with either Pro Racing source row. It is useful evidence that the Bahrain F2004 was deliberately represented with race grime in the 1:43 collector-model market.

Sources:
- [Motorsport Maranello Store, BBR 1:43 Ferrari F2004 Bahrain Dirty Version](https://store.motorsportmaranello.com/shop/f1-bbr-models-1-43-ferrari-f2004-gp-bahrain-2004-1-m-schumacher-dirty-version/)
- [Motorsport Italia, same BBR listing](https://store.motorsportitalia.it/prodotto/modellino-f1-bbr-models-1-43-ferrari-f2004-gp-bahrain-2004-1-m-schumacher-dirty-version/)

Combined with Hot Wheels B6222 (1:18, factory weathering explicitly stated), this makes intentional weathering on the 1:43 Hot Wheels sample more plausible. It remains unconfirmed until the actual Hot Wheels sample photos can be inspected closely and compared for weathering placement/pattern, base markings, and packaging. Do not transfer BBR code BG263 or Hot Wheels code B6222 to rows 35/41.
