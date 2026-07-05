#!/usr/bin/env python3
"""
Generate docs/reference/recipes.md from the Bannerbound modpack's datapack JSON, rendering
each recipe as a Minecraft-style crafting grid (item icons in slots) plus supporting tables.

Item icons are extracted from the mod textures (MIT) and the vanilla 1.21.1 jar, and copied
into docs/assets/items/. See iconlib.py for the id -> texture resolution.

Usage (from repo root):
    python tools/gen_recipes.py
Config via env: BANNERBOUND_SRC (mod checkout), MC_JAR (path to 1.21.1.jar).
"""
import os, json, glob, html
from collections import Counter
import iconlib

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
ANTI = os.path.join(iconlib.MOD, "Antiquity/src/main/resources/data/bannerboundantiquity")
COREL = os.path.join(iconlib.MOD, "Core/src/main/resources/assets/bannerbound/lang/en_us.json")
ANTIL = os.path.join(iconlib.MOD, "Antiquity/src/main/resources/assets/bannerboundantiquity/lang/en_us.json")
OUT = os.path.join(REPO, "docs/reference/recipes.md")
ICON_DIR = os.path.join(REPO, "docs/assets/items")
os.makedirs(ICON_DIR, exist_ok=True)

# ---- names -----------------------------------------------------------------
lang = {}
for p in (COREL, ANTIL):
    with open(p, encoding="utf-8") as f:
        lang.update(json.load(f))

def pretty(idstr):
    return " ".join(w.capitalize() for w in idstr.split(":")[-1].replace("_", " ").split())

def name(idstr):
    if not idstr:
        return "?"
    if ":" not in idstr:
        idstr = "minecraft:" + idstr
    ns, path = idstr.split(":", 1)
    for pre in ("item", "block"):
        if f"{pre}.{ns}.{path}" in lang:
            return lang[f"{pre}.{ns}.{path}"]
    return pretty(idstr)

def langkey(k):
    return lang.get(k, k)

def secs(t):
    return f"{t / 20.0:g}s"

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def files(sub):
    return sorted(glob.glob(os.path.join(ANTI, sub, "*.json")))

def esc(s):
    return html.escape(str(s), quote=True)

# ---- icons -----------------------------------------------------------------
_icons = {}
def icon_file(idstr):
    if idstr in _icons:
        return _icons[idstr]
    r = iconlib.resolve_png(idstr)
    if not r:
        _icons[idstr] = None
        return None
    _ns, _path, data = r
    fn = iconlib.safe_name(idstr) + ".png"
    with open(os.path.join(ICON_DIR, fn), "wb") as f:
        f.write(data)
    _icons[idstr] = fn
    return fn

# ---- slot / grid / process HTML -------------------------------------------
def slot(idstr, count=1, cls=""):
    if not idstr:
        return '<span class="mc-slot"></span>'
    fn = icon_file(idstr)
    nm = name(idstr)
    ct = f'<i class="mc-ct">{count}</i>' if count and count != 1 else ''
    if not fn:
        return (f'<span class="mc-slot mc-slot--txt {cls}" title="{esc(nm)}">'
                f'{esc(nm.split()[0][:4])}{ct}</span>')
    return (f'<span class="mc-slot {cls}"><img src="../../assets/items/{fn}" alt="{esc(nm)}" '
            f'title="{esc(nm)}" loading="lazy">{ct}</span>')

def arrow():
    return '<span class="mc-arrow" aria-hidden="true"></span>'

def grid(cells, out_id, out_ct=1):
    """cells: up to 9 (id, count) or None, row-major."""
    inner = "".join(slot(*cells[i]) if i < len(cells) and cells[i] else slot(None)
                     for i in range(9))
    return (f'<span class="mc-craft"><span class="mc-grid">{inner}</span>'
            f'{arrow()}{slot(out_id, out_ct, "mc-slot--out")}</span>')

def process(inputs, station, out_id, out_ct=1):
    """inputs: list of (id, count). station: id or None."""
    ins = "".join(slot(i, c) for i, c in inputs)
    st = slot(station, 1, "mc-slot--machine") if station else ""
    return (f'<span class="mc-craft">{ins}{st}{arrow()}'
            f'{slot(out_id, out_ct, "mc-slot--out")}</span>')

def htable(headers, rows):
    h = "".join(f"<th>{esc(x)}</th>" for x in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<div class="mc-scroll"><table class="mc-recipes"><thead><tr>{h}</tr>'
            f'</thead><tbody>{body}</tbody></table></div>')

