#!/usr/bin/env python3
"""
Generate docs/reference/recipes.md straight from the Bannerbound modpack's datapack JSON.

The modpack ships every recipe as data JSON (crafting_stone_recipes, anvil_recipes,
kiln_recipes, ...). This script parses all of it, resolves item ids to display names via
the lang files, and writes a single comprehensive Recipe Reference page — so the page can
never drift from the game.

Usage (from the repo root):
    python tools/gen_recipes.py

By default it expects the mod source as a sibling checkout at ../Bannerbound. Override with:
    BANNERBOUND_SRC=/path/to/Bannerbound python tools/gen_recipes.py
"""
import os, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
MOD = os.environ.get("BANNERBOUND_SRC", os.path.join(REPO, "..", "Bannerbound"))
ANTI = os.path.join(MOD, "Antiquity/src/main/resources/data/bannerboundantiquity")
COREL = os.path.join(MOD, "Core/src/main/resources/assets/bannerbound/lang/en_us.json")
ANTIL = os.path.join(MOD, "Antiquity/src/main/resources/assets/bannerboundantiquity/lang/en_us.json")
OUT = os.path.join(REPO, "docs/reference/recipes.md")

if not os.path.isdir(ANTI):
    raise SystemExit(
        f"Mod source not found at {MOD!r}.\n"
        "Clone github.com/Nitsu430/Bannerbound next to this repo, or set BANNERBOUND_SRC."
    )

# ---- name resolution -------------------------------------------------------
lang = {}
for p in (COREL, ANTIL):
    with open(p, encoding="utf-8") as f:
        lang.update(json.load(f))

def pretty(idstr):
    """Fallback for vanilla items: minecraft:cooked_beef -> Cooked Beef"""
    path = idstr.split(":")[-1]
    return " ".join(w.capitalize() for w in path.replace("_", " ").split())

def name(idstr):
    if not idstr:
        return "?"
    if ":" not in idstr:
        idstr = "minecraft:" + idstr
    ns, path = idstr.split(":", 1)
    for pre in ("item", "block"):
        k = f"{pre}.{ns}.{path}"
        if k in lang:
            return lang[k]
    return pretty(idstr)

def langkey(k):
    return lang.get(k, k)

def secs(ticks):
    return f"{ticks / 20.0:g}s"

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def ing_list(ings):
    parts = []
    for i in ings:
        if i.get("tag"):
            nm = "#" + i["tag"].split(":")[-1].replace("_", " ").title()
        else:
            nm = name(i.get("item") or i.get("id") or "?")
        c = i.get("count", 1)
        parts.append(nm + (f" ×{c}" if c and c != 1 else ""))
    return ", ".join(parts)

def ing_single(x):
    if isinstance(x, str):
        return name(x)
    if isinstance(x, dict):
        if "item" in x:
            return name(x["item"])
        if "id" in x:
            return name(x["id"])
        if "tag" in x:
            return "#" + x["tag"].split(":")[-1].replace("_", " ").title()
    return "?"

def result_of(d):
    r = d.get("result", {})
    if isinstance(r, str):
        return name(r), 1
    return name(r.get("id") or r.get("item")), r.get("count", 1)

def qty(nm, c):
    return nm + (f" ×{c}" if c != 1 else "")

def tbl(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)

def files(sub):
    return sorted(glob.glob(os.path.join(ANTI, sub, "*.json")))

S = []  # (title, intro, table)

# ---- Knapping --------------------------------------------------------------
rows = sorted((name(d["head"]), f"{d.get('percentage_standard','?')}%", f"{d.get('percentage_fine','?')}%")
              for d in map(load, files("knapping_shapes")))
S.append(("Knapping (Crafting Stone shapes)",
    "Knapped tool heads and the timing thresholds that grade them **Standard** vs **Fine**. "
    "See [Knapping](../antiquity/knapping.md).",
    tbl(["Tool head", "Standard at", "Fine at"], rows)))

