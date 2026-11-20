# Front-page image for Friday 20 November 2026 world news.
# Drawn with PIL shapes and text only: no photos, no network.
# Run: python3 make_image.py -> writes entry.png (1024x1024) next to this file.
import math
import os

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF_BOLD = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")

PAPER = (249, 245, 233)
INK = (17, 17, 21)
GREY = (62, 62, 70)
RED = (172, 30, 38)
NAVY = (20, 46, 94)
GOLD = (176, 128, 8)
TEAL = (0, 104, 104)
GREEN = (26, 114, 56)
PURPLE = (90, 44, 134)
ORANGE = (176, 76, 0)
CARD = (255, 253, 247)
EDGE = (38, 38, 46)
DARK = (20, 26, 46)

canvas = Image.new("RGB", (SIZE, SIZE), PAPER)
pen = ImageDraw.Draw(canvas)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap_lines(text, fnt, max_width):
    lines = []
    current = ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if pen.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_text_block(x, y, text, fnt, fill, max_width, gap=4):
    for line in wrap_lines(text, fnt, max_width):
        pen.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def kicker(x, y, label, colour):
    pen.rectangle([x, y, x + 10, y + 17], fill=colour)
    pen.text((x + 16, y - 1), label.upper(), font=font(SANS_BOLD, 14), fill=colour)
    return y + 25


def card(x0, y0, x1, y1, fill=CARD):
    pen.rectangle([x0, y0, x1, y1], fill=fill, outline=EDGE, width=2)


def icon_scales(x, y, colour):
    pen.line([x + 30, y + 2, x + 30, y + 42], fill=colour, width=4)
    pen.line([x + 6, y + 10, x + 54, y + 10], fill=colour, width=4)
    for sx in (x + 6, x + 54):
        pen.line([sx, y + 10, sx - 8, y + 26], fill=colour, width=2)
        pen.line([sx, y + 10, sx + 8, y + 26], fill=colour, width=2)
        pen.arc([sx - 10, y + 22, sx + 10, y + 38], 0, 180, fill=colour, width=3)
    pen.line([x + 18, y + 50, x + 42, y + 50], fill=colour, width=5)


def icon_chart_down(x, y, colour):
    pen.line([x + 4, y + 4, x + 4, y + 52], fill=colour, width=3)
    pen.line([x + 4, y + 52, x + 56, y + 52], fill=colour, width=3)
    pts = [(x + 8, y + 14), (x + 20, y + 24), (x + 30, y + 20), (x + 42, y + 36), (x + 54, y + 44)]
    pen.line(pts, fill=RED, width=4)
    pen.polygon([(x + 54, y + 44), (x + 46, y + 42), (x + 50, y + 50)], fill=RED)


def icon_tanker(x, y, colour):
    pen.polygon([(x + 4, y + 34), (x + 56, y + 34), (x + 48, y + 48), (x + 12, y + 48)], fill=colour)
    pen.rectangle([x + 12, y + 22, x + 30, y + 34], fill=colour)
    pen.rectangle([x + 34, y + 26, x + 46, y + 34], fill=colour)
    pen.line([x + 40, y + 26, x + 40, y + 12], fill=colour, width=3)
    pen.ellipse([x + 34, y + 4, x + 46, y + 14], outline=ORANGE, width=3)
    for wx in range(2, 56, 13):
        pen.arc([x + wx, y + 50, x + wx + 11, y + 60], 0, 180, fill=NAVY, width=2)


def icon_tower(x, y, colour):
    pen.rectangle([x + 18, y + 6, x + 42, y + 54], fill=colour)
    pen.polygon([(x + 14, y + 6), (x + 46, y + 6), (x + 30, y - 2)], fill=colour)
    for wy in (14, 24, 34, 44):
        for wx in (23, 32):
            pen.rectangle([x + wx, y + wy, x + wx + 5, y + wy + 6], fill=(255, 255, 255))
    pen.line([x + 52, y + 2, x + 40, y + 16], fill=RED, width=4)
    pen.ellipse([x + 36, y + 14, x + 44, y + 22], fill=RED)


def icon_cyclone(x, y, colour):
    for r, start in ((24, 20), (17, 140), (10, 260)):
        pen.arc([x + 30 - r, y + 30 - r, x + 30 + r, y + 30 + r], start, start + 230, fill=colour, width=4)
    pen.ellipse([x + 26, y + 26, x + 34, y + 34], fill=colour)


