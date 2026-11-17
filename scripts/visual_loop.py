#!/usr/bin/env python3
"""FALLBACK: render html → screenshot ชุด (desktop+mobile) — ใช้เมื่อ harness browser capture ใช้ไม่ได้เท่านั้น

ต้องมี playwright + chromium (pip install playwright && python3 -m playwright install chromium)
และฟอนต์ไทย fonts-thai-tlwg-ttf (apt-get install)

Usage: visual_loop.py <page.html> <out_dir> <card_id>
Output: <out_dir>/manifest-playwright.json + png 4 ไฟล์ (viewport + full-page × desktop/mobile)
"""
import json, os, sys
from playwright.sync_api import sync_playwright


def capture(html_path: str, out_dir: str, card_id: str):
    os.makedirs(out_dir, exist_ok=True)
    manifest = {"card_id": card_id, "shots": [], "source": "playwright-fallback"}
    url = "file://" + os.path.abspath(html_path)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, vw, vh in [("desktop", 1440, 900), ("mobile", 390, 844)]:
            pg = b.new_page(viewport={"width": vw, "height": vh})
            pg.goto(url)
            pg.wait_for_timeout(2500)
            shot = os.path.join(out_dir, f"{card_id}-{name}.png")
            full = os.path.join(out_dir, f"{card_id}-{name}-full.png")
            pg.screenshot(path=shot)
            pg.screenshot(path=full, full_page=True)
            manifest["shots"].append({"viewport": name, "png": shot, "full": full})
            pg.close()
        b.close()
    mf = os.path.join(out_dir, "manifest-playwright.json")
    with open(mf, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("evidence(fallback):", mf)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage: visual_loop.py <page.html> <out_dir> <card-id>")
    capture(sys.argv[1], sys.argv[2], sys.argv[3])