# ---- Crafting Stone --------------------------------------------------------
rows = []
for d in map(load, files("crafting_stone_recipes")):
    if "ingredients" not in d:
        continue
    out, c = result_of(d)
    rows.append((qty(out, c), ing_list(d["ingredients"])))
rows.sort()
S.append(("Crafting Stone",
    "Stack the loose ingredients on a carved "
    "[Crafting Stone](../antiquity/knapping.md#using-the-crafting-stone) and sneak-right-click to knap them.",
    tbl(["Makes", "From"], rows)))

# ---- Inventory grid --------------------------------------------------------
from collections import Counter
rows = []
for d in map(load, files("recipe")):
    if "ingredients" in d:
        ings = ing_list(d["ingredients"])
    elif "pattern" in d:
        cnt = Counter("".join(d["pattern"]).replace(" ", ""))
        key = d.get("key", {})
        ings = ", ".join(qty(ing_single(key.get(sym, {})), n) for sym, n in cnt.items())
    else:
        continue
    out, c = result_of(d)
    rows.append((qty(out, c), ings, "2×2 / grid"))
rows.sort()
S.append(("Inventory Crafting Grid",
    "Recipes made in the ordinary 2×2 (or crafting-table) grid — the bootstrap crafts of the age.",
    tbl(["Makes", "From", "Where"], rows)))

# ---- Woodworking -----------------------------------------------------------
wood = tbl(["Output (of the worked wood)", "Log cost", "Yield"],
    sorted((pretty(d["variant"]), f"{d.get('log_cost','?')} log", d.get("yield", 1))
           for d in map(load, files("carpentry_outputs"))))
asm = tbl(["Assembles", "From"],
    sorted((qty(name(d["result"]), d.get("yield", 1)), ing_list(d["ingredients"]))
           for d in map(load, files("carpentry_assembly"))))
S.append(("Woodworking Table",
    "Batch-sawing outputs and assembly recipes at the [Woodworking Table](../antiquity/woodworking.md). "
    "Simple outputs cost logs of whichever wood you load; assemblies combine set ingredients.",
    "**Sawn outputs**\n\n" + wood + "\n\n**Assemblies**\n\n" + asm))

# ---- Masonry ---------------------------------------------------------------
rows = sorted((pretty(d["variant"]), f"{d.get('base_cost','?')} stone", d.get("yield", 1))
              for d in map(load, files("masonry_outputs")))
S.append(("Mason's Bench",
    "Dressing stone at the [Mason's Bench](../antiquity/masonry.md). Cost is in blocks of the base stone you load.",
    tbl(["Output", "Stone cost", "Yield"], rows)))

# ---- Pottery ---------------------------------------------------------------
rows = []
for d in map(load, files("pottery_recipes")):
    out, c = result_of(d)
    rows.append((qty(out, c), ing_list(d["ingredients"]), d.get("spins", "?")))
rows.sort()
S.append(("Pottery Slab",
    "Shaping clay at the [Pottery Slab](../antiquity/pottery.md); each needs a number of spins of the minigame. "
    "Unfired ceramics are then hardened in the Kiln (below).",
    tbl(["Shapes", "From", "Spins"], rows)))

# ---- Kiln ------------------------------------------------------------------
rows = []
for d in map(load, files("kiln_recipes")):
    out, c = result_of(d)
    rows.append((qty(out, c), ing_single(d["ingredient"]), secs(d.get("ticks", 0)),
                 f"{int(d.get('chance', 1.0) * 100)}%"))
rows.sort()
S.append(("Kiln (firing)",
    "Baking clay, ceramics, and lime in the [Kiln](../antiquity/pottery.md#firing-the-kiln).",
    tbl(["Fires into", "From", "Time", "Yield"], rows)))

