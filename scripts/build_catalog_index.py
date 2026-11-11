#!/usr/bin/env python3
"""Build a source-preserving, searchable Hot Wheels catalog index.

Mainline groups are scoped to their model year and Collector # where available.
Premium groups are scoped to year, product family, series section and normalized
model name. These are provisional navigation groups, not proven casting IDs.
"""
from __future__ import annotations

import csv
import html
import json
import re
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTRACTIONS = ROOT / "research" / "extractions"
OUT = ROOT / "catalog" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

PREMIUM_MARKERS = (
    "CAR-CULTURE", "HOT-WHEELS-BOULEVARD", "FAST-FURIOUS-PREMIUM-SERIES",
    "POP-CULTURE", "REPLICA-ENTERTAINMENT", "HOT-WHEELS-ENTERTAINMENT",
    "TEAM-TRANSPORT", "TEAM-TRANSPORTER",
)

def clean(value: object) -> str:
    text = html.unescape(str(value or ""))
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def norm(value: str) -> str:
    value = clean(value).casefold()
    value = re.sub(r"\s*\((?:\d+(?:st|nd|rd|th)\s+color|super treasure hunt|treasure hunt)[^)]*\)\s*$", "", value, flags=re.I)
    return re.sub(r"[^a-z0-9]+", " ", value).strip()

def year_from(path: Path) -> str:
    match = re.search(r"(?:19|20)\d{2}", path.name)
    return match.group(0) if match else ""

def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

def premium_family(path: Path) -> str:
    name = path.name.upper()
    if "CAR-CULTURE-2-PACK" in name: return "Car Culture 2-Pack"
    if "CAR-CULTURE" in name: return "Car Culture"
    if "TEAM-TRANSPORT" in name or "TEAM-TRANSPORTER" in name: return "Team Transport"
    if "FAST-FURIOUS" in name: return "Fast & Furious Premium"
    if "BOULEVARD" in name: return "Boulevard"
    if "POP-CULTURE" in name: return "Pop Culture"
    if "REPLICA-ENTERTAINMENT" in name or "HOT-WHEELS-ENTERTAINMENT" in name: return "Entertainment"
    return "Premium / other"

def extract_premium(path: Path, rows: list[dict]) -> list[dict]:
    result = []
    for row in rows:
        if (row.get("record_type") or "").strip() != "product_table_row":
            continue
        try:
            headers = json.loads(row.get("source_headers_json") or "[]")
            cells = json.loads(row.get("source_cell_values_json") or "[]")
        except (json.JSONDecodeError, TypeError):
            continue
        values = {str(k).strip().casefold(): clean(v) for k, v in zip(headers, cells)}
        def get(*names):
            for name in names:
                if values.get(name.casefold()):
                    return values[name.casefold()]
            return ""
        model = get("Casting Name", "Model Name", "Car Name")
        toy = get("Toy #", "Toy Number")
        if not model and not toy:
            continue
        notes = get("Notes")
        base_codes = re.findall(r"\b[A-Z]\d{2,4}[A-Z]?\b", notes)
        identical = re.findall(r"Identical to\s+([A-Z0-9, /-]+)", notes, flags=re.I)
        result.append({
            "catalog": "Premium",
            "year": year_from(path),
            "family": premium_family(path),
            "source_file": path.relative_to(ROOT).as_posix(),
            "source_section": clean(row.get("source_section")),
            "source_table_index": clean(row.get("source_table_index")),
            "source_row_index": clean(row.get("source_row_index")),
            "toy_number": toy,
            "collector_number": get("Col #", "Collector #"),
            "model_name": model,
            "series": clean(row.get("source_section")),
            "series_number": get("Series #", "Col #"),
            "color": get("Body Color", "Color"),
            "tampo": get("Tampos", "Tampo", "Decoration"),
            "base": get("Base", "Base Color / Type"),
            "wheel_type": get("Wheel Type"),
            "notes": notes,
            "base_codes": sorted(set(base_codes)),
            "explicit_identical_to": sorted(set(x.strip(" ,") for x in identical if x.strip(" ,"))),
            "source_page": clean(row.get("source_file")),
        })
    return result

