---
title: Optional Mods
description: The supported add-on mods — JEI, Jade, Create, Iris + Sodium, and Pandas Falling Trees — what each one adds to Bannerbound and why you might want it.
---

# Optional Mods

<p class="bb-lead"><em>Bannerbound runs perfectly on its own two mods. But a handful of well-loved companions make the age of stone easier to read, easier to learn, and a good deal prettier — and Bannerbound is built to greet each of them with real integration, not just tolerance.</em></p>

!!! abstract "The short version"
    Every mod on this page is **optional** — install none of them and the pack still plays start to
    finish. But **JEI** teaches you *how* to make things, **Jade** tells you *what* you're looking at,
    **Create** unlocks the animated **Hold [W] to Ponder** tutorials, **Iris + Sodium** bring shaders
    and frame-rate, and **Pandas Falling Trees** makes your foresters chop like a real player. Grab
    the ones that suit you and drop them in your `mods` folder — see [Installation](../getting-started/installation.md).

## At a glance

Bannerbound declares each of these as a *soft* dependency: if it's present, the matching integration
switches on; if it's absent, nothing breaks and no errors appear. Match the version and put each mod on
the side (client, server, or both) it actually runs on.

| Mod | Version | Runs on | What it adds |
| --- | --- | --- | --- |
| **JEI** (Just Enough Items) | 19 or newer | :material-monitor: Client | Searchable recipe viewer, with full Bannerbound station integration |
| **Jade** | 15.8 or newer | :material-monitor: Client | "What am I looking at" HUD showing block & entity state |
| **Create** | 0.5 or newer | :material-monitor: Client | Powers the **Hold [W] to Ponder** animated guide scenes |
| **Iris** + **Sodium** | Iris 1.8.12, Sodium 0.6.13 | :material-monitor: Client | Shader support and a large performance boost |
| **Pandas Falling Trees** | any recent build | :material-server: Client **&** server | Natural whole-tree felling for citizen foresters |

!!! tip "On a server?"
    JEI, Jade, Create, Iris, and Sodium are **client-side** — each player installs the ones they like,
    and the server never needs them. The single exception is **Pandas Falling Trees**: it runs on
    **both sides**, so if you want your foresters to use it, it has to be installed on the server *and*
    on every client that connects.

---

## JEI — the recipe viewer

**JEI** (Just Enough Items) is the searchable recipe book that overlays your inventory: type an item's
name to find it, then click it to see every way to **make** it (:material-arrow-left-bold: recipes) or
**use** it (:material-arrow-right-bold: uses). It's the single most useful add-on for learning
Bannerbound, because Antiquity crafts almost nothing in a vanilla grid — and Bannerbound ships a full
JEI plugin so all of its unusual stations show up as proper, browsable recipe categories.

### Custom station categories

Look up any Antiquity item and JEI sends you to the right station, laid out with input slots, the
output, and a short plain-language **note** telling you exactly how the interaction works.

| JEI category | Station it covers | What its note explains |
| --- | --- | --- |
| **Crafting Stone** | [Crafting Stone](../antiquity/knapping.md) | Place the loose ingredients on the stone in any order |
| **Fletching Station** | [Fletching Station](../antiquity/fletching-and-archery.md) | Commit the pile, then finish the stretch-release minigame |
| **Pottery Slab** | [Pottery Slab](../antiquity/pottery.md) | Place clay, pick the output, then complete the spin minigame |
| **Bloomery Smelting** | [Bloomery](../antiquity/metalworking.md) | The smelt time and expected yield |
| **Kiln Firing** | [Kiln](../antiquity/pottery.md) | The firing time and expected yield |
| **Drying Rack** | [Drying Rack](../antiquity/cooking-and-food.md) | How long the item takes to dry |
| **Mortar and Pestle** | [Mortar & Pestle](../antiquity/herbalism.md) | Add water and a grindable ingredient, then work the pestle |
| **Woodworking** | [Woodworking Table](../antiquity/woodworking.md) | How many logs to add and how many items the sawing minigame yields |
| **Crucible Casting** | [Crucible + moulds](../antiquity/metalworking.md) | Melt ore in a crucible, heat it in a Bloomery, pour into a fired mould |
| **Cold-Hammer Forging** | [Stone Anvil](../antiquity/metalworking.md) | How many hammer strikes — and that the timing minigame sets the tool's quality |

!!! info "World Interactions — a category unique to Bannerbound"
    Antiquity is full of things you do by **right-clicking the world** rather than at a bench: knapping
    gravel into flint on a stone surface, cutting plant fiber from grass, chopping firewood on a stump,
    spear-fishing, lighting a campfire with fire sticks, fertilizing crops with dung, and dozens more.
    JEI gathers every one of these into a **World Interactions** category. Look up flint, a blade, a
    spear, or a mud brick and you'll find the exact right-click that produces it, described step by
    step — the fastest way to learn the moves that have no crafting grid at all.