def mdtable(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)

def result_of(d):
    r = d.get("result", {})
    if isinstance(r, str):
        return r, 1
    return (r.get("id") or r.get("item")), r.get("count", 1)

def ing_pairs(ings):
    """[{item,count}] -> [(id, count)], tags -> ('#tag', count) sentinel handled by slot txt."""
    out = []
    for i in ings:
        if i.get("tag"):
            out.append((None, i.get("count", 1)))  # tag: render empty-ish; name in text col
        else:
            out.append((i.get("item") or i.get("id"), i.get("count", 1)))
    return out

def ing_text(ings):
    parts = []
    for i in ings:
        if i.get("tag"):
            nm = "any " + i["tag"].split(":")[-1].replace("_", " ")
        else:
            nm = name(i.get("item") or i.get("id") or "?")
        c = i.get("count", 1)
        parts.append(nm + (f" ×{c}" if c and c != 1 else ""))
    return esc(", ".join(parts))

def name_cell(idstr, count=1):
    ic = slot(idstr, 1, "mc-slot--inline")
    return f'<span class="mc-namecell">{ic}<span>{esc(name(idstr))}' + \
           (f' ×{count}' if count != 1 else '') + '</span></span>'

S = []  # (title, intro, html_or_md)

# ---- Crafting Stone --------------------------------------------------------
rows = []
for d in map(load, files("crafting_stone_recipes")):
    if "ingredients" not in d:
        continue
    out, c = result_of(d)
    ings = d["ingredients"]
    rows.append((name(out), name_cell(out, c), ing_text(ings),
                 grid(ing_pairs(ings), out, c)))
rows.sort(key=lambda r: r[0])
S.append(("Crafting Stone",
    "Stack the loose ingredients on a carved "
    "[Crafting Stone](../antiquity/knapping.md#using-the-crafting-stone) and sneak-right-click to knap "
    "them together. Order doesn't matter — the grid below just shows the ingredients.",
    htable(["Makes", "Ingredients", "Recipe"], [(r[1], r[2], r[3]) for r in rows])))

# ---- Inventory grid --------------------------------------------------------
rows = []
for d in map(load, files("recipe")):
    out, c = result_of(d)
    if "pattern" in d:
        key = d.get("key", {})
        cells = []
        for ch in ("".join(d["pattern"]).ljust(9))[:9]:
            k = key.get(ch)
            if not k:
                cells.append(None)
            else:
                cells.append((k.get("item") or k.get("id"), 1))
        ings = [{"item": (v.get("item") or v.get("id")), "count":
                 Counter("".join(d["pattern"]))[ch2]} for ch2, v in key.items()]
        vis = grid(cells, out, c)
        itxt = ing_text([{"item": (v.get("item") or v.get("id"))} for v in key.values()])
    elif "ingredients" in d:
        ings = d["ingredients"]
        vis = grid(ing_pairs(ings), out, c)
        itxt = ing_text(ings)
    else:
        continue
    rows.append((name(out), name_cell(out, c), itxt, vis))
rows.sort(key=lambda r: r[0])
S.append(("Inventory Crafting Grid",
    "Recipes made in the ordinary 2×2 (or crafting-table) grid — the bootstrap crafts of the age.",
    htable(["Makes", "Ingredients", "Recipe"], [(r[1], r[2], r[3]) for r in rows])))

# ---- Stone Anvil -----------------------------------------------------------
rows = []
for d in map(load, files("anvil_recipes")):
    out, c = result_of(d)
    ings = d.get("ingredients", [])
    rows.append((name(out), name_cell(out, c), ing_text(ings),
                 grid(ing_pairs(ings), out, c), d.get("strikes", "?")))
rows.sort(key=lambda r: r[0])
S.append(("Stone Anvil — cold-hammer forging",
    "Haft and forge cast parts into finished tools on the "
    "[Stone Anvil](../antiquity/metalworking.md#cold-hammer-forging). *Strikes* is the number of clean "
    "hits the timing minigame needs; land them for higher quality.",
    htable(["Forges", "Ingredients", "Recipe", "Strikes"], [(r[1], r[2], r[3], r[4]) for r in rows])))

