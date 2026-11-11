# Pro Racing 1:43: blocked Variant review queue

**Scope:** the product rows currently marked `hold` in `PRO-RACING-1-43-VARIANT-CANDIDATES.csv` (14 rows after adding the Stewart SF3 #18 source-number conflict).

## Audit result

- 13 held rows mapped one-to-one to the original product source rows.
- No evidence in the source CSV justifies changing any of the 13 casting labels.
- The hold reasons are not all casting problems. They comprise possible second-version claims, missing variant attributes, prototype/sample provenance, assortment-only context, a Bahrain/Sakhir identity question, and a year/package anomaly.
- The source photo column contains asset names or placeholders, not automatically verified visual evidence. Named assets must be inspected before they can support a variant decision.
- No canonical Variant was created and no source value was overwritten.

## Priority order

1. **Rows 3 and 6:** source notes explicitly say “Might be a 2nd version”.
2. **Rows 4–5:** the Stewart SF3 source rows list #17 and #18. External records identify #17 as Johnny Herbert and Hot Wheels 1:43 item 24624; #18 is not a 1999 Stewart SF3 race number. Row 4 remains a candidate, row 5 is held for source-number conflict. The missing information is what the alleged second version is, not proof that the casting label is wrong.
3. **Rows 35 and 41:** compare the Bahrain package clue and Sakhir/Bahrain sample reference. Keep separate Release candidates until item-level evidence establishes their relationship. Row 41 is not in the 13-row hold set, but is the essential comparison row.
4. **Rows 31 and 32:** the commercial set is now identified as Hot Wheels Racing B7022 (JAN 0027084052251). Its three contents and original black/red display box are supported by a catalog record and actual package photographs. The remaining gap is whether Terry Choy's source rows depict these exact retail cars/box, and whether any sample image can be linked to an individual car. Do not infer that link from assortment membership alone.
5. **Rows 9, 12, 13, 24 and 33:** inspect named website/sample assets. Treat prototype/sample provenance as provenance, not as a Variant attribute.
6. **Rows 10 and 19:** obtain independent physical/catalog evidence; the source provides only casting label and year.
7. **Row 36:** resolve the “Represents 1994” book-package note against the source year 2004. Preserve both as separate source facts until the nature of each field is established.

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


## Stewart SF3 source-number review (rows 4–5)

The product-table extraction records two Stewart SF3 rows for 1999: row 4 with tampo **#17**, row 5 with tampo **#18**. Neither row has a usable product photo, toy number, driver name, or packaging reference.

- **Row 4 / #17:** the 1999 Stewart SF3 #17 was driven by **Johnny Herbert**. Hot Wheels catalog item **24624** is independently identified as a 1:43 1999 Stewart SF3 #17 Johnny Herbert. eBay product identifiers list MPN 24624, scale 1:43, and year 1999; a separate factory-sealed listing gives the same car and EAN 074299246241. This is a strong staged release candidate, but the source row has no photo or driver field, so the Terry Choy sample-to-retail-item link is not proven. Sources: [eBay product record 24624](https://www.ebay.com/p/9026414817); [factory-sealed 24624 listing and EAN](https://www.ebay.co.uk/itm/116383918469); [1999 European GP entry/results](https://www.f1stats.ru/1999/1999eur.html).
- **Important adjacent comparator:** Hot Wheels 1:43 item **24527** is not #17. Wheel Wonderland identifies it as Rubens Barrichello's #16 Stewart SF3. This distinction prevents the two Hot Wheels references from being conflated. Source: [Wheel Wonderland 24527](https://www.wheelwonderland.com/en/specials/stewart-sf3-24527/).
- **Row 5 / #18:** the 1999 Stewart SF3 did not race as #18. Its drivers were #16 Rubens Barrichello and #17 Johnny Herbert; #18 belonged to Olivier Panis in the Prost AP02. No Hot Wheels 1:43 Stewart SF3 #18 release was found. This is a source-number conflict, not permission to silently change the row's number or casting. Keep it held pending the original source image or other direct evidence. Sources: [1999 European GP entry/results](https://www.f1stats.ru/1999/1999eur.html); [1999 season team/driver numbers](https://www.gasolinasuper.es/formula-1-1999/).

**Disposition:** row 4 stays a provisional Variant candidate and receives Hot Wheels 24624 as a staged Release candidate; row 5 is moved to hold and added to the blocked review queue. No canonical Variant or Release was created, and no source field was overwritten.


## McLaren MP4/15 rows 7–8: driver-specific release candidates

The source extraction records **David** in row 7 and **Mika** in row 8, both for McLaren MP4/15, 2000. Neither row has a physical product photograph or a toy number. Row 8's photo cell says “Mika Website Asset”; the asset itself and its relation to a physical sample are not established by that label alone.

- **Row 7 / David:** multiple catalog and listing records identify Hot Wheels Racing **26751** as the 1:43 2000 McLaren MP4/15, David Coulthard, race number **#2**. Cars & Trucks Modellbau Frommer explicitly records driver, number, season and scale; eBay listings independently identify MPN 26751 and 1:43, including a factory-sealed listing. [Cars & Trucks Modellbau Frommer](https://www.cars-trucks.de/Modellautos/hot-wheels-1-43/mattel-hot-wheels-racing-26751-mclaren-mercedes-mp4-15-david-coulthard-2000-1-43.html); [eBay 26751 factory-sealed listing](https://www.ebay.co.uk/itm/197813051613); [Unomag item details](https://unomag.ru/26751-mclaren-f1-mp4-15-n-2-season-2000-d-coulthard-silver).
- **Row 8 / Mika:** multiple catalog records identify Hot Wheels Racing **26750** as the 1:43 2000 McLaren MP4/15, Mika Hakkinen, race number **#1**. House of Modelcars records manufacturer, scale, driver, number, original factory packaging and EAN **074299267505**; Diecast.com.ua independently confirms reference 26750 and 1:43. [House of Modelcars](https://www.houseofmodelcars.com/eng/product/mclaren/11456); [Diecast.com.ua](https://diecast.com.ua/en/12824-mclaren-mp4-15.html); [ToyMart](https://www.toymart.com/Hot-Wheels-26750-F1-McLaren-MP4-15/9309).
- **Cross-check:** Wheel Wonderland's 1:43 McLaren MP4/15 casting page lists exactly two 2000 editions, 26750 and 26751. [Wheel Wonderland](https://www.wheelwonderland.com/fr/castings/mclaren-mp4-15-1-43/).

**Disposition:** rows 7 and 8 remain separate provisional Variant candidates because the source distinguishes the two drivers, and the catalog records corroborate distinct #2 and #1 releases. Both receive staged Release candidates, 26751 and 26750 respectively. This is a strong model/catalog match, not proof that the Terry Choy sample rows depict those exact retail examples. No canonical Variant or Release has been created; the original source photo note is preserved.


## Rows 9–10: Jordan EJ10 and Williams FW22 retail comparators

- **Row 9, Jordan EJ10 (2000):** two distinct Hot Wheels 1:43 retail treatments are documented. Item **26754** is Heinz-Harald Frentzen #5 (UPC/EAN 0074299267543); item **26755** is Jarno Trulli #6 (EAN 074299267550). ModelCarsDb lists both driver-specific catalog codes; House of Modelcars confirms 26755, #6, Trulli, scale 1:43, and original factory packaging; Formula143 independently records 26755/Trulli. Models118 and a sealed eBay record corroborate 26754/Frentzen. The source row says only “Jordan Website Asset”; that label is not visual evidence, and the asset has not been identified from pixels. Keep row 9 held between the two candidate Releases. Sources: [ModelCarsDb](https://modelcarsdb.com/makes/Jordan/Mugen-Honda-EJ10-formula-1-2000-Hot-Wheels-1%3A43-3237/); [House of Modelcars](https://www.houseofmodelcars.com/nld/product/jordan/11458); [Formula143](https://formula143.org/2019/06/04/2000-jordan-ej10-trulli/); [Models118](https://models118.nl/jordan-ej10-5-h-h-frentzen-f1-2000-hot-wheels-1-43-26754/); [sealed Frentzen listing](https://www.ebay.com/p/2255618038).
- **Row 10, Williams FW22 (2000):** independent catalogs and listings consistently identify Hot Wheels **26746**, Ralf Schumacher #9, 1:43, EAN **074299267468** (13-digit UPC form **0074299267468**). House of Modelcars explicitly states original factory packaging; Yuui independently confirms the MPN, scale, driver, year and number; bol and eBay listings add corroboration and photographs. This is a strong retail Release candidate, but the source row is “Image Not Available” and has no driver, number, SKU or EAN. Keep source-row linkage held. Sources: [House of Modelcars](https://www.houseofmodelcars.com/eng/product/williams-f1/11460); [Yuui](https://www.yuui.nl/en/collections/menu/products/2000-williams-bmw-fw22-ralf-schumacher); [bol](https://www.bol.com/nl/nl/p/williams-f1-fw22-bmw-modelauto-schaal-1-43/9300000150926722/); [eBay item record](https://www.ebay.com/p/14012068030); [Wheel Wonderland](https://www.wheelwonderland.com/fr/specials/williams-fw22-26746/).
- No canonical Variant or Release was created. External retail catalog identity is not the same as provenance for the Terry Choy source row.


## Rows 11–12: Ferrari F1-2000 and Jaguar R1

- **Row 11, Ferrari F1-2000 (2000):** Hot Wheels 1:43 baseline retail item **26748**, Michael Schumacher #3, is corroborated by Yuui, bol, diecast.com.ua and Ferrari catalog records. House of Modelcars lists a **26748M** “Marlboro Livery” #3 treatment with EAN 074299267482 and original factory packaging. Formula143 also documents a separate F1-2000 in the **B0722 Michael Schumacher Ferrari Hat Trick** set, described as a “race dirty version” representing the Malaysian GP. These are distinct catalog contexts/treatments; the Terry Choy source row only names “Ferrari F12000 Website Asset” and contains no actual image or deco detail. Do not choose between them without inspecting the asset. Sources: [Yuui 26748](https://www.yuui.nl/en/products/2000-ferrari-f1-2000-michael-schumacher-2); [bol 26748](https://www.bol.com/nl/nl/p/ferrari-f1-2000-hotwheels-1-43-2000-michael-schumacher-scuderia-ferrari-marlboro-26748/9300000150926555/); [House of Modelcars 26748M](https://www.houseofmodelcars.com/eng/product/ferrari-f1/6048); [Formula143 B0722](https://formula143.org/2019/07/02/2000-ferrari-f1-2000-schumacher/); [ToyWonders B0722 set contents](https://www.toywonders.com/site09/diecastA/Mattel_Hot_Wheels_Racing_Ferrari_Micheal_Shumacher_Championship_Collection_1_43_Assoted_L6237_238p7050.html).
- **Row 12, Jaguar R1 (2000):** two Hot Wheels 1:43 driver-specific releases are corroborated. **26752** is Eddie Irvine #7 (EAN 074299267529); **26753** is Johnny Herbert #8 (EAN 074299267536). Formula143 documents both driver/number/scale/item combinations; House of Modelcars confirms 26753 and original factory packaging; R.M.Toys and eBay corroborate 26752. The source row has only “Jaguar r1 Website Asset”, so neither SKU can be assigned until that image is visually identified. Sources: [Formula143 Irvine](https://formula143.org/2019/03/09/2000-jaguar-r1/); [Formula143 Herbert](https://formula143.org/2019/07/03/2000-jaguar-r1-herbert/); [House of Modelcars 26753](https://www.houseofmodelcars.com/eng/product/jaguar-f1/11462); [R.M.Toys 26752](https://www.rmtoys.co.uk/products/hot-wheels-1-43-scale-diecast-26752-jaguar-r1-eddie-irvine); [eBay 26752](https://www.ebay.co.uk/itm/176004960669).
- No canonical Variant or Release was created. Both rows remain held pending visual identification of their named website assets.


## Rows 13–14: Jaguar R2 FEP and Ferrari F2001 #55573

- **Row 13, Jaguar R2 (source year 2000):** the source photo reference is “FEP Signed 2000 Jaguar Terry Proto (3)”. FEP means Final Engineering Pilot, a pre-production sample used for engineering/graphics review, not a normal retail release. The Hot Wheels 1:43 Jaguar R2 retail releases found in catalogs are both dated **2001**: **50205** Eddie Irvine #18 (EAN 074299502057) and **50206** Pedro de la Rosa. Wheel Wonderland lists both as the only two 1:43 R2 releases; House of Modelcars confirms 50205, scale, driver, #18 and original factory packaging. This does not identify the livery or retail successor of the signed 2000 FEP sample. Keep as prototype-provenance hold; do not map to 50205/50206. Sources: [FEP explanation](https://hotwheels.fandom.com/wiki/Final_engineering_pilot); [Wheel Wonderland 50205](https://www.wheelwonderland.com/en/specials/jaguar-r2-50205/); [Wheel Wonderland 50206](https://www.wheelwonderland.com/en/specials/jaguar-r2-50206/); [House of Modelcars 50205](https://www.houseofmodelcars.com/eng/product/jaguar-f1/11464); [Diecast Company](https://www.diecastcompany.nl/speelgoedsearchresults?artikelstatus=6&cid=&fid=&jid=&mid=&nobotcode=1755463999&pagina=2118&schaal=&voorraad=&zoekwoord=).
- **Row 14, Ferrari F2001 #1 (2001):** source row explicitly gives toy number **55573** and “Single Pack”. House of Modelcars independently identifies 55573 as Hot Wheels Ferrari F2001, Michael Schumacher #1, 1:43, EAN **074299555732**, supplied in original factory packaging. Armand Modelcars independently confirms manufacturer, scale, item number, EAN, driver and race number. This is a strong source-to-release match because casting, year, #1, toy number and package context all agree. Keep the existing Variant candidate linked to the row's #1 attribute; do not conflate with other F2001 treatments, 2-packs, 3-packs or the later 50213 catalog entry. Sources: [House of Modelcars](https://www.houseofmodelcars.com/eng/product/ferrari-f1/6047); [Armand Modelcars](https://www.armand-modelcars.nl/nld/product/ferrari-f1/6047); [Hot Wheels Wiki source table](https://hotwheels.fandom.com/wiki/Pro_Racing_Grand_Prix_%281%3A43%29_series).
- No canonical entities were created. Row 13 remains held as a prototype; row 14 is retained as a strong staged Release candidate, not yet canonicalized.


## Rows 15–16: Ferrari F2001 World Champion / Christmas labels

- **Row 15:** source says “World Champion Single Pack” and names a sample photo, but gives no toy number, driver, tampo or barcode. Hot Wheels 55573 is independently confirmed as a 1:43 Schumacher #1 single-pack retail model; 50213 (Schumacher) and 50214 (Barrichello) are separately cataloged 2001 1:43 releases. Hot Wheels 55602 is a 2002 Constructors Champions two-car set with Schumacher and Barrichello F2001s; Fongu's review says the Schumacher model also appeared in a standard Hot Wheels box. These are useful comparators, not proof that row15 is any one of them. Keep release identity and variant on hold. Sources: [Fandom source table](https://hotwheels.fandom.com/wiki/Pro_Racing_Grand_Prix_(1%3A43)_series); [55573 House of Modelcars](https://www.houseofmodelcars.com/eng/product/ferrari-f1/6047); [50213 Wheel Wonderland](https://www.wheelwonderland.com/en/specials/f2001-50213/); [50214 Classic Trax](https://www.classictrax.co.uk/product/rubens-barrichello-hot-wheels-diecast-model-car-143-scale-ferrari-f2001/); [55602 set listing](https://www.rihappy.com.br/pack-2-hot-wheels---1-43---ferrari-2001-constructor-s-champions---hot-wheels-racing---55602-1002433941/p); [Fongu review](https://fongugp4.blogspot.com/2019/07/143-model-review-2001-world-champion.html).
- **Row 16:** source says “World Champion Christmas 2001” and photo reference “Michael Schumacher World Champion Christmas 2001”. Exact research did not verify a Hot Wheels 1:43 F2001 under this title. Similar Christmas 2001 F2001 listings found are explicitly **1:18**, so they cannot be used to identify this 1:43 source row. Keep release and variant on hold.
- No SKU or canonical Variant/Release assigned to rows 15–16. Source wording is preserved without converting it into model attributes.


## Row 20: Williams FW21 / 2001 Compaq #5 discrepancy

- Source row 20 is preserved exactly as **Williams FW21**, year **2001**, color text **“Compaq” & racing decals**, tampo **#5**, note **Yellow helmet**, photo reference **“2001 Compaq Terry Sample (1)”**. The image itself is not present in the product-table extraction, so the model cannot be visually checked here.
- Strong retail comparator: Hot Wheels **50211**, Williams **FW23**, Ralf Schumacher #5, 2001, 1:43. Catalog listings identify this exact model/item number and scale: [Modellspielwaren Reinhardt](https://www.modellspielwaren-reinhardt.de/1-43-Formel-1/1-43-Hot-Wheels-50211-Williams-F1-FW-23-Ralf-Schumacher.html); [Ricardo](https://www.ricardo.ch/de/a/williams-bmw-fw23-5-2001-%28ralf-schumacher%29-1-43-hot-wheels-1206940164/).
- Contradiction: the FW21 was a **1999** car. Its #5 driver was Alessandro Zanardi; #6 was Ralf Schumacher. Hot Wheels 1:43 FW21 item **24524** is cataloged as 1999 Zanardi: [Williams Database](https://www.williamsdb.com/the-history-of-williams/the-history-of-williams-1999/); [StatsF1](https://www.statsf1.com/en/williams/grand-prix-1999.aspx); [Wheel Wonderland 24524](https://www.wheelwonderland.com/en/specials/williams-fw21-24524/); [Formula143](https://formula143.org/2019/06/04/1999-williams-fw21-zanardi/).
- The source attributes (2001 + Compaq + #5 + yellow helmet) strongly fit FW23/Ralf Schumacher, but this is not enough to overwrite the source casting label or identify the sample as retail item 50211. **Hold** pending visual inspection of the actual Terry sample.


## Rows 20–21: paired 2001 Williams Compaq entries and FW21/FW23 conflict

- **Row 20:** Williams FW21, 2001, Compaq/racing decals, #5, Yellow helmet. Hot Wheels **50211** is cataloged as 1:43 Williams FW23, 2001, Ralf Schumacher #5.
- **Row 21:** Williams FW21, 2001, Compaq/racing decals, #6, White helmet. Hot Wheels **50212** is cataloged as 1:43 Williams FW23, 2001, Juan Pablo Montoya #6; independent records confirm the scale, driver, number and 2001 FW23 identity. [TPI Modellauto 50212](https://tpi-modellauto.ch/williams/8904-williams-bmw-fw23-1-43-074299502125.html); [We-R-Toys 50212](https://wertoys.com/hot-wheels-racing-williams-f1-team-fw23-juan-pablo-montoya-car-2000-mattel-50212/); [LastDodo 50212](https://www.lastdodo.de/de/items/883909-williams-fw23-bmw).
- The two rows form a compelling paired hypothesis: 2001 + Compaq + #5/yellow helmet matches FW23/Ralf Schumacher 50211, while 2001 + Compaq + #6/white helmet matches FW23/Juan Pablo Montoya 50212. This is materially stronger than assessing row20 alone.
- The conflict remains: FW21 was the **1999** Williams, with #5 Alessandro Zanardi and #6 Ralf Schumacher. Hot Wheels 1:43 FW21 #6/Ralf comparator is **24625**, not the 2001 Montoya model. [Williams Database FW21](https://www.williamsdb.com/car-profiles/fw21/); [Hot Wheels FW21 #6 24625](https://scalemodels4u.ru/en/product/hot-wheels-mattel-williams-f1-team-fw21-6-ralf-schumacher-1999.html).
- **Disposition:** preserve the source casting label “FW21” and source year “2001”; stage FW23 #5/#6 as separate hypotheses only. No source photographs were available for visual inspection, so neither 50211 nor 50212 is assigned to the Terry Choy samples and no canonical Variant/Release is created.

## Row 22: generic Ferrari F2002, release identity unresolved

- Source row22 contains only “Ferrari F2002” and year 2002. Its photo is marked unavailable; there is no driver, race number, GP, toy number, packaging or assortment clue.
- Hot Wheels 1:43 comparators include **54618**, Ferrari F2002 Michael Schumacher #1 (Canadian GP/Vodafone livery); **B7022**, a three-car set containing F1-2000 #3, F2001 #1 and F2002 #1 (Canadian GP); **B0722**, the Ferrari Hat Trick 2000–2002 set; and **L6237**, the five-car Schumacher Championship Collection containing a 2002 British GP F2002. Sources: [54618 Alex Reade](https://alexreade.net/products/mattel-1-43-2002-ferrari-f2002-schumacher-54618); [Hattons 54618](https://www.hattons.co.uk/863550/hot_wheels_elite_54618_2002_ferrari_f2002_michael_schumacher/stockdetail); [Suruga-ya B7022](https://www.suruga-ya.jp/kaitori/kaitori_detail/770004005); [Formula143 B0722](https://formula143.org/2019/07/27/2002-ferrari-f2002-schumacher/); [Toy Wonders L6237](https://www.toywonders.com/ProductCart/pc/Mattel-Hot-Wheels-Racing-Ferrari-Micheal-Shumacher-Championship-Collection-1-43-Assoted-L6237-p7050.htm).
- These are distinct release/assortment contexts, not interchangeable SKU aliases. Row23 separately records “150 GP Wins” with its own photo reference; do not transfer that context to row22.
- **Disposition:** retain row22 as an unspecified F2002 candidate and hold exact Variant/Release identity. No canonical entities created.


## Row 24: Williams FW24, 2002 — scale/manufacturer identity unresolved

- Source row24 contains only **Williams FW24**, year **2002**, and photo reference **“2002 Williams F1 Terry”**. The source image was not available for visual inspection in this review.
- Hot Wheels FW24 retail products **54624** (Ralf Schumacher #5) and **54625** (Juan Pablo Montoya #6) are confirmed as **1:18**, not 1:43. [Wheel Wonderland 54624](https://www.wheelwonderland.com/fr/specials/williams-fw24-54624/); [Wheel Wonderland 54625](https://www.wheelwonderland.com/fr/specials/williams-fw24-54625/).
- The documented 1:43 FW24 retail models found are **Minichamps**, including 400020005 (Ralf Schumacher #5) and 400020006 (Juan Pablo Montoya #6), with further season-specific variants. [Yuui 400020005](https://www.yuui.nl/en/products/2002-williamsf1-bmw-fw24-ralf-schumacher-3); [House of Modelcars 400020005](https://www.houseofmodelcars.com/eng/product/williams-f1/11514); [Formula43 2002 list](https://www.formula43.net/F102.html).
- The Fandom series page's placement of the row in a 1:43 table does not independently prove that the Terry sample is a retail Hot Wheels 1:43 product. A prototype/sample, a manufacturer attribution error, or another identity remain possible but unproven.
- **Disposition:** preserve the source casting/year, keep Variant and Release on hold, and do not assign Hot Wheels 54624/54625 or Minichamps 1:43 SKUs to this sample.

## Row 25: McLaren MP4/16 / 2002 / Kimi — FEP sample and chassis-year conflict

- The source product row records McLaren MP4/16, year 2002, tampo Kimi, and photo reference “2002 McLaren Terry Choy Proto (4)”.
- I visually inspected the three archived Gallery assets for 2002 McLaren Terry Choy Proto (1)–(3). They show a Kimi-marked McLaren model in a display package, the reverse of the package, and the underside. The Gallery captions identify the subject as “FEP 2002 McLaren F1”, “No UPC Code”, and “Blank Base”. This supports an engineering/final-engineering-pilot sample interpretation rather than an ordinary retail release.
- The source row's exact (4) photograph is not among those three Gallery assets. The physical identity between row25 and the Gallery trio is therefore provisional, even though the subject and Kimi clue are closely aligned.
- There is a real chassis-year conflict: McLaren's 2002 Formula One car was the MP4-17, driven by Kimi Räikkönen as #4. [F1ERA 2002 McLaren season](https://f1era.com/team/mclaren/2002); [Formula Web Magazine](https://www.formulawebmagazine.com/f1team/13/west-mclaren-mercedes).
- Known Hot Wheels 1:43 MP4/16 retail comparators are 2001 models: 50209 Mika Häkkinen and 50210 David Coulthard. Neither is a Kimi 2002 match. [We-R-Toys 50209](https://wertoys.com/hot-wheels-racing-mclaren-mp4-16-mika-hakkinen-car-2000-mattel-50209/); [Wheel Wonderland 50210](https://www.wheelwonderland.com/en/specials/mclaren-mp4-16-50210/); [Cars & Trucks 50210](https://www.cars-trucks.de/Modellautos/hot-wheels-1-43/mattel-hot-wheels-racing-50210-mclaren-mercedes-mp4-16-david-coulthard-2001-1-43.html).
- Disposition: preserve the source casting label and year verbatim. Hold exact Variant/Release identity. Do not assign 50209/50210, do not silently rename the sample MP4/17, and do not create canonical entities. The exact row25 image (4), a legible base/plinth code, or Mattel documentation is needed to resolve the identity.

## Row 30: Ferrari F1-2000 / “Part of a 3 Pack” — B7022 candidate, source link held

- The source row records Ferrari F1-2000, table year 2002, note “Part of a 3 Pack”, and “Image Not Available”. It provides no tampo, driver, racing number, UPC, package identifier, or individual photograph.
- Mattel/Hot Wheels Racing B7022 is independently confirmed as a 1:43 three-car set, JAN 0027084052251. Suruga-ya specifies its contents: F1-2000 #3 Shell, Malaysian GP Sepang (22 Oct 2000); F2001 #1 Shell, Belgian GP Spa (2 Sep 2001); and F2002 #1 Vodafone, Canadian GP Montreal (9 Jun 2002). [Suruga-ya B7022 catalog](https://www.suruga-ya.jp/kaitori/kaitori_detail/770004005).
- A B7022-labeled eBay listing shows the original Hot Wheels Racing three-car display box. [B7022 package listing](https://www.ebay.com/itm/204701681876). Formula143 independently identifies the F1-2000 member as Michael Schumacher #3, Malaysian GP, 1:43. [Formula143 F1-2000 B7022](https://formula143.org/2019/07/02/2000-ferrari-f1-2000-schumacher/).
- Disposition: B7022 is a strong assortment candidate for rows 30–32, but row30 itself cannot yet be physically tied to that exact retail model. The B7022 F1-2000 has specific #3 Shell Malaysian GP decoration; the source row lacks those details. Do not merge it with the generic row11 F1-2000 candidate or create canonical Variant/Release/Assortment links.
- Gallery items 39–40 and 43–44 show a separate six-in-a-row Ferrari F1 World Champions display. They are not evidence for the B7022 three-pack and must not be conflated with it.