def icon_chip(x, y, colour):
    pen.rectangle([x + 14, y + 14, x + 46, y + 46], outline=colour, width=4)
    pen.rectangle([x + 24, y + 24, x + 36, y + 36], fill=colour)
    for p in (18, 28, 38):
        pen.line([x + p, y + 14, x + p, y + 5], fill=colour, width=3)
        pen.line([x + p, y + 46, x + p, y + 55], fill=colour, width=3)
        pen.line([x + 14, y + p, x + 5, y + p], fill=colour, width=3)
        pen.line([x + 46, y + p, x + 55, y + p], fill=colour, width=3)


def icon_drone(x, y, colour):
    pen.ellipse([x + 22, y + 24, x + 38, y + 38], fill=colour)
    for dx, dy in ((6, 8), (44, 8), (6, 44), (44, 44)):
        pen.ellipse([x + dx, y + dy, x + dx + 12, y + dy + 12], outline=colour, width=3)
        pen.line([x + dx + 6, y + dy + 6, x + 30, y + 31], fill=colour, width=2)


def icon_heart(x, y, colour):
    pen.ellipse([x + 8, y + 8, x + 30, y + 30], fill=colour)
    pen.ellipse([x + 30, y + 8, x + 52, y + 30], fill=colour)
    pen.polygon([(x + 10, y + 24), (x + 50, y + 24), (x + 30, y + 54)], fill=colour)
    pen.line([x + 14, y + 30, x + 24, y + 30], fill=(255, 255, 255), width=3)
    pen.line([x + 24, y + 30, x + 28, y + 22], fill=(255, 255, 255), width=3)
    pen.line([x + 28, y + 22, x + 32, y + 36], fill=(255, 255, 255), width=3)
    pen.line([x + 32, y + 36, x + 46, y + 30], fill=(255, 255, 255), width=3)


def icon_flags(x, y, colour):
    for i, c in enumerate((NAVY, RED, (56, 56, 150))):
        fx = x + i * 19
        pen.line([fx + 2, y + 4, fx + 2, y + 54], fill=INK, width=3)
        pen.rectangle([fx + 2, y + 4, fx + 18, y + 22], fill=c)


# ---------------- Masthead ----------------
pen.rectangle([0, 0, SIZE, 100], fill=INK)
pen.text((24, 6), "THE WORLD IN ONE DAY", font=font(SERIF_BOLD, 44), fill=(255, 255, 255))
pen.text((26, 58), "Friday  20 November 2026  —  World News Front Page", font=font(SANS_BOLD, 21), fill=(255, 208, 86))
pen.text((SIZE - 24, 10), "20 NOV", font=font(SANS_BOLD, 30), fill=(255, 255, 255), anchor="ra")
pen.text((SIZE - 24, 42), "2026", font=font(SANS_BOLD, 30), fill=(255, 208, 86), anchor="ra")
pen.text((SIZE - 24, 76), "FRIDAY", font=font(SANS, 13), fill=(198, 198, 208), anchor="ra")

# ---------------- Lead story: Kyiv strikes ----------------
LX0, LY0, LX1, LY1 = 14, 108, 1010, 334
card(LX0, LY0, LX1, LY1)
yy = kicker(LX0 + 16, LY0 + 10, "Lead story  ·  Kyiv, Ukraine  ·  Overnight Friday", RED)
pen.text((LX0 + 16, yy), "Russian missiles hit Kyiv again;", font=font(SERIF_BOLD, 33), fill=INK)
pen.text((LX0 + 16, yy + 39), "three Dnipro bridges damaged", font=font(SERIF_BOLD, 33), fill=INK)
draw_text_block(
    LX0 + 16, yy + 86,
    "Russia attacked Kyiv with ballistic missiles overnight on Friday 20 November, causing explosions and fires and damaging three bridges over the Dnipro. A drone struck a hospital in Kharkiv, injuring four. It followed Thursday's strikes that killed one person and damaged a cathedral and two embassies, a day after Ukraine hit the Crimea Bridge for the third time in four days.",
    font(SANS, 16), GREY, 620, gap=4)
# Lead visual: night skyline over the river
vx = LX0 + 662
pen.rectangle([vx, LY0 + 44, vx + 312, LY0 + 132], fill=(24, 32, 58))
for bx, bh in ((8, 46), (44, 66), (86, 40), (122, 58), (162, 44), (200, 70), (244, 50)):
    pen.rectangle([vx + bx, LY0 + 132 - bh, vx + bx + 30, LY0 + 132], fill=(52, 66, 104))