### The info tab

Many blocks and tools also carry an **info page** — the :material-information: tab in JEI. It's a
paragraph of guidance written for that exact item: what the [Crucible](../antiquity/metalworking.md)
does, how the Bellows keeps a smelt hot, what a Bone Knife is for, how Salt preserves food. When you
pull up an item and aren't sure where to even begin, the info tab is the place to start.

### It only shows what you've discovered

Bannerbound's JEI plugin is **research-aware**. Items and recipes you haven't unlocked yet are quietly
kept out of the list, so browsing JEI never spoils your [tech tree](../civilization/research-and-eras.md) —
you see what you *can* make now, and new entries appear as your civilization learns. Anything whose
result you already know how to make always stays visible, so your starting tools and their recipes are
never hidden from you.

!!! tip "Want to see everything anyway?"
    There's a config toggle that reveals not-yet-discovered items and recipes in JEI — handy for
    planning a long game or writing a guide. Leave it off for a first, unspoiled playthrough; flip it
    on when you'd rather see the whole map of what's ahead.

---

## Jade — what am I looking at

**Jade** paints a small tooltip at the top of your screen naming whatever block or entity your crosshair
is on — and, crucially, showing its **live state**. Bannerbound's stations are often multiblocks with no
inventory screen, so a glance-able readout is the difference between guessing and knowing.

With Jade installed you can look at a station and read things like:

- a **Bloomery's** current temperature as it heats, holds, and cools
- **cooking or firing progress** ticking upward on a campfire, kiln, or drying rack
- the identity and status of the block in front of you before you commit a right-click

It changes nothing about how the game plays — it just surfaces the numbers and states the game is
already tracking, so you stop opening menus to check on a smelt.

---

## Create — Hold [W] to Ponder

Create's best-known feature isn't a machine at all — it's **Ponder**, an animated, narrated tutorial
system that walks you through a mechanic step by step in a little 3D scene. Bannerbound hooks straight
into it.

When **Create** is installed, [Chronicle](codex-and-ponder.md) research entries that have a scene attached
show a **Hold [W] to Ponder** prompt. Hold :material-keyboard-outline: **W** and Create's Ponder window
opens, playing an animated walkthrough of that station or interaction — assembling it, using it, and
showing the result — far clearer than any wall of text.

??? question "What happens without Create?"
    The **Hold [W] to Ponder** prompt simply doesn't appear, and the rest of the Chronicle works
    exactly as before. Ponder is a bonus layer on top of the written guide, not a replacement for it —
    so the pack is fully playable without Create. Install it only if you want the animated scenes.
    See [Chronicle & Ponder](codex-and-ponder.md) for how the two fit together.

---

## Iris + Sodium — performance & shaders

**Sodium** is a rendering overhaul that dramatically improves frame-rate, and **Iris** adds shaderpack
support on top of it. They're designed to work as a pair, and they matter for one Bannerbound feature in
particular.

The [Faith](../civilization/faith.md) night sky — where you draw your gods into glowing constellations —
is built to be seen under a good shaderpack. A dark, deep, shader-lit sky makes the stars you connect and
the domains they burn in genuinely beautiful, turning Pantheon Mode from a mechanic into a spectacle.
Even without shaders, the frame-rate that Sodium buys back keeps a busy, thinking civilization running
smoothly.

!!! tip "Play with shaders?"
    Install **Iris 1.8.12** and **Sodium 0.6.13** together, then load your favorite shaderpack and step
    out under a clear night to raise a god. If you don't use shaders, Sodium on its own is still a
    worthwhile performance win.

---

## Pandas Falling Trees — natural foresting

Bannerbound's citizen **foresters** cut down trees for their settlement. On their own, they use an
in-house **whole-tree chop** — the whole trunk comes down in one job, which works fine but looks a little
abrupt.

When **Pandas Falling Trees** (the `fallingtrees` mod) is present, foresters hand the actual felling over
to it, so a citizen brings a tree down exactly the way you would with the mod installed — the same
satisfying, natural fall. It's pure polish: nothing depends on it, and the built-in chop takes over
seamlessly if it's missing.

!!! warning "This is the one that runs on the server too"
    Unlike the client-only add-ons above, Pandas Falling Trees runs on **both sides**. On a multiplayer
    server, install it on the **server** for the foresting behavior, and on **every client** that joins,
    or you'll see mismatched tree behavior. On single-player it just works.

---

## Where to next

- [Installation & Setup](../getting-started/installation.md) — versions, the two required mods, and how to add these
- [Chronicle & Ponder](codex-and-ponder.md) — the in-game guidebook the Create scenes plug into
- [Faith & the Stars](../civilization/faith.md) — the night sky these shaders are built for
- [Research & Eras](../civilization/research-and-eras.md) — the progression JEI quietly follows