# ---- Pottery ---------------------------------------------------------------
POTTERY = "bannerboundantiquity:pottery_slab"
rows = []
for d in map(load, files("pottery_recipes")):
    out, c = result_of(d)
    ings = d["ingredients"]
    rows.append((name(out), name_cell(out, c),
                 process(ing_pairs(ings), POTTERY, out, c), d.get("spins", "?")))
rows.sort(key=lambda r: r[0])
S.append(("Pottery Slab",
    "Shaping clay on the [Pottery Slab](../antiquity/pottery.md); *spins* is how many turns of the "
    "throwing minigame it takes. Fire the unfired result in a Kiln (below).",
    htable(["Shapes", "Recipe", "Spins"], [(r[1], r[2], r[3]) for r in rows])))

# ---- Kiln ------------------------------------------------------------------
KILN = "bannerboundantiquity:kiln"
rows = []
for d in map(load, files("kiln_recipes")):
    out, c = result_of(d)
    inp = d["ingredient"].get("item") or d["ingredient"].get("id")
    rows.append((name(out), name_cell(out, c), process([(inp, 1)], KILN, out, c),
                 secs(d.get("ticks", 0)), f"{int(d.get('chance', 1.0) * 100)}%"))
rows.sort(key=lambda r: r[0])
S.append(("Kiln — firing",
    "Baking clay, ceramics, and lime in the [Kiln](../antiquity/pottery.md#firing-the-kiln).",
    htable(["Fires into", "Recipe", "Time", "Yield"], [(r[1], r[2], r[3], r[4]) for r in rows])))

# ---- Bloomery --------------------------------------------------------------
BLOOM = "bannerboundantiquity:bloomery"
rows = []
for d in map(load, files("bloomery_recipes")):
    out, c = result_of(d)
    inp = d["ingredient"].get("item") or d["ingredient"].get("id")
    rows.append((name(out), name_cell(out, c), process([(inp, 1)], BLOOM, out, c),
                 secs(d.get("ticks", 0)), f"{int(d.get('chance', 1.0) * 100)}%"))
rows.sort(key=lambda r: r[0])
S.append(("Bloomery — smelting",
    "Straight smelting in the [Bloomery](../antiquity/metalworking.md#the-bloomery-your-first-furnace). "
    "To make bronze-age *parts*, melt ore in a crucible instead (see the metal chart below).",
    htable(["Smelts into", "Recipe", "Time", "Yield"], [(r[1], r[2], r[3], r[4]) for r in rows])))

# ---- Drying ----------------------------------------------------------------
RACK = "bannerboundantiquity:oak_drying_rack"
rows = []
for d in map(load, files("drying_recipes")):
    out, c = result_of(d)
    rows.append((name(out), name_cell(out, c), process([(d["input"], 1)], RACK, out, c),
                 secs(d.get("ticks", 0))))
rows.sort(key=lambda r: r[0])
S.append(("Drying Rack",
    "Air-drying on a [Drying Rack](../antiquity/cooking-and-food.md) — preserved food, leather, and "
    "thatch bundles.",
    htable(["Dries into", "Recipe", "Time"], [(r[1], r[2], r[3]) for r in rows])))

# ---- Stew ------------------------------------------------------------------
POT = "bannerboundantiquity:stone_cooking_pot"
rows = []
for d in map(load, files("stew_recipes")):
    nm = langkey(d["name"])
    ings = d["ingredients"]
    rows.append((nm, esc(nm), process(ing_pairs(ings), POT, "minecraft:mushroom_stew", 1),
                 ing_text(ings), d.get("servings", "?"), f"×{d.get('bonus', '?')}",
                 secs(d.get("cook_ticks", 0))))
rows.sort(key=lambda r: r[0])
S.append(("Cooking Pot — stews",
    "Simmering [stews](../antiquity/cooking-and-food.md) in a Stone Cooking Pot over a lit campfire. "
    "*Bonus* multiplies the food value of the ingredients; each pot yields several servings.",
    htable(["Stew", "Recipe", "Ingredients", "Servings", "Food bonus", "Cook time"],
           [(r[1], r[2], r[3], r[4], r[5], r[6]) for r in rows])))

# ---- Grog ------------------------------------------------------------------
TROUGH = "bannerboundantiquity:oak_fermentation_trough"
rows = []
for d in map(load, files("grog_recipes")):
    nm = langkey(d["name"])
    rows.append((nm, esc(nm), process([(d["input"], 1)], TROUGH, "minecraft:potion", 1),
                 name(d["input"]), d.get("servings", "?"), d.get("food_value", "?"),
                 secs(d.get("ferment_ticks", 0))))