pen.ellipse([vx + 268, LY0 + 54, vx + 292, LY0 + 78], fill=(255, 208, 86))
pen.line([vx + 4, LY0 + 140, vx + 308, LY0 + 140], fill=GOLD, width=4)
pen.line([vx + 62, LY0 + 140, vx + 62, LY0 + 156], fill=GOLD, width=3)
pen.line([vx + 250, LY0 + 140, vx + 250, LY0 + 156], fill=GOLD, width=3)
for wx in range(vx + 6, vx + 302, 22):
    pen.arc([wx, LY0 + 160, wx + 16, LY0 + 172], 0, 180, fill=NAVY, width=2)
pen.text((vx + 156, LY0 + 178), "Kyiv · Dnipro bridges · 20 Nov", font=font(SANS, 13), fill=GREY, anchor="ma")
stats = [("3 bridges", "damaged in Kyiv"), ("4 injured", "Kharkiv hospital"), ("3rd strike", "on Crimea Bridge")]
for i, (big, small) in enumerate(stats):
    sx = vx + i * 106
    pen.rectangle([sx, LY0 + 190, sx + 100, LY0 + 206], fill=RED if i == 0 else NAVY)
    pen.text((sx + 50, LY0 + 198), big, font=font(SANS_BOLD, 13), fill=(255, 255, 255), anchor="mm")
    pen.text((sx + 50, LY0 + 210), small, font=font(SANS, 11), fill=GREY, anchor="ma")

# ---------------- Markets band ----------------
MY0, MY1 = 342, 428
pen.rectangle([14, MY0, 1010, MY1], fill=DARK, outline=EDGE, width=2)
pen.rectangle([14, MY0, 26, MY1], fill=(255, 208, 86))
pen.text((38, MY0 + 7), "MARKETS  ·  Friday 20 Nov — AI sell-off deepens", font=font(SANS_BOLD, 18), fill=(255, 208, 86))
draw_text_block(38, MY0 + 31,
                "Asia fell hard Friday as doubt over AI spending spread: Taiwan plunged over 2,200 points, Japan's Nikkei fell 4.8%, South Korea halted selling and SoftBank dropped over 16%. The S&P 500 fell about 2% for a fifth straight day; gold slipped below $3,600.",
                font(SANS, 13), (232, 234, 244), 950, gap=3)
nums = [("TAIWAN", "−2,200 pts"), ("NIKKEI", "−4.8%"), ("SOFTBANK", "−16%"), ("S&P 500", "−2% · 5 days"), ("GOLD", "< $3,600"), ("BRENT OIL", "$90.05")]
nx = 38
for label, value in nums:
    pen.text((nx, MY1 - 26), label, font=font(SANS_BOLD, 10), fill=(160, 170, 200))
    pen.text((nx, MY1 - 14), value, font=font(SANS_BOLD, 13), fill=(255, 120, 120) if ("−" in value or "<" in value) else (255, 255, 255))
    nx += 162

# ---------------- Grid: 9 panels ----------------
COLS_X = [14, 346, 678]
COL_W = 332
ROWS_Y = [436, 610, 784]
ROW_H = 166