# ---- Bloomery --------------------------------------------------------------
rows = []
for d in map(load, files("bloomery_recipes")):
    out, c = result_of(d)
    rows.append((qty(out, c), ing_single(d["ingredient"]), secs(d.get("ticks", 0)),
                 f"{int(d.get('chance', 1.0) * 100)}%"))
rows.sort()
S.append(("Bloomery (smelting)",
    "Straight smelting in the [Bloomery](../antiquity/metalworking.md#the-bloomery-your-first-furnace). "
    "For bronze-age parts, melt ore in a crucible instead — see the metal chart below.",
    tbl(["Smelts into", "From", "Time", "Yield"], rows)))

# ---- Metals, moulds, alloys ------------------------------------------------
mw = load(os.path.join(ANTI, "metalworking/definitions.json"))
mrows = sorted(((m.capitalize(), f"{v['melt_point']} °C", f"{v['mb_per_unit']} mB/piece")
                for m, v in mw["metals"].items()), key=lambda r: int(r[1].split()[0]))
prows = [(pretty(shape), f"{mb} mB", f"{-(-mb // 50)} ore pieces")
         for shape, mb in sorted(mw["molds"].items(), key=lambda kv: kv[1])]
alloy = mw["alloys"][0]["components"]
alloytxt = ", ".join(f"{k} {int(v['min'] * 100)}–{int(v['max'] * 100)}%" for k, v in alloy.items())
S.append(("Metals, moulds & alloys",
    "The numbers behind [casting and forging](../antiquity/metalworking.md). Each ore piece is **50 mB**; "
    f"**bronze** is alloyed in the crucible ({alloytxt}).",
    "**Metals**\n\n" + tbl(["Metal", "Melts at", "Volume"], mrows) +
    "\n\n**Mould metal cost**\n\n" + tbl(["Mould", "Metal needed", "Min. ore"], prows)))

# ---- Anvil -----------------------------------------------------------------
rows = []
for d in map(load, files("anvil_recipes")):
    out, c = result_of(d)
    rows.append((out, ing_list(d.get("ingredients", [])), d.get("strikes", "?")))
rows.sort()
S.append(("Stone Anvil (cold-hammer forging)",
    "Hafting and forging cast parts into finished tools on the "
    "[Stone Anvil](../antiquity/metalworking.md#cold-hammer-forging). Strikes = clean hits the minigame needs.",
    tbl(["Forges", "From", "Strikes"], rows)))

# ---- Drying ----------------------------------------------------------------
rows = []
for d in map(load, files("drying_recipes")):
    out, c = result_of(d)
    rows.append((out, name(d["input"]), secs(d.get("ticks", 0))))
rows.sort()
S.append(("Drying Rack",
    "Air-drying on a [Drying Rack](../antiquity/cooking-and-food.md) — preserved food and thatch bundles.",
    tbl(["Dries into", "From", "Time"], rows)))

# ---- Stew ------------------------------------------------------------------
rows = sorted((langkey(d["name"]), ing_list(d["ingredients"]), d.get("servings", "?"),
               f"×{d.get('bonus', '?')}", secs(d.get("cook_ticks", 0)))
              for d in map(load, files("stew_recipes")))
S.append(("Cooking Pot (stews)",
    "Simmering [stews](../antiquity/cooking-and-food.md) in a Stone Cooking Pot over a lit campfire. "
    "*Bonus* multiplies the food value of the ingredients.",
    tbl(["Stew", "Ingredients", "Servings", "Food bonus", "Cook time"], rows)))

# ---- Grog ------------------------------------------------------------------
rows = sorted((langkey(d["name"]), name(d["input"]), d.get("servings", "?"),
               d.get("food_value", "?"), secs(d.get("ferment_ticks", 0)))
              for d in map(load, files("grog_recipes")))
S.append(("Fermentation Trough (grog)",
    "[Brewing](../antiquity/brewing.md) grog from crushed fermentables.",
    tbl(["Grog", "From", "Servings", "Food value", "Ferment time"], rows)))