rows.sort(key=lambda r: r[0])
S.append(("Fermentation Trough — grog",
    "[Brewing](../antiquity/brewing.md) grog from crushed fermentables.",
    htable(["Grog", "Recipe", "From", "Servings", "Food value", "Ferment time"],
           [(r[1], r[2], esc(r[3]), r[4], r[5], r[6]) for r in rows])))

# ---- Mortar ----------------------------------------------------------------
MORTAR = "bannerboundantiquity:mortar_and_pestle"
item_rows, dye_rows = [], []
for d in map(load, files("mortar_recipes")):
    ing = d.get("ingredient", {})
    ing_id = ing.get("item") or ing.get("id")
    if d.get("result_liquid"):
        color = d["result_liquid"].replace("_", " ").title()
        dye_rows.append((color, esc(color), name_cell(ing_id), esc(d.get("base_liquid") or "water")))
    elif "result_item" in d or "result" in d:
        r = d.get("result_item") or d.get("result")
        out = r.get("id") or r.get("item")
        item_rows.append((name(out), name_cell(out, r.get("count", 1)),
                          process([(ing_id, 1)], MORTAR, out, r.get("count", 1))))
item_rows.sort(key=lambda r: r[0]); dye_rows.sort(key=lambda r: r[0])
mtxt = ""
if item_rows:
    mtxt += "**Pastes, powders & poisons**\n\n" + \
        htable(["Grinds into", "Recipe"], [(r[1], r[2]) for r in item_rows]) + "\n\n"
if dye_rows:
    mtxt += "**Dyes & inks**\n\n" + \
        htable(["Dye / liquid", "From", "Base"], [(r[1], r[2], r[3]) for r in dye_rows])
S.append(("Mortar & Pestle",
    "Grinding at the [Mortar & Pestle](../antiquity/herbalism.md) — poisons, pastes, and dye liquids "
    "(dyes colour a liquid rather than yielding an item).", mtxt))

# ---- Fletching -------------------------------------------------------------
FLETCH = "bannerboundantiquity:fletching_station"
rows = []
for d in map(load, files("fletching_recipes")):
    out, c = result_of(d)
    ings = d["ingredients"]
    rows.append((name(out), name_cell(out, c), process(ing_pairs(ings), FLETCH, out, c),
                 ing_text(ings), d.get("stretches", "?")))
rows.sort(key=lambda r: r[0])
S.append(("Fletching Station",
    "Binding arrows and tackle at the [Fletching Station](../antiquity/fletching-and-archery.md). Every "
    "arrow mixes a **tip**, a **shaft**, and **fletching** — see the parts table below.",
    htable(["Makes", "Recipe", "Ingredients", "Stretches"],
           [(r[1], r[2], r[3], r[4]) for r in rows])))

# ---- Woodworking & Masonry (log/stone-cost outputs) ------------------------
wood = mdtable(["Output (of the worked wood)", "Log cost", "Yield"],
    sorted((pretty(d["variant"]), f"{d.get('log_cost', '?')} log", d.get("yield", 1))
           for d in map(load, files("carpentry_outputs"))))
asm_rows = []
for d in map(load, files("carpentry_assembly")):
    out = d["result"]
    asm_rows.append((name(out), name_cell(out, d.get("yield", 1)),
                     grid(ing_pairs(d["ingredients"]), out, d.get("yield", 1))))
asm_rows.sort(key=lambda r: r[0])
asm = htable(["Assembles", "Recipe"], [(r[1], r[2]) for r in asm_rows])
S.append(("Woodworking Table",
    "At the [Woodworking Table](../antiquity/woodworking.md): batch-saw plain outputs from logs of "
    "whichever wood you load (cost in logs), or assemble set recipes.",
    "**Sawn outputs** — made from logs of the loaded wood.\n\n" + wood +
    "\n\n**Assemblies**\n\n" + asm))

mason = mdtable(["Output", "Stone cost", "Yield"],
    sorted((pretty(d["variant"]), f"{d.get('base_cost', '?')} stone", d.get("yield", 1))
           for d in map(load, files("masonry_outputs"))))
S.append(("Mason's Bench",
    "Dressing stone at the [Mason's Bench](../antiquity/masonry.md); cost is in blocks of the base "
    "stone you load.", mason))