def extract_mainline(path: Path, rows: list[dict]) -> list[dict]:
    result = []
    year = year_from(path)
    for index, row in enumerate(rows, 1):
        model = clean(row.get("Model Name") or row.get("Casting Name") or row.get("Car Name") or row.get("Toy Name"))
        toy = clean(row.get("Toy #") or row.get("Toy Number"))
        if not model and not toy:
            continue
        result.append({
            "catalog": "Mainline",
            "year": year,
            "family": "Mainline",
            "source_file": path.relative_to(ROOT).as_posix(),
            "source_section": clean(row.get("Section heading") or row.get("Series")),
            "source_row_index": clean(row.get("Row within table") or row.get("Row within section") or str(index)),
            "toy_number": toy,
            "collector_number": clean(row.get("Collector #") or row.get("Col. #") or row.get("Col #")),
            "model_name": model,
            "series": clean(row.get("Series")),
            "series_number": clean(row.get("Series #")),
            "color": clean(row.get("Color") or row.get("Body Color")),
            "tampo": clean(row.get("Tampo") or row.get("Tampos")),
            "base": clean(row.get("Base Color / Type") or row.get("Base Color")),
            "wheel_type": clean(row.get("Wheel Type")),
            "notes": clean(row.get("Notes")),
            "base_codes": sorted(set(re.findall(r"\b[A-Z]\d{2,4}[A-Z]?\b", clean(row.get("Notes"))))),
            "explicit_identical_to": [],
            "source_page": "",
        })
    return result

def main():
    files = sorted(EXTRACTIONS.glob("MAINLINE-*.csv"))
    premium_files = sorted(p for p in EXTRACTIONS.glob("MODERN-SPECIAL-SERIES-*.csv")
                           if any(marker in p.name.upper() for marker in PREMIUM_MARKERS))
    records = []
    inventory = []
    for path in files + premium_files:
        rows = read_csv(path)
        if path.name.startswith("MAINLINE-"):
            extracted = extract_mainline(path, rows)
            catalog = "Mainline"
        else:
            extracted = extract_premium(path, rows)
            catalog = "Premium"
        records.extend(extracted)
        inventory.append({
            "file": path.relative_to(ROOT).as_posix(),
            "catalog": catalog,
            "year": year_from(path),
            "source_rows": len(rows),
            "product_records": len(extracted),
        })

    groups = defaultdict(list)
    for record in records:
        name_key = norm(record["model_name"])
        if record["catalog"] == "Mainline":
            # Collector numbers are year-specific. Early-era sources often lack them.
            scope = record["collector_number"] or name_key
            key = f'mainline:{record["year"]}:{scope}'
        else:
            key = "|".join(("premium", record["year"], record["family"],
                            norm(record["series"]), name_key))
        record["candidate_group_id"] = key
        groups[key].append(record)

    group_rows = []
    for key, members in sorted(groups.items()):
        names = sorted({m["model_name"] for m in members if m["model_name"]})
        toy_numbers = sorted({m["toy_number"] for m in members if m["toy_number"]})
        bases = sorted({code for m in members for code in m["base_codes"]})
        explicit = sorted({code for m in members for code in m["explicit_identical_to"]})
        group_rows.append({
            "id": key,
            "catalog": members[0]["catalog"],
            "year": members[0]["year"],
            "family": members[0]["family"],
            "series": members[0]["series"],
            "display_name": names[0] if names else "",
            "model_names": names,
            "toy_numbers": toy_numbers,
            "record_count": len(members),
            "casting_status": "single_source_record" if len(members) == 1 else "provisional_same_casting",
            "evidence_flags": (["multiple_source_records"] if len(members) > 1 else [])
                              + (["base_code_evidence"] if bases else [])
                              + (["explicit_identical_note"] if explicit else []),
            "base_codes": bases,
            "explicit_identical_to": explicit,
            "source_files": sorted({m["source_file"] for m in members}),
        })

    stats = {
        "mainline_files": len(files),
        "premium_files": len(premium_files),
        "source_files": len(inventory),
        "product_records": len(records),
        "mainline_records": sum(r["catalog"] == "Mainline" for r in records),
        "premium_records": sum(r["catalog"] == "Premium" for r in records),
        "candidate_groups": len(group_rows),
        "multi_record_groups": sum(g["record_count"] > 1 for g in group_rows),
        "years": sorted({r["year"] for r in records if r["year"]}),
        "premium_families": dict(sorted(Counter(r["family"] for r in records if r["catalog"] == "Premium").items())),
    }
    payload = {"schema_version": 1, "generated_from": "research/extractions/", "stats": stats,
               "source_inventory": inventory, "candidate_groups": group_rows, "records": records}
    (OUT / "catalog-index.json").write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    (OUT / "catalog-index-stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False))

if __name__ == "__main__":
    main()
