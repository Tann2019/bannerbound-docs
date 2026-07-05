---
title: Keybinds & Commands
description: Every Bannerbound key binding, the Pantheon Mode star-drawing controls, and the player and operator slash-commands for the Chronicle, eras, research, faith, and world age.
---

# Keybinds & Commands

<p class="bb-lead"><em>The fast lookup. Which key opens the Chronicle, which clicks draw a god into the night sky, and the operator commands that let you nudge a settlement's era, faith, or research when you need to test or fix a world.</em></p>

!!! abstract "TL;DR"
    - Bannerbound adds its own keybind category — find it under **Options → Controls → Bannerbound**.
    - **Open Chronicle** is bound to ++j++ out of the box. The **Journal Tracker** toggle ships unbound — pick your own key.
    - **Pantheon Mode** has its own in-mode controls for connecting and naming constellations.
    - A few `/bannerbound` **commands** need no cheats — they open the Chronicle, leave a settlement, or check the world era.
    - The rest are admin/operator tools (they need cheats or op). They set eras, reset faith, cap the age, and force research — useful for testing, not part of normal play.

## Keybinds

All of Bannerbound's bindings live in one category. Open **Options → Controls**, scroll to the **Bannerbound** group, and rebind anything to taste.

| Binding | Default key | What it does |
| --- | --- | --- |
| **Open Chronicle** | ++j++ | Opens the [Chronicle](codex-and-ponder.md), your in-game guidebook — every discovery, recipe, and lesson your civilization has earned. |
| **Toggle Journal Tracker** | *Unbound* | Shows or hides the on-screen objective tracker (the running to-do list in the corner). Bind your own key. |
| **Toggle Beauty Debug** | ++b++ | Toggles the beauty overlay, a decorator's tuning aid that shows how much appeal the blocks around you are giving off. |

!!! tip "Chronicle first"
    New to the pack? Press ++j++ early and often. The Chronicle unlocks entries as you play, so it always reflects what your settlement can actually do right now — it's the single best in-game reference.

!!! note "The Journal Tracker is unbound on purpose"
    Its previous default (++k++) clashed with the shader-pack selector some players run through Iris, and wasn't especially intuitive — so it now ships with no key at all. If you want the objective tracker on a hotkey, set one under **Controls → Bannerbound**.

### Pantheon Mode controls