# ---- Knapping thresholds (data) -------------------------------------------
krows = sorted((name_cell(d["head"]), f"{d.get('percentage_standard', '?')}%",
                f"{d.get('percentage_fine', '?')}%") for d in map(load, files("knapping_shapes")))
S.append(("Knapping — tool-head shapes",
    "Heads knapped on the [Crafting Stone](../antiquity/knapping.md); the minigame grades each "
    "**Standard** or **Fine** by how accurately you strike.",
    htable(["Tool head", "Standard at", "Fine at"], krows)))

# ---- Metals, moulds, alloys (data) ----------------------------------------
mw = load(os.path.join(ANTI, "metalworking/definitions.json"))
mrows = sorted(((m.capitalize(), f"{v['melt_point']} °C", f"{v['mb_per_unit']} mB / piece")
                for m, v in mw["metals"].items()), key=lambda r: int(r[1].split()[0]))
prows = [(pretty(s), f"{mb} mB", f"{-(-mb // 50)} ore pieces")
         for s, mb in sorted(mw["molds"].items(), key=lambda kv: kv[1])]
alloy = mw["alloys"][0]["components"]
atxt = ", ".join(f"{k} {int(v['min'] * 100)}–{int(v['max'] * 100)}%" for k, v in alloy.items())
S.append(("Metals, moulds & alloys",
    "The numbers behind [casting and forging](../antiquity/metalworking.md). Each ore piece melts to "
    f"**50 mB**; **bronze** is alloyed in the crucible ({atxt}).",
    "**Metals**\n\n" + mdtable(["Metal", "Melts at", "Volume"], mrows) +
    "\n\n**Mould metal cost**\n\n" + mdtable(["Mould", "Metal needed", "Min. ore"], prows)))

# ---- Arrow parts (data + icons) -------------------------------------------
arows = []
for d in map(load, files("arrow_parts")):
    ing = d.get("ingredient", "")
    arows.append((d.get("slot", "?").title(), d.get("material", "?").title(),
                  name_cell(ing), d.get("damage", "?"), d.get("weight", "?"), d.get("accuracy", "?")))
arows.sort(key=lambda r: (r[0], r[1]))
S.append(("Arrow parts",
    "Every arrow at the [Fletching Station](../antiquity/fletching-and-archery.md) mixes a **tip**, a "
    "**shaft**, and **fletching**. Mix materials for the damage, weight, and accuracy you want.",
    htable(["Slot", "Material", "Item", "Damage", "Weight", "Accuracy"], arows)))

# ---- write -----------------------------------------------------------------
header = """---
title: Recipe Reference
description: Every Bannerbound crafting recipe as a visual grid, generated straight from the modpack's data so it always matches the game — knapping, Crafting Stone, woodworking, masonry, pottery, smelting, forging, cooking, brewing, and fletching.
tags:
  - reference
---

# Recipe Reference

<p class="bb-lead"><em>Every custom recipe in the Antiquity age, rendered as a crafting grid and pulled directly from the modpack's own data — exhaustive, and always matching the version you're playing. Hover any icon for its name; use Ctrl&#8202;+&#8202;F to jump to an item.</em></p>

!!! abstract "How to read the grids"

    Each recipe shows its **ingredients → result**. A machine icon in the middle (kiln, bloomery, pottery slab, cooking pot…) marks a station process rather than a hand-craft. Crafting Stone recipes are *shapeless* — ingredient positions don't matter. Timings are in seconds; **mB** (millibuckets) measure liquid metal, one ore piece = 50&nbsp;mB.

!!! note "Auto-generated"

    Built by `tools/gen_recipes.py` from the modpack source and item textures. If a recipe here disagrees with another page, this one is the source of truth — re-run the generator or report the mismatch.

"""

footer = """
## Where to next

- [Knapping & First Tools](../antiquity/knapping.md) — how the Crafting Stone and knapping minigames work.
- [Metalworking & Bronze](../antiquity/metalworking.md) — the full smelt → melt → cast → forge pipeline.
- [Research & Eras](../civilization/research-and-eras.md) — which research unlocks each craft.
- [Glossary](glossary.md) — terms used throughout the wiki.
"""

body = "\n".join(f"## {t}\n\n{intro}\n\n{tbl}\n" for t, intro, tbl in S)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(header + body + footer)

n_icons = sum(1 for v in _icons.values() if v)
print(f"Wrote {OUT}")
print(f"Sections: {len(S)}   Icons copied: {n_icons}   (unresolved: {sum(1 for v in _icons.values() if not v)})")
