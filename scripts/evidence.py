#!/usr/bin/env python3
"""รวมภาพที่ capture ด้วย harness browser tools เป็น evidence pack ผูก acceptance criteria

Usage: evidence.py <out_dir> <card_id> <criteria.json>
  criteria.json = [{"id":"AC1","text":"...","shot":"AC1.png","result":"pass|fail|unverified"}]
  (shot paths สัมพัทธ์กับ out_dir — ภาพถ่ายโดย agent ผ่าน browser capture ก่อนเรียกสคริปต์นี้)

Output: <out_dir>/manifest.json + ตรวจว่าไฟล์ภาพที่อ้างมีจริงครบ
"""
import json, os, sys


def pack(out_dir: str, card_id: str, criteria: list):
    missing = []
    entries = []
    for c in criteria:
        p = os.path.join(out_dir, c["shot"])
        if not os.path.isfile(p):
            missing.append(c["shot"])
        entries.append({"id": c["id"], "text": c["text"],
                        "shot": os.path.abspath(p), "result": c["result"]})
    pack = {"card_id": card_id,
            "generated_by": "harness-browser-capture",
            "evidence": entries}
    mf = os.path.join(out_dir, "manifest.json")
    with open(mf, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=2)
    if missing:
        sys.exit(f"evidence pack INCOMPLETE — ภาพไม่มีจริง: {missing}")
    print("evidence:", mf)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage: evidence.py <out_dir> <card_id> <criteria.json>")
    pack(sys.argv[1], sys.argv[2], json.load(open(sys.argv[3], encoding="utf-8")))
