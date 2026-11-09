# Hot Wheels Haulers extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Haulers _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `5926fd2198d7e5838d7947c9c89b974375214176`
- Manifest file size: 673,268 bytes
- Manifest SHA-256: `65006A2FD7C7DF9E141AE845F9AE3E793AAB1BEA906079A8C91DDE4293E3C554`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 18
- Product rows: 242
- Export columns: 21
- Excluded tables: 0 (non-product/navigation or single-column tables)

## Product tables
- 1997 [ ]: 9 data rows, 6 source columns. Headers: Casting Name | Color | Graphic | Note | Photo | Photo Carded
- Multi-Packs [ ]: 16 data rows, 6 source columns. Headers: Toy # | Name | Vehicles | Note | Photo | Photo Carded
- 1998 [ ]: 6 data rows, 6 source columns. Headers: Casting Name | Color | Graphic | Note | Photo | Photo Carded
- Multi-Packs [ ]: 4 data rows, 6 source columns. Headers: Toy # | Name | Vehicles | Note | Photo | Photo Carded
- 24K Plated Gold Haulers [ ]: 4 data rows, 6 source columns. Headers: Casting Name | Color | Graphic | Note | Photo | Photo Carded
- 1999 [ ]: 30 data rows, 7 source columns. Headers: Casting Name | Color | Graphic | Mix | Note | Photo | Photo Carded
- Multi-Packs [ ]: 19 data rows, 6 source columns. Headers: Toy # | Name | Vehicles | Note | Photo | Photo Carded
- 2000 [ ]: 12 data rows, 7 source columns. Headers: Casting Name | Color | Graphic | Mix | Note | Photo | Photo Carded
- 2000 Sub-Series [ ]: 24 data rows, 8 source columns. Headers: Series | Casting Name | Color | Graphic | Mix | Note | Photo | Photo Carded
- Multi-Packs [ ]: 30 data rows, 6 source columns. Headers: Toy # | Name | Vehicles | Note | Photo | Photo Carded
- Metallic Haulers [ ]: 4 data rows, 6 source columns. Headers: Casting Name | Color | Graphic | Note | Photo | Photo Carded
- 2001 [ ]: 21 data rows, 8 source columns. Headers: Sub-Series | Toy # | Casting Name | Color | Graphic | Note | Photo | Photo Carded
- Unreleased Assortment [ ]: 21 data rows, 7 source columns. Headers: Sub-Series | Toy # | Casting Name | Color | Graphic | Note | Photo
- Multi-Packs [ ]: 4 data rows, 6 source columns. Headers: Toy # | Name | Vehicles | Note | Photo | Photo Carded
- New Deluxe Haulers [ ]: 4 data rows, 6 source columns. Headers: Casting Name | Color | Graphic | Note | Photo | Photo Carded
- 2002 [ ]: 15 data rows, 7 source columns. Headers: Toy # | Casting Name | Color | Graphic | Note | Photo | Photo Carded
- 2nd Assortment [ ]: 15 data rows, 7 source columns. Headers: Toy # | Casting Name | Color | Graphic | Note | Photo | Photo Carded
- Multi-Packs [ ]: 4 data rows, 6 source columns. Headers: Toy # | Name | Vehicles | Note | Photo | Photo Carded

## QA notes
- Product-table rows are retained in source order.
- Original source headers and cell content are preserved in the final two columns.
- Unmapped source columns remain available in Raw source headers and Raw source cells.
- Empty values remain empty; no casting identity or release equivalence has been inferred.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-HOT-WHEELS-HAULERS.csv`
