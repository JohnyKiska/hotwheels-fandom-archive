#!/usr/bin/env python3
"""Download a bounded image-review batch from the curated CSV queue."""
import csv
import hashlib
import os
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "database/pilot/pro-racing-1-43-image-review.csv"
OUT = ROOT / "database/pilot/assets/pro-racing-1-43"
MANIFEST = OUT / "MANIFEST.csv"
LIMIT = int(os.environ.get("IMAGE_LIMIT", "10"))
MAX_BYTES = 12 * 1024 * 1024
ALLOWED_HOSTS = {"static.wikia.nocookie.net"}

def safe_name(value):
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._")
    return value[:100] or "image"

OUT.mkdir(parents=True, exist_ok=True)
rows = list(csv.DictReader(QUEUE.open(encoding="utf-8-sig", newline="")))
rows = [r for r in rows if r.get("visual_inspection_status") == "not_inspected"][:LIMIT]
manifest_rows = []
for row in rows:
    idx = int(row["gallery_item_index"])
    url = row["image_url"]
    host = urlparse(url).hostname
    filename = f"{idx:03d}_{safe_name(row['file_name'])}"
    record = {
        "gallery_item_index": idx,
        "file_name": row["file_name"],
        "local_file": "",
        "source_url": url,
        "content_type": "",
        "bytes": 0,
        "sha256": "",
        "download_status": "failed",
        "error": "",
    }
    try:
        if host not in ALLOWED_HOSTS:
            raise ValueError(f"Blocked host: {host}")
        req = urllib.request.Request(url, headers={"User-Agent": "HW-Catalog-Image-Archive/1.0"})
        with urllib.request.urlopen(req, timeout=45) as response:
            content_type = response.headers.get_content_type()
            if not content_type.startswith("image/"):
                raise ValueError(f"Unexpected content type: {content_type}")
            data = response.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError(f"Image exceeds {MAX_BYTES} bytes")
        if not data:
            raise ValueError("Empty response")
        ext = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp", "image/gif": ".gif"}.get(content_type)
        if not ext:
            raise ValueError(f"Unsupported image type: {content_type}")
        target = OUT / (Path(filename).stem + ext)
        target.write_bytes(data)
        record.update(local_file=str(target.relative_to(ROOT)), content_type=content_type,
                      bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                      download_status="downloaded")
    except Exception as exc:
        record["error"] = str(exc)[:300]
    manifest_rows.append(record)
    print(f"{idx}: {record['download_status']} {record['local_file'] or record['error']}")

with MANIFEST.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(manifest_rows[0].keys()) if manifest_rows else
        ["gallery_item_index","file_name","local_file","source_url","content_type","bytes","sha256","download_status","error"])
    writer.writeheader()
    writer.writerows(manifest_rows)

success = sum(r["download_status"] == "downloaded" for r in manifest_rows)
print(f"Downloaded {success}/{len(manifest_rows)} images.")
if not manifest_rows or success == 0:
    sys.exit(1)
