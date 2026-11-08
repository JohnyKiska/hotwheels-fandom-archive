# Mainline ↔ Premium 2025 comparison

Date: 2026-11-08
Status: first-pass structured extraction and exact normalized-name comparison.
Scope: Mainline 2025 vs Car Culture 2025, Boulevard 2025, and Car Culture: Team Transport 2025.

## Fixed source inputs

| Dataset | Repository / branch | Path | Fandom revision | Git blob SHA |
|---|---|---|---:|---|
| Mainline 2025 | JohnyKiska/hotwheels / archive/historical-html-1968-2026 | ALLHW/2025/List of 2025 Hot Wheels _ Hot Wheels Wiki _ Fandom.html | 811101 | b155324bd3fca3281ed91fd7a8fa992e04f1662f |
| Car Culture 2025 | JohnyKiska/hotwheels-fandom-archive / main | Modern Special Series/Car Culture/2025 Car Culture _ Hot Wheels Wiki _ Fandom.html | 816325 | ea4d1a0dbf111f28e1c60a6a6e4d6f183481b6dc |
| Boulevard 2025 | same | Modern Special Series/Boulevard/2025 Hot Wheels Boulevard _ Hot Wheels Wiki _ Fandom.html | 795779 | 3c36cc3686cc0483a2f21a7dd275de577ed83b38 |
| Team Transport 2025 | same | Modern Special Series/Car Culture/2025 Car Culture_ Team Transport _ Hot Wheels Wiki _ Fandom.html | 768859 | ab7a0ec32ccdd994a25bfb87ebf2b824094abcc4 |

Mainline archive manifest SHA-256: bbdac9d328130734328c1bb9b8a01fc738055dd596f0b7dfcf286ae5b142672c. GitHub Contents metadata reports 824,886 bytes.

## Extraction and QA

HTML table markup was parsed directly. Mainline's primary table contains 1 header row and 440 data rows. It has 440 distinct Toy # values and 250 distinct Collector # values. 146 rows are explicitly marked (2nd Color). First row: HYW18 / Collector #001 / Mazda MX-5 Miata. Final row: JJM42 / Collector #250 / 1983 Porsche 928S (2nd Color). A trailing photo column is blank in all 440 rows and is not treated as a missing catalog attribute.

Premium table counts:
- Car Culture: 8 themed tables, 6 rows each, 48 rows total. Segments: Hammer Drop, Silhouettes, HW Off Road, Fast Wagons, Circuit Legends, Eurospeed, Ronin Run II, Timeless Icons. 40 distinct normalized casting names.
- Boulevard: Mix 1–5, 5 rows each, 25 rows total. Separate Boxed Set table excluded from loose-vehicle row count.
- Team Transport: 5 tables, 29 component rows total, 26 distinct component names. Continuation rows omit bundle Toy # and Series # cells; names were read from the first cell on continuation rows and third cell on bundle-start rows. This preserves packaged set SKU vs individual component.

## Comparison method

Source model/casting names were normalized by lowercasing, normalizing curly apostrophes, replacing punctuation runs with spaces, and collapsing whitespace. Results are name-match candidates only. They do not establish identical casting, body, chassis, tooling, decoration, or physical release. Source notes remain literal source data.

## Exact normalized-name candidates

### Mainline 2025 ↔ Car Culture 2025

| Car Culture segment | Premium Toy # | Casting name | Mainline Toy # | Collector # | Mainline series |
|---|---|---|---|---|---|
| Timeless Icons | HRW08 | Mazda 787B | JBB39 | 226 | Peak Pursuit |
| HW Off Road | JBK74 | Land Rover Defender 90 | JBB29 | 210 | Then and Now |

Result: 2 matching rows out of 48 Car Culture rows.

### Mainline 2025 ↔ Boulevard 2025

| Boulevard mix | Premium Toy # | Casting name | Mainline Toy # | Collector # | Mainline series |
|---|---|---|---|---|---|
| Mix 5 | JHW26 | Ford GT | HYY92 | 159 | HW Modified |
| Mix 5 | JBL29 | Ford RS200 | JBB49 | 247 | Peak Pursuit |
| Mix 5 | JBL29 | Ford RS200 | JBC49 | 247 | Peak Pursuit / Super Treasure Hunt |

Result: 2 Boulevard rows out of 25. Ford RS200 maps to two Mainline rows under Collector #247 (regular and STH), so Collector # is not a unique release key.

### Mainline 2025 ↔ Team Transport 2025

| Team Transport set Toy # | Series # | Component casting | Mainline Toy # | Collector # | Mainline series |
|---|---|---|---|---|---|
| JBM29 | #74 | Jaguar Mk1 | HYX19 | 075 | HW Race Day |
| JBM35 | #78 | DMC DeLorean | HYW88 | 036 | HW Art Cars |
| JBM36 | #80 | '73 Honda Civic Custom | JBB42 | 231 | Then and Now |
| JBM36 | #80 | '73 Honda Civic Custom | JBC46 | 231 | Then and Now / Super Treasure Hunt |

Result: 3 distinct component-name candidates across 29 component rows. '73 Honda Civic Custom maps to regular and STH Mainline rows under Collector #231. Team Transport Toy # identifies the packaged bundle, not an individual component.

## Combined result and limitations

- Car Culture: 2 Premium rows with exact normalized-name candidates.
- Boulevard: 2 Premium rows with exact normalized-name candidates.
- Team Transport: 3 component names with candidates (4 Mainline row links because two components map to regular + STH rows).
- These are not unique casting counts and are not confirmed tooling matches. No fuzzy/near-name matches are included.
- Next: visually inspect candidate pairs and body/chassis/base/wheel evidence; preserve regular and STH releases separately; preserve Team Transport bundle SKU, component order, component type, and source row grouping.
- This is a comparison of archived Fandom pages, not an independent Mattel catalog, packaging, or physical-sample audit.