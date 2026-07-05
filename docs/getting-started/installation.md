---
title: Installation & Setup
description: Everything you need to get Bannerbound running — versions, the two required mods, install steps for client and server, and the optional add-ons.
---

# Installation & Setup

<p class="bb-lead"><em>Two mods, one civilization. Get Bannerbound loaded, launch your world, and the age of stone is yours to shape.</em></p>

!!! abstract "The short version"
    Bannerbound runs on **Minecraft 1.21.1** with **NeoForge 21.1.230** and **Java 21**. Install
    **both** required mods — **Bannerbound: Core** and **Bannerbound: Antiquity** — into your `mods`
    folder (Antiquity needs Core to run). Add the optional mods you like for a smoother ride, launch,
    and read on to [Your First Hour](first-hour.md).

## What you need

Bannerbound targets a single, exact Minecraft and mod-loader version. Match it precisely — a
mismatched loader is the number-one cause of a world that refuses to load.

| Requirement | Version | Notes |
| --- | --- | --- |
| Minecraft | **1.21.1** | Exactly this release — not 1.21.0, not 1.21.2. |
| Mod loader | **NeoForge 21.1.230** | NeoForge, *not* Forge or Fabric. |
| Java | **Java 21** | Required by Minecraft 1.21.1. Most launchers can download it for you. |
| Memory | A few gigabytes allocated | A living civilization does real thinking, so give it room — several gigabytes is a comfortable starting point. |

!!! warning "NeoForge, not Forge"
    "Forge" and "NeoForge" are different loaders. Bannerbound is built for **NeoForge**. If your
    launcher offers both, pick NeoForge and version **21.1.230**.

## The two required mods

Bannerbound ships as a pair. You need **both** in your `mods` folder for the pack to work.

=== ":material-castle: Core"

    **Bannerbound: Core** (`bannerbound`) is the civilization engine — settlements, citizens, jobs,
    housing, food, [research](../civilization/research-and-eras.md), [faith](../civilization/faith.md),
    diplomacy, and everything that makes a village into a nation. This mod stands on its own.

=== ":material-pickaxe: Antiquity"

    **Bannerbound: Antiquity** (`bannerboundantiquity`) is the Stone-to-Bronze-Age tech expansion —
    [knapping](../antiquity/knapping.md), [woodworking](../antiquity/woodworking.md),
    [masonry](../antiquity/masonry.md), [pottery](../antiquity/pottery.md),
    [metalworking](../antiquity/metalworking.md), and the rest of the early crafts. It **hard-depends
    on Core** and loads **after** it.

!!! info "Load order is automatic"
    Antiquity declares Core as a required dependency and asks the loader to place it *after* Core —
    NeoForge sorts this out on its own. You just need both JARs present. If Antiquity is installed
    without Core, the game will stop at startup and tell you Core is missing.

## Installing Bannerbound

Pick the path that matches how you play. All three end the same way: both required mod files sitting
in your `mods` folder.