When you draw a god into the sky, you enter **Pantheon Mode** — a special star-connecting state you trigger from beneath the open night sky (you'll need the **Star Charts** research first; see [Faith](../civilization/faith.md)). While you're in it, a legend at the top of the screen reminds you of the controls:

| Control | Action |
| --- | --- |
| **Left click** | Connect the highlighted star to your constellation. |
| **Right click** *or* ++r++ | Undo the last connection. |
| ++enter++ | Open the naming prompt — name the constellation and the deity it becomes. |
| ++esc++ | Leave Pantheon Mode without finishing. |

!!! warning "You need clear sky — and enough of the right stars"
    Pantheon Mode only opens when you're standing under the open night sky. A roof, deep cave, or midday sun will keep the heavens veiled — find an open rooftop or hilltop at night. When you go to name a god, your constellation must contain between **3 and 12 stars**, and at least one of them must be a **colored (domain) star** — otherwise the naming prompt won't let you confirm.

## Commands

Every command below is rooted at `/bannerbound`. Most are gated to **operators** (permission level 2): in single-player you'll need **Allow Cheats** enabled, and on a server you must be op. A handful, listed first, need no cheats at all.

!!! danger "The admin commands override normal progression"
    Setting an era, forcing research, or resetting faith skips the systems that would normally earn those things. They're perfect for testing and troubleshooting — and a fast way to spoil a survival playthrough. Prefer them on test worlds.

### Player commands

These carry no permission gate — any player can run them.

| Command | What it does |
| --- | --- |
| `/bannerbound codex` | Opens the [Chronicle](codex-and-ponder.md) — exactly what the ++j++ key does, handy if you've rebound it. |
| `/bannerbound leave` | Leaves your current [settlement](../civilization/settlements.md). |
| `/bannerbound world get_age` | Prints the current **world era**. |

### Eras & world age

| Command | What it does |
| --- | --- |
| `/bannerbound set_age <era>` | Sets **your own settlement's** era. Reports *"&lt;settlement&gt; is now in the &lt;era&gt;."* |
| `/bannerbound world set_age <era>` | Sets the **world** era directly. Reports *"World age is now the &lt;era&gt;."* |
| `/bannerbound reset_world_age` | Drops the world all the way back to **Antiquity** and clears the discovered-research set. Reports *"World age reset to Antiquity. Discovered-research set cleared."* |
| `/bannerbound force_max_age <era\|none>` | Caps how far any settlement may advance. Any [research](../civilization/research-and-eras.md) that would push past the cap is blocked. `none` clears the cap. Run it **with no era** to read the current cap. |

The valid era names are:

`antiquity` · `medieval` · `renaissance` · `industrial` · `diesel` · `atomic` · `modern` · `future`

!!! example "Locking a world to the Bronze Age"
    Want a server that never leaves the [Antiquity](../antiquity/index.md) content?

    ```
    /bannerbound force_max_age antiquity
    ```

    The game confirms the cap, and any research that would push a settlement past Antiquity simply won't complete. Later, lift it with `/bannerbound force_max_age none` — you'll see *"Era cap cleared — civilizations may advance freely."*

### Research

| Command | What it does |
| --- | --- |
| `/bannerbound unlock <research>` | Force-completes a research on **your settlement**, walking its prerequisite chain so anything it depends on unlocks too. Reports *"Force-unlocked '&lt;research&gt;' for &lt;settlement&gt;."* |
| `/bannerbound unresearch <research>` | Undoes a completed research on your settlement (works on both the science and culture trees). Reports *"Unresearched &lt;research&gt; for &lt;settlement&gt;."* |

Both commands tab-complete: `unlock` suggests the whole tree, while `unresearch` only offers researches your settlement has actually finished — so you can see at a glance what's undoable. See [Research & Eras](../civilization/research-and-eras.md) for how research normally progresses.

### Faith

| Command | What it does |
| --- | --- |
| `/bannerbound reset_religion <settlement\|all>` | Strips a settlement's faith so its founding flow can be re-run without a fresh world. Pass a settlement name, or `all` to wipe every settlement. Reports *"Faith reset on &lt;n&gt; settlement(s)."* |

Use this when you want to re-test the whole religion path — drawing new gods, re-founding a [faith](../civilization/faith.md) — on a world you've already been playing.

!!! tip "Names with spaces"
    If a settlement's name contains spaces, wrap it in quotes: `/bannerbound reset_religion "Old Harbor"`. Tab-completion adds the quotes for you.

### The Chronicle

Operator commands for editing what a player has unlocked in the [Chronicle](codex-and-ponder.md) — handy for setting up a curated test save or handing a new player a head start.

| Command | What it does |
| --- | --- |
| `/bannerbound codex unlock <player> <entry\|all>` | Unlocks a single Chronicle entry (or `all` of them) for the named player. |
| `/bannerbound codex lock <player> <entry\|all>` | Re-locks a single entry, or `all`, for that player. |
| `/bannerbound codex reset <player>` | Wipes that player's entire Chronicle unlock/read state back to a fresh start. |

### Tuning & other operator tools

The `/bannerbound` tree also carries a set of deeper testing tools. Tab-completion is the best way to explore them; the ones you're most likely to reach for are collected here.

???+ note "Adjusting a settlement's output"
    These take a **settlement name or `all`** as the first argument, then a value. `set_*` fixes the rate outright; `add_*` nudges it (values may be negative, and a rate that would drop below zero is simply clamped to zero).

    | Command | What it does |
    | --- | --- |
    | `/bannerbound <settlement\|all> set_food_generation <value>` | Sets the food generation rate. |
    | `/bannerbound <settlement\|all> set_culture_generation <value>` | Sets the culture generation rate. |
    | `/bannerbound <settlement\|all> set_science_generation <value>` | Sets the science generation rate. |
    | `/bannerbound <settlement\|all> add_food_generation <value>` | Adjusts food generation up or down. |
    | `/bannerbound <settlement\|all> add_culture_generation <value>` | Adjusts culture generation up or down. |
    | `/bannerbound <settlement\|all> add_science_generation <value>` | Adjusts science generation up or down. |
    | `/bannerbound <settlement\|all> set_population <value>` | Sets the settlement's population. |
    | `/bannerbound <settlement\|all> add_population <value>` | Adjusts population up or down. |

??? info "Other command families (testing & debug)"
    Discoverable through tab-completion, these are unstable dev tools meant for testing edge cases, not for normal play — expect them to change:

    - `/bannerbound crisis start <crisis>` / `clear` — trigger or end a [crisis](../civilization/crises.md) on your settlement.
    - `/bannerbound diplomacy list | discover <target> | war <target> | peace <target>` — force [diplomacy](../civilization/diplomacy.md) states with a known settlement.
    - `/bannerbound walls preview | refine | layout | construct | cancel | status` — step through the [wall](../civilization/walls.md) planner by command.
    - A suite of world-simulation debug commands for stress-testing [barbarians](../civilization/barbarians.md), city-states, camps, and traders.

    !!! warning "Not player-facing"
        These bypass the normal rules — spawning threats, forcing wars, skipping timers. Keep them off survival servers.

## Where to next

- [The Chronicle & Ponder](codex-and-ponder.md) — the guidebook the ++j++ key opens, and how it fills in.
- [Faith](../civilization/faith.md) — draw constellations into gods using the Pantheon Mode controls above.
- [Research & Eras](../civilization/research-and-eras.md) — how eras and research advance without commands.
- [Glossary](glossary.md) — quick definitions for the terms above.