# ---- Mortar ----------------------------------------------------------------
dye_rows, item_rows = [], []
for d in map(load, files("mortar_recipes")):
    ing = ing_single(d.get("ingredient", "?"))
    if d.get("result_liquid"):
        dye_rows.append((d["result_liquid"].replace("_", " ").title(), ing, d.get("base_liquid") or "water"))
    elif "result_item" in d or "result" in d:
        r = d.get("result_item") or d.get("result")
        item_rows.append((qty(name(r.get("id") or r.get("item")), r.get("count", 1)), ing))
dye_rows.sort(); item_rows.sort()
mtxt = ""
if item_rows:
    mtxt += "**Pastes, powders & poisons**\n\n" + tbl(["Grinds into", "From"], item_rows) + "\n\n"
if dye_rows:
    mtxt += "**Dyes & inks**\n\n" + tbl(["Dye / liquid", "From", "Base liquid"], dye_rows)
S.append(("Mortar & Pestle",
    "Grinding at the [Mortar & Pestle](../antiquity/herbalism.md) — poisons, pastes, and dye liquids.",
    mtxt))

# ---- Fletching -------------------------------------------------------------
fl = tbl(["Makes", "From", "Stretches"],
    sorted((qty(*result_of(d)), ing_list(d["ingredients"]), d.get("stretches", "?"))
           for d in map(load, files("fletching_recipes"))))
arows = sorted(((d.get("slot", "?").title(), d.get("material", "?").title(), name(d.get("ingredient", "")),
                 d.get("damage", "?"), d.get("weight", "?"), d.get("accuracy", "?"))
                for d in map(load, files("arrow_parts"))), key=lambda r: (r[0], r[1]))
ap = tbl(["Slot", "Material", "Item", "Damage", "Weight", "Accuracy"], arows)
S.append(("Fletching Station",
    "Binding arrows and tackle at the [Fletching Station](../antiquity/fletching-and-archery.md). "
    "Every arrow mixes a **tip**, a **shaft**, and **fletching** — mix and match for the stats you want.",
    "**Fletched items**\n\n" + fl + "\n\n**Arrow parts (tip / shaft / fletching stats)**\n\n" + ap))

# ---- write -----------------------------------------------------------------
header = """---
title: Recipe Reference
description: Every Bannerbound crafting recipe, generated straight from the modpack's data so it always matches the game — knapping, Crafting Stone, woodworking, masonry, pottery, smelting, forging, cooking, brewing, and fletching.
tags:
  - reference
---

# Recipe Reference

<p class="bb-lead"><em>Every custom recipe in the Antiquity age, pulled directly from the modpack's own data files — so this list is exhaustive and always matches the version you're playing. Use your browser's find (Ctrl&#8202;+&#8202;F) to jump to any item.</em></p>

!!! abstract "How to read this page"

    Recipes are grouped by the **station** that makes them. Timings are shown in seconds; **mB** (millibuckets) measure liquid metal, where one raw-ore piece melts to 50&nbsp;mB. For *how* each station works and its minigame, follow the link under each heading to the full guide. Vanilla item names are shown as they appear in-game.

!!! note "Auto-generated"

    This page is built by `tools/gen_recipes.py` from the modpack source. If a recipe here disagrees with another page, this one is the source of truth — please report the mismatch (or re-run the generator).

"""

footer = """
## Where to next

- [Knapping & First Tools](../antiquity/knapping.md) — how the Crafting Stone and knapping minigames work.
- [Metalworking & Bronze](../antiquity/metalworking.md) — the full smelt → melt → cast → forge pipeline.
- [Research & Eras](../civilization/research-and-eras.md) — which research unlocks each craft.
- [Glossary](glossary.md) — terms used throughout the wiki.
"""

body = "\n".join(f"## {t}\n\n{intro}\n\n{table}\n" for t, intro, table in S)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(header + body + footer)

print(f"Wrote {OUT} ({len(S)} sections)")
