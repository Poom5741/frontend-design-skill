#!/usr/bin/env python3
"""ดึงโค้ด component จาก registry ที่ whitelist (shadcn/Magic UI) · MIT/Apache เท่านั้น

Sources (license ยืนยันแล้วใน references/component-index.md):
  - shadcn/ui  MIT    https://ui.shadcn.com/r/styles/new-york/<component>.json
  - Magic UI   MIT    https://magicui.design/r/<component>.json

Usage: python3 source-fetch.py <lib> <component>  → JSON to stdout
"""
import json, sys, urllib.request

REGISTRY = {
    "shadcn":  "https://ui.shadcn.com/r/styles/new-york/{component}.json",
    "magicui": "https://magicui.design/r/{component}.json",
}
UA = {"User-Agent": "bluebelt-dojo-sourcing/1.0"}


def fetch(lib: str, component: str) -> dict:
    if lib not in REGISTRY:
        sys.exit(f"unknown lib '{lib}' — valid: {sorted(REGISTRY)} (license whitelist เท่านั้น)")
    url = REGISTRY[lib].format(component=component)
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
    except Exception as e:
        sys.exit(f"fetch failed: {url}\n  {e}\n  (ถ้า registry เปลี่ยนรูปแบบ — แก้ REGISTRY map ด้านบน)")
    files = {f["path"]: f["content"] for f in data.get("files", [])}
    return {"lib": lib, "component": component,
            "registryDependencies": data.get("registryDependencies", []),
            "dependencies": data.get("dependencies", []), "files": files}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: source-fetch.py <shadcn|magicui> <component>")
    json.dump(fetch(sys.argv[1], sys.argv[2]), sys.stdout, ensure_ascii=False, indent=2)
