# Mainline 2010: ordinary vs International source comparison

## Sources

- Ordinary: `ALLHW/2010/List of 2010 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`, blob `26c08a2134f9c4df6b4c634a2cf9b3c4e941966c`, revision 815649.
- International: `ALLHW/2010/List of 2010 Hot Wheels (International) _ Hot Wheels Wiki _ Fandom.html`, blob `2ef979cd1dda8236096ed4eb9c490aff5b6ce8e1`, revision 815650.

## High-level comparison

| Measure | Ordinary | International |
|---|---:|---:|
| Source rows | 440 | 228 |
| Annual Mainline rows before tire-exclusive sections | 422 | 228 |
| Unique Toy # | 252 | 226 |
| Unique Collector # | 240 | 214 |
| Collector # range | 001–240 | 001–214 |
| TH rows | 12 | 12 |
| STH rows | 12 | 12 |

Ordinary list has two additional tire-exclusive sections with 18 rows; all 18 Toy # values already occur in the ordinary annual Mainline tables. International has no corresponding tire-exclusive sections in this snapshot.

## Toy # overlap

Exact Toy # comparison between ordinary annual Mainline tables (excluding the two tire-exclusive appendices) and International:

- 213 Toy # values occur in both sources.
- 39 Toy # values occur only in the ordinary annual Mainline tables.
- 13 Toy # values occur only in the International list.

International-only Toy # values:

| Toy # | Model Name |
|---|---|
| R0927 | Gallardo LP 560-4 |
| R0934 | Ford Focus RS |
| R0940 | Lamborghini Reventón Roadster |
| R0944 | Citroën C4 Rally |
| R0946 | Mazda Furai |
| R0948 | Scirocco GT 24 |
| R6452 | '86 Monte Carlo SS |
| R6453 | Volkswagen SP2 |
| R6459 | '10 Aston Martin DBS |
| R4748 | Classic Packard |
| R4749 | Ratbomb |
| R4750 | Shelby Cobra Daytona Coupe |
| R4754 | '69 Ford Torino Talladega |

## Interpretation boundaries

- A shared Toy # is evidence of a cross-listing candidate, not proof that regional releases, packaging, paint/deco or exact release variants are identical.
- Many ordinary model-name strings include `(2nd Color)` or `(3rd Color)`, while the International list uses the base name. Preserve raw names and derive normalized comparison names separately.
- International TH/STH rows intentionally share Collector #053–064; do not collapse those pairs.
- International Collector #087 has three AMC Javelin AMX color entries under Toy #R7504.
- Keep the two source datasets distinct in the database and represent cross-listing links with provenance and confidence.
