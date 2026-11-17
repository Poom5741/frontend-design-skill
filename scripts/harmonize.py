#!/usr/bin/env python3
"""ฉีด token system เข้า component code (shadcn CSS-var scheme) + รายงาน hex ค้าง

Usage: harmonize.py <tokens.json> <components.json>  → JSON to stdout
  components.json = output ของ source-fetch.py (มี key "files")
Output: {"files": {...}, "leftover_hex": [{"path","hex"}...]}

leftover_hex ≠ error — แต่ห้ามซ่อน: ขั้น assemble ต้องแก้มือจนหมดตาม protocol ใน SKILL.md
"""
import json, re, sys


def css_vars(tokens: dict) -> str:
    c = tokens["colors"]
    lines = [f"  --background: {c['background']};", f"  --foreground: {c['foreground']};",
             f"  --primary: {c['primary']};", f"  --primary-foreground: {c['primary-foreground']};",
             f"  --muted: {c['muted']};", f"  --muted-foreground: {c['muted-foreground']};",
             f"  --border: {c['border']};", f"  --radius: {tokens['radius']['base']};"]
    return ":root {\n" + "\n".join(lines) + "\n}\n"


def harmonize(files: dict, tokens: dict) -> dict:
    block = css_vars(tokens)
    token_hexes = {v.upper() for v in tokens["colors"].values()}
    out, leftover = {}, []
    for path, code in files.items():
        if "<html" in code or (":root" in code and "--background" in code):
            code = re.sub(r":root\s*\{[^}]*\}", block.strip(), code, count=1) if ":root" in code \
                else code.replace("<style>", "<style>\n" + block, 1)
        else:
            code = block + "\n" + code
        hexes = {h.upper() for h in re.findall(r"#[0-9a-fA-F]{6}\b", code)} - token_hexes
        if hexes:
            leftover.append({"path": path, "hex": sorted(hexes)})
        out[path] = code
    return {"files": out, "leftover_hex": leftover}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: harmonize.py <tokens.json> <components.json>")
    tokens = json.load(open(sys.argv[1], encoding="utf-8"))
    data = json.load(open(sys.argv[2], encoding="utf-8"))
    json.dump(harmonize(data["files"], tokens), sys.stdout, ensure_ascii=False, indent=2)