panels = [
    dict(colour=NAVY, kick="Justice · The Hague", head="World court: Myanmar committed genocide",
         body="The ICJ ruled 9–6 that Myanmar committed genocide against the Rohingya — its first such finding against a state. The UN chief welcomed it Friday; Myanmar must help refugees return and file a compensation plan within two years.",
         icon="scales"),
    dict(colour=PURPLE, kick="Summit · Shenzhen, China", head="After the first Trump–Xi–Putin summit",
         body="APEC adopted the Shenzhen Outlook on trade, data and AI risks after Thursday's first three-way meeting. Commentators judged Xi and Putin the winners; Trump flew home Friday.",
         icon="flags"),
    dict(colour=NAVY, kick="Economy · New York", head="Anthropic's record IPO meets doubt",
         body="Claude maker Anthropic closed its Nasdaq debut 17% up near $97 after raising a record $81.3 billion at about a $1.5 trillion valuation. Friday it was set to join major indexes — yet AI shares kept falling.",
         icon="chart"),
    dict(colour=ORANGE, kick="War · Iran / Hormuz", head="Iran war: Senate backs Trump; Hormuz burns",
         body="The US Senate rejected limits on Trump's war powers 51–48. Trump said Friday he will decide the next step after New Year as Israel urges more bombing. Cost so far: over $48 billion.",
         icon="tanker"),
    dict(colour=RED, kick="War · Riyadh, Saudi Arabia", head="Houthi missile damages Riyadh tower",
         body="Saudi authorities confirmed Friday that a Houthi attack damaged the Public Investment Fund tower in Riyadh's financial district. The Houthis claimed four targets in Saudi Arabia. No injuries were reported.",
         icon="tower"),
    dict(colour=TEAL, kick="Climate · India / Antalya", head="Cyclone Akvan nears India; COP31 stuck",
         body="Odisha and Andhra Pradesh raised alerts Friday as Cyclone Akvan neared India's east coast; 10 trains were cancelled. At COP31 in Antalya, talks stayed split over fossil-fuel phase-out and climate finance.",
         icon="cyclone"),
    dict(colour=NAVY, kick="Tech · Chips and AI", head="880,000 AI chips for China; critical patch",
         body="A US House panel revealed Commerce approved nearly 880,000 advanced AI chips for Chinese firms including Alibaba and Tencent. Broadcom urged instant updates for a critical VMware flaw. Gemini gained Mac control.",
         icon="chip"),
    dict(colour=GREEN, kick="Aid · UK / Ukraine / Europe", head="UK pledges 1,000+ drones for Ukraine",
         body="Britain pledged over 1,000 long-range drones in a £260 million package announced by Andy Burnham in Berlin on Friday. Across Europe, a youth action day linked living costs, housing and education.",
         icon="drone"),
    dict(colour=GREEN, kick="Health · Culture · Sport", head="Kenya's last Ebola patient goes home",
         body="Kenya discharged its last Ebola patient, 37 days after its first case. GTA VI entered day two after a record launch. 'The Year of the Ghost' won Best Film at IDFA; Côte d'Ivoire drew late with Gambia.",
         icon="heart"),
]

ICONS = {
    "scales": icon_scales, "chart": icon_chart_down, "tanker": icon_tanker,
    "tower": icon_tower, "cyclone": icon_cyclone, "chip": icon_chip,
    "drone": icon_drone, "heart": icon_heart, "flags": icon_flags,
}

for idx, p in enumerate(panels):
    x0 = COLS_X[idx % 3]
    y0 = ROWS_Y[idx // 3]
    x1, y1 = x0 + COL_W, y0 + ROW_H
    card(x0, y0, x1, y1)
    yy = kicker(x0 + 12, y0 + 9, p["kick"], p["colour"])
    ICONS[p["icon"]](x1 - 68, y0 + 28, p["colour"])
    for line in wrap_lines(p["head"], font(SERIF_BOLD, 19), COL_W - 88):
        pen.text((x0 + 12, yy), line, font=font(SERIF_BOLD, 19), fill=INK)
        yy += 24
    yy += 1
    draw_text_block(x0 + 12, yy, p["body"], font(SANS, 12), GREY, COL_W - 24, gap=3)

# ---------------- Ticker footer ----------------
pen.rectangle([0, 958, SIZE, SIZE], fill=INK)
pen.text((14, 962), "ALSO FRIDAY 20 NOV:", font=font(SANS_BOLD, 12), fill=(255, 208, 86))
ticker = ("Trump pardons baseball star Pete Rose posthumously  ·  US sanctions Comancheros and 'Ndrangheta  ·  "
          "13,000 protest in Tokyo against Takaichi  ·  Samsung names Won-Joon Choi mobile chief  ·  "
          "Meta rethinks 2030 net-zero goal  ·  Amazon in $7bn talks for AI startup Decart  ·  "
          "Fire at Muhammad Yunus's ancestral home in Bangladesh  ·  India–Japan 2+2 talks  ·  "
          "Cincinnati Zoo's Fiona the hippo dies  ·  UN: 1m Afghan children face deadly malnutrition")
draw_text_block(14, 978, ticker, font(SANS, 11), (228, 228, 232), SIZE - 28, gap=2)

out_path = os.path.join(HERE, "entry.png")
canvas.save(out_path, optimize=True)
print("wrote", out_path, canvas.size, os.path.getsize(out_path), "bytes")