=== ":material-package-variant: Modpack launcher"

    The easiest route. In a launcher like the CurseForge, Prism, or Modrinth app:

    - [ ] Create a new instance on **Minecraft 1.21.1** with **NeoForge 21.1.230**.
    - [ ] Add **Bannerbound: Core** and **Bannerbound: Antiquity** to the instance.
    - [ ] Add any [optional mods](#optional-mods) you want.
    - [ ] Launch. The launcher handles Java and the loader for you.

    !!! tip "If a curated Bannerbound pack is available"
        When a ready-made pack exists, just install it — it already bundles the correct loader, both
        mods, and a sensible set of optional add-ons. Nothing to assemble by hand.

=== ":material-folder-cog: Manual (client)"

    Prefer to build it yourself?

    - [ ] Install the **NeoForge 21.1.230** client for **Minecraft 1.21.1** (run the NeoForge
      installer, choose *Install client*).
    - [ ] Launch that profile once so the `mods` folder is created, then close the game.
    - [ ] Drop **both** mod JARs into `.minecraft/mods` (or your instance's `mods` folder).
    - [ ] Drop any [optional mods](#optional-mods) in beside them.
    - [ ] Launch the NeoForge profile.

    On Windows the default `mods` folder lives at `%APPDATA%\.minecraft\mods`.

=== ":material-server: Dedicated server"

    Running a shared world for your friends? The two required mods go on the **server** too.

    - [ ] Install the **NeoForge 21.1.230** dedicated server for **Minecraft 1.21.1**.
    - [ ] Place **Bannerbound: Core** and **Bannerbound: Antiquity** in the server's `mods` folder.
    - [ ] Every player installs the **same** required mods on their client.
    - [ ] Start the server, accept the EULA, and connect.

    !!! warning "Client-side extras stay on the client"
        **JEI**, **Jade**, **Create**, **Iris**, and **Sodium** are client-only — leave them off the
        server. The one exception is **Pandas Falling Trees**: it runs on both sides, so if you want
        citizen foresters to fell trees with it, install it on the **server and every client**.

## Optional mods

None of these are required, but each one makes Bannerbound nicer to play. Install the ones that suit
you — the pack detects each and lights up the matching feature quietly, with no errors if it's absent.

| Mod | What it adds |
| --- | --- |
| **JEI** (Just Enough Items) | A searchable recipe viewer. Look up any recipe, ingredient, or use in-game. **JEI 19 or newer.** |
| **Jade** | Hover tooltips that name the block or entity you're looking at and show its state — invaluable for reading multiblock stations. **Jade 15.8+.** |
| **Create** | Powers the **Hold [W] to Ponder** animated guide scenes — step-by-step visual walkthroughs of Antiquity's stations, opened right from the [Chronicle](../reference/codex-and-ponder.md). **Create 0.5+.** |
| **Iris** + **Sodium** | Shader support and a big frame-rate boost. Together they let the [faith](../civilization/faith.md) night sky and its constellations render correctly under a shaderpack. **Iris 1.8.12 with Sodium 0.6.13.** |
| **Pandas Falling Trees** | Lets your citizen foresters fell whole trees exactly the way a player does. Without it, foresters fall back to a built-in whole-tree chop — so it's a polish, not a requirement. |

!!! tip "Recommended starter set"
    For a first playthrough, **JEI** and **Jade** pay for themselves immediately — one tells you *how*
    to make things, the other tells you *what* you're looking at. Add **Create** if you want the
    animated Ponder tutorials, and **Iris + Sodium** if you play with shaders.

??? question "Do the Ponder scenes need Create to exist?"
    Yes — the **Hold [W] to Ponder** prompt only appears when Create is installed. Without it, the
    written [Chronicle](../reference/codex-and-ponder.md) entries still teach you everything; you
    simply won't get the animated version. Nothing breaks either way.

## The old ways are closed

One thing to know before you set out: **the ancient portals are sealed at the start of a game.** Try
to step through to the Nether or the End early and you'll be turned back with a line you'll come to
know well:

!!! quote
    "The old ways into the Nether and the End are closed to you."

These realms open only later, once your people have advanced far enough down the road of
[research and the eras](../civilization/research-and-eras.md). It's not a bug; it's the road. Focus on
your first settlement, keep your [Chronicle](../reference/codex-and-ponder.md) growing, and the wider
world will open in time.

## First-launch checklist

Before you dive into your first world, a quick pass:

- [ ] Instance is on **Minecraft 1.21.1** + **NeoForge 21.1.230**.
- [ ] **Bannerbound: Core** and **Bannerbound: Antiquity** are both in `mods`.
- [ ] Optional mods (if any) are in `mods` too — client-only ones on the client, Pandas Falling Trees on both sides for servers.
- [ ] The game reaches the main menu with no missing-dependency error.
- [ ] In-world, press **`J`** to open the **Chronicle** — your in-game guidebook. If it opens, you're good to go.

!!! success "You're in"
    Mods loaded, world created, Chronicle at your fingertips. Now go make history.

## Where to next

- [Your First Hour](first-hour.md) — what to do the moment you spawn.
- [Founding a Settlement](founding-a-settlement.md) — plant your banner and claim your first ground.
- [The Codex & Ponder](../reference/codex-and-ponder.md) — how the Chronicle and animated guides work.
- [Keybinds & Commands](../reference/keybinds-and-commands.md) — every default key, including the Chronicle.
