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


## External cross-check: Ferrari F2003-GA sample (row 33)

The row's source label is **Ferrari F2003-GA**, source year 2003, with named source photo **2003 Ferrari F1 Sample Terry (2)**. Independent catalogs confirm a standard Hot Wheels 1:43 Ferrari F2003-GA release exists as **B1018**:

- [Die Carz: Ferrari F2003-GA, B1018](https://diecarz.com/cars/hotwheels/ferrari-f2003-ga-168398) — Hot Wheels Racing, 2003, 1:43, toy code B1018.
- [Suruga-ya: B1018](https://www.suruga-ya.jp/kaitori/kaitori_detail/770000521) — Mattel, 1:43, Ferrari F2003-GA Shell #1, Michael Schumacher; JAN 0027084009231.
- [Yuui's F1 Scale Models: B1018](https://www.yuui.nl/en/collections/menu/products/2003-ferrari-f2003-ga-michael-schumacher) — Hot Wheels, 1:43, catalog number HWB1018, Michael Schumacher #1.
- [Hobby Search: B1018](https://www.1999.co.jp/10102602) — Mattel, 1/43, code B1018.

This establishes a plausible retail comparator for the same casting/year, but **does not prove that Terry Choy's sample is B1018**. The source photo itself has not been visually compared with B1018's tampo, race number, base, display plinth, or packaging. Keep row 33 on hold; do not promote B1018 to its exact release identity or attach a candidate-specific image relation yet.

## External cross-check: Ferrari 412 T1 “book package” (row 36)

The source row records casting label **Ferrari 412 T1**, source-table year **2004**, and note verbatim: “Represents 1994, in a Book pacakage”. External catalogs confirm at least two different Hot Wheels 1:43 Ferrari 412 T1-family products:

- [Armand Modelcars: T6284](https://www.armand-modelcars.nl/nld/product/ferrari/1848) — Hot Wheels Elite, 1:43, Ferrari 412 T1, Jean Alesi #27, Great Britain GP 1994, EAN 027084923049.
- [F1 Scale Models stock list](https://www.f1scalemodels.com/F1_Stocklist.pdf) — lists Ferrari 412 T1, 1994, Jean Alesi #27 Great Britain GP, Hot Wheels, code T6284.
- [ToysHouse: N5583](https://toyshouse.it/en/products/hot-wheels-n5583-ferrari-412-t1-berger-1994-vince-gp-germany) — Hot Wheels Elite, 1:43, Ferrari 412 T1, Gerhard Berger #28, German GP winner 1994, code N5583, limited edition 10,000.
- [eBay: N5583](https://www.ebay.com/itm/178548319139) — listing with photographs of the model and its black Hot Wheels Elite packaging.

These records establish plausible 1994 retail models and distinct driver/race configurations, but none documents a **book-shaped package** or connects either SKU to the Terry Choy source row. The “book package” may refer to a special presentation format, but no supporting package evidence was found in this search. Row 36 therefore remains held: retain source year 2004 and the 1994/package note as separate source facts; do not choose T6284 or N5583, and do not infer a release year or package type.

**Disposition for rows 33 and 36:** external retail comparators found; exact source-sample identity and package evidence remain unverified. No canonical Variant or Release created.


## Row 36: “book package” terminology check

A targeted search for a Hot Wheels Ferrari 412 T1 1:43 book-shaped package found no catalog or sale record tying that packaging to either known Hot Wheels retail 412 T1 release:

- **T6284**: Jean Alesi #27, Great Britain GP 1994, Hot Wheels Elite, 1:43, limited 5,000. [Armand Modelcars](https://www.armand-modelcars.nl/nld/product/ferrari/1848); [F1 Scale Models stock list](https://f1scalemodels.com/F1_Stocklist.pdf).
- **N5583**: Gerhard Berger #28, German GP winner 1994, Hot Wheels Elite, 1:43, limited 10,000. [F1 Scale Models stock list](https://f1scalemodels.com/F1_Stocklist.pdf); [eBay listing with model and black/red Hot Wheels Elite box photos](https://www.ebay.com/itm/178548319139).

A book-shaped Hot Wheels Racing presentation case is independently documented for a **different car**, Ferrari 312 T2 (Niki Lauda, 1977 German GP), in a special “La Storia” presentation. The listing describes a metal book-shaped display case and illustrated booklet; it states 1:43 and 2004 on the packaging. [Catawiki, Hot Wheels Racing La Storia Ferrari 312 T2](https://www.catawiki.com/en/l/105807162-hot-wheels-1-43-model-race-car-hot-wheels-racing-1-43-cofanetto-ferrari-312-t2-niki-lauda-german-gp-1977-come-nuovo). This proves that Hot Wheels used a book-shaped presentation format, but it does **not** identify the row 36 Ferrari 412 T1 as a La Storia product. Search results also show IXO-branded La Storia Ferrari 412 T1B models, which are a different manufacturer and must not be conflated with Mattel Hot Wheels.

The archived product-table extraction for row 36 has Photo = Image Not Available and no image URL in its structured cell data. Therefore the source page currently supplies no photograph with which to visually inspect the alleged book package.

**Updated disposition:** “book package” is a credible description of a presentation format used in the Hot Wheels Racing 1:43 ecosystem, but the specific Ferrari 412 T1 / row 36 association remains unverified. Do not assign T6284, N5583, or a La Storia identity. Preserve source year 2004 and “Represents 1994, in a Book pacakage” verbatim as separate source facts. A physical photograph, package label, or Mattel item code is required to proceed.

## Row 33: Gallery cross-check for the Terry Choy Ferrari sample

The product-table row identifies the casting as **Ferrari F2003-GA**, year 2003, and names a source photo **2003 Ferrari F1 Sample Terry (2)**. The extracted row has no image URL for that Photo field, and the archived pilot asset directory contains no (2) image.

The same page's Gallery extraction contains two adjacent images:
- Gallery item 20, **2003 Ferrari F1 Sample Terry (1).jpg**, captioned “2003 Ferrari Sample (Terry Choy collection)”. Its prior visual review records a close view of a red Ferrari Formula 1 car and a package label referencing Michael Schumacher.
- Gallery item 21, **2003 Ferrari F1 Sample Terry (3).jpg**, captioned “Back”. Its prior visual review records a Ferrari Formula 1 car on a sample display box, with Ferrari shield and red livery visible; the exact F2003-GA casting was not independently legible.

These two Gallery assets support a **2003 Ferrari sample group** and explain why the product-table photo stem is relevant. They do not substitute for the missing (2) source image, and do not establish the row's tampo, race number, base, plinth, packaging, or SKU.

The adjacent product-table row 34 is separately labelled **Ferrari F2003-GA**, with note **F1 World Champions** and a different source photo, **Ferrari 2003 World Champions Terry Sample (1)**. The existing Gallery review treats that material as a distinct World Champions presentation/sample context. Do not merge row 33 into row 34 or assume both are the same deco/release.

Retail comparator check remains unchanged: Mattel's product page identifies B1018 as a 1:43 Ferrari F1 model released in 2003; collector/catalog sources identify it as Ferrari F2003-GA, Michael Schumacher #1, Shell livery, JAN 0027084009231. This is a valid comparator for the casting/year, **not proof that Terry Choy's row 33 sample is B1018**. The B1018 comparison still lacks the missing (2) image and sample-specific base/package evidence.

**Disposition:** keep row 33 as hold in the Variant candidates. Keep Gallery items 20–21 as reviewed group-level/casting-candidate evidence only. No canonical Variant, Release, SKU assignment, or row-specific image relation is authorized by the current evidence.

## Rows 33–34: B1018 retail comparator and World Champions distinction

A further source check sharpens the standard retail comparator, but still does not identify either Terry Choy sample as B1018:

- Mattel's official product support record lists **Hot Wheels F1 1:43 Race Ferrari**, Product # **B1018**, released **2003**.
- Suruga-ya identifies B1018 as **Ferrari F2003-GA Shell #1**, red, Michael Schumacher, with Shell logos, a black named base, and a clear display case; JAN **0027084009231**. Its page separately displays a 2007-10-31 release-date field, which conflicts with Mattel's official 2003 release field. Retain Mattel's product-year value for the release-year comparator and treat Suruga-ya's date as a catalog-field discrepancy, not proof of a second B1018 issue.
- Diecast.com.ua independently labels B1018 as Ferrari F2003-GA #1, Scuderia Ferrari Marlboro, World Champion Formula 1 2003, Michael Schumacher. This is useful as a retail-deco reference, but it does not show that the Terry Choy sample has the same livery or SKU.

The wording **F1 World Champions** in product-table row 34 is therefore not enough to identify B1018. It may describe a distinct sample/deco or presentation context. The page's Gallery has a separate cluster of Ferrari 2003 World Champions sample images, including item 29 captioned as figures in the sample car and items 30–31 showing additional presentation/package views. Those images were already reviewed as display/sample context; they do not independently prove that row 34 is B1018, nor that it is the same object as row 33's “2003 Ferrari F1 Sample Terry (2)”.

**Disposition unchanged:** row 33 remains hold; row 34 remains a separate candidate_variant. B1018 stays a retail comparator only. No exact SKU, release identity, or image-to-row canonical relation is assigned without the missing row-33 photo and a direct visual comparison of row 34's sample car/deco/base/package.


## B7022 package photo cross-check (rows 30–32)

The current B7022 evidence was rechecked against an actual six-photo eBay listing and Suruga-ya catalog record:

- Suruga-ya identifies Mattel B7022, JAN `0027084052251`, scale 1:43, and the three contents: Ferrari F1-2000 #3 Malaysian GP (Shell), Ferrari F2001 #1 Belgian GP at Spa (Shell), and Ferrari F2002 #1 Canadian GP at Montreal (Vodafone/Shell-era livery). https://www.suruga-ya.jp/kaitori/kaitori_detail/770004005
- The eBay listing photographs show the black/red Hot Wheels Racing presentation box with all three cars together. Close-up photographs show the printed GP labels and race numbers on the display base; the #1 F2001 Belgian GP and #1 F2002 Canadian GP details are visually legible. https://www.ebay.com/itm/204701681876
- This is strong confirmation of the commercial B7022 assortment and its component specifications. It does **not** establish that the Terry Choy source rows 30–32 are photographs or records of this exact retail B7022 item. The source table only says “Part of a 3 Pack” and gives the three casting names; it contains no item number, barcode, GP, race number, or individual source photos for these rows.
- Therefore rows 31–32 remain held at the individual Variant/source-item level. The candidate CSV now records the B7022 component specifications as external evidence while preserving the provenance hold. No canonical Variant, Release, or Assortment is created.
