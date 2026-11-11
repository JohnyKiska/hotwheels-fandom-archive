#!/usr/bin/env python3
"""Build provisional casting groups from the Mainline visual-review queue.

Collector # is used as a first-pass grouping key only. Multi-row groups are
provisionally treated as one casting unless physical evidence identifies a
structural difference. This script never promotes a hypothesis to a verified
casting and never edits the source queue.
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

VARIANT_SUFFIX = re.compile(
    r"\\s*\\((?:\\d+(?:st|nd|rd|th)\\s+Color|Super Treasure Hunt|Treasure Hunt)[^)]*\\)\\s*$",
    re.IGNORECASE,
)


def normalized_model(name: str) -> str:
    value = (name or "").strip()
    previous = None
    while value != previous:
        previous = value
        value = VARIANT_SUFFIX.sub("", value).strip()
    return re.sub(r"\\s+", " ", value).casefold()


def unique(values):
    return sorted({(v or "").strip() for v in values if (v or "").strip()}, key=str.casefold)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Source visual-review queue CSV")
    parser.add_argument("--output", required=True, help="Generated casting-groups CSV")
    args = parser.parse_args()

    with Path(args.input).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"Toy #", "Collector #", "Model Name", "Visual Review Status"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"Missing required columns: {', '.join(sorted(missing))}")
        rows = list(reader)

    groups = defaultdict(list)
    for row in rows:
        key = (row.get("Collector #") or "").strip()
        if key:
            groups[key].append(row)

    output_fields = [
        "Collector #", "Display Name", "Toy #s", "Source Row IDs",
        "Model Names", "Catalog Series", "Source Series", "Group Size",
        "Casting Identity Status", "Casting Identity Basis", "Review Flags",
        "User Visual Review Statuses", "Internet Photo Sources",
    ]
    output_rows = []
    for collector, members in sorted(groups.items(), key=lambda item: int(item[0]) if item[0].isdigit() else item[0]):
        names = unique(row.get("Model Name", "") for row in members)
        normalized_names = unique(normalized_model(row.get("Model Name", "")) for row in members)
        catalog_series = unique(row.get("Catalog Series", "") for row in members)
        source_series = unique(row.get("Series", "") for row in members)
        hunt_types = unique(row.get("Hunt Type", "") for row in members)
        distribution = unique(row.get("Distribution / Exclusive", "") for row in members)
        statuses = unique(row.get("Visual Review Status", "") for row in members)
        toy_codes = unique(row.get("Toy #", "") for row in members)
        row_ids = unique(row.get("Source Row ID", "") for row in members)
        photo_sources = unique(row.get("Internet Photo Source", "") for row in members)

        flags = []
        if len(members) == 1:
            flags.append("single_entry_no_comparison")
        if len(normalized_names) > 1:
            flags.append("model_name_conflict")
        if len(catalog_series) > 1:
            flags.append("catalog_series_variation")
        if len(source_series) > 1:
            flags.append("source_series_variation")
        if hunt_types:
            flags.append("hunt_or_special_release")
        if distribution:
            flags.append("distribution_exclusive_mix")
        if photo_sources:
            flags.append("photo_evidence_available")
        if any("wheel" in (row.get("Review Reason", "") or "").casefold() for row in members):
            flags.append("wheel_difference_note")

        if len(members) == 1:
            identity_status = "single_entry_no_comparison"
            basis = "Only one source row exists for this Collector #; no same-casting assumption is made."
        elif all(status == "user_confirmed_same_casting" for status in statuses):
            identity_status = "user_confirmed_same_casting"
            basis = "Every member row carries a user-confirmed physical casting comparison."
        else:
            identity_status = "provisional_same_casting"
            basis = "Default project rule: entries sharing a Collector # are provisionally grouped as one casting until structural evidence shows a difference. Color, tampo, wheels, finish, hunt status and distribution do not alone create a new casting."

        output_rows.append({
            "Collector #": collector,
            "Display Name": names[0] if names else "",
            "Toy #s": " | ".join(toy_codes),
            "Source Row IDs": " | ".join(row_ids),
            "Model Names": " | ".join(names),
            "Catalog Series": " | ".join(catalog_series),
            "Source Series": " | ".join(source_series),
            "Group Size": str(len(members)),
            "Casting Identity Status": identity_status,
            "Casting Identity Basis": basis,
            "Review Flags": " | ".join(flags),
            "User Visual Review Statuses": " | ".join(statuses),
            "Internet Photo Sources": " | ".join(photo_sources),
        })

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(output_rows)

    multi = sum(1 for row in output_rows if int(row["Group Size"]) > 1)
    provisional = sum(1 for row in output_rows if row["Casting Identity Status"] == "provisional_same_casting")
    confirmed = sum(1 for row in output_rows if row["Casting Identity Status"] == "user_confirmed_same_casting")
    print(f"Source rows: {len(rows)}; Collector groups: {len(output_rows)}; "
          f"multi-entry groups: {multi}; provisional: {provisional}; user-confirmed: {confirmed}")


if __name__ == "__main__":
    main()
