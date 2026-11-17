# Component Index — แหล่งประกอบหน้า frontend ที่คัดลิขสิทธิ์แล้ว (v1, 2026-11-16)

> กฎ: ใช้เฉพาะแหล่ง license **MIT / ISC / Apache-2.0** (whitelist) · ตัวที่ license ไม่ชัวร์อยู่ tier "CONDITIONAL" ห้ามใช้ก่อนตรวจ
> วิธีใช้: เลือก design direction ก่อน (จาก popular-web-designs templates) → เลือก library จากตารางที่เข้า direction → harmonize ทุก component ลง token system เดียว → ประกอบ

## Tier A — Foundation (ตัวโครง UI, license ยืนยันแล้ว)

| แหล่ง | License | ★ | ลักษณะ | เหมาะเมื่อ |
|---|---|---|---|---|
| shadcn/ui (github.com/shadcn-ui/ui) | MIT | 128k | Tailwind · copy-paste · อุตสาหกรรมมาตรฐาน | พื้นฐาน default ของเกือบทุก brief |
| Radix UI (primitives) | MIT | 19.5k | headless primitives (a11y สมบูรณ์) | ต้องการ behavior แบบไม่ผูก skin |
| Headless UI | MIT | 28.8k | headless สำหรับ Tailwind | เสริม shadcn เมื่อ shadcn ไม่มีชิ้น |
| daisyUI | MIT | 42.9k | class-based, อิสระจาก React | งาน static HTML/ไม่ต้องการ framework |
| Mantine | MIT | 32k | ชุดใหญ่ hooks เยอะ | dashboard/แอปซีเรียส |
| Chakra UI | MIT | 40.7k | ใช้งานง่าย | rapid prototyping |

## Tier B — สาย stunning/unique (สำหรับ landing ที่ต้อง "ไม่ slop")

| แหล่ง | License | ★ | ลักษณะ |
|---|---|---|---|
| **Magic UI** (magicuidesign/magicui) | MIT | 23.3k | animated components — ตัวสำคัญสุดของ "stunning look" |
| Flowbite (themesberg/flowbite) | MIT | 9.4k | ครบทั้ง HTML ล้วน + React |
| HeroUI (เดิม NextUI) | Apache-2.0 | 31.2k | สวย modern พร้อมใช้ |
| Tremor | Apache-2.0 | 3.7k | dashboard/chart blocks |

## Tier C — Icons / Data / Motion (ชิ้นส่วนเสริม)

| แหล่ง | License | ใช้ทำ |
|---|---|---|
| Heroicons (tailwindlabs) | MIT | icons พื้นฐาน |
| Lucide | ISC | icons ชุดใหญ่ |
| Recharts | MIT | charts |
| visx (airbnb) | MIT | charts ละเอียด/custom |
| Motion (เดิม Framer Motion) | MIT | animation |

## Tier D — Design direction vocab (ไม่ใช่ component — คือ "รส" ทั้งระบบ)

- skill `popular-web-designs` — 54 design systems (Stripe, Linear, Vercel, Apple, SpaceX...) เลือก 1 อันเป็นโทนก่อน harmonize
- skill `frontend-design` — doctrine กัน slop + slop diagnostic checklist

## Tier CONDITIONAL — ยังไม่ยืนยัน ห้ามใช้จนตรวจ license เอง

| แหล่ง | เหตุที่ยังรอ |
|---|---|
| Aceternity UI | มี free tier แต่เงื่อนไข attribution/pro — ตรวจก่อนใช้ |
| Origin UI | repo slug ยังไม่ยืนยัน (origin-space/originui 404) |
| Preline UI | repo ไม่เจอ — license ไม่ยืนยัน |
| Tailwind UI / Untitled UI | มีค่าใช้จ่าย — ออกนอก whitelist |

## หลัก harmonization (กำแพงโกเธสเตอร์)

1. เลือก token system จาก direction ก่อน (palette · radius · spacing · type) — **ล็อกก่อนเลือก component**
2. ทุก component ที่ดึงมาต้อง re-skin ลง tokens — ห้ามใช้สไตล์เดิมของ library ค้าง
3. จำกัด 1 foundation library ต่อหน้า (ผสม Magic UI เข้า shadcn ได้เพราะทั้งคู่ Tailwind-based — ผสม Mantine เข้า shadcn ไม่ได้)
4. ห้ามใช้ component จาก 2 foundation ที่ design system ต่างเชื้อชาติ

## Visual Loop (กติกาตามคำตัดสินของ Poom 2026-11-16)

```
สร้าง → render → screenshot → วิจารณ์ใส่ slop checklist (frontend-design) → แก้
→ ทำซ้ำ ให้ดีที่สุดในรอบตัวเอง (เก็บทุกเวอร์ชัน v1/v2/v3)
→ ส่งเวอร์ชันดีสุดให้ผู้ใช้ → ผู้ใช้พิจารณา
→ "ชอบอันนี้" = ล็อก · "ยังไม่ชอบ + บอกจุด" = วนรอบถัดไป (ไม่จำกัดรอบ)
ตาของผู้ใช้คือ taste gate สุดท้าย — agent ไม่มีสิทธิ์ตัดสินว่า "สวยพอ" เอง
```
