---
title: Multiplayer & Game Rules
description: How proximity chat and whisper range work on a Bannerbound server, and every custom /gamerule toggle — global chat, the celestial sky, meteor showers, offline war, and the invented-language UI — with its default and effect.
---

# Multiplayer & Game Rules

<p class="bb-lead"><em>Bannerbound isn't just single-player writ large. On a shared world your voice only carries so far — chat is a thing that travels through the air, not a magic broadcast — and a handful of custom game rules let a server owner retune the world's clock, its skies, and even the language on your screen. This page collects both.</em></p>

!!! abstract "TL;DR"
    - **Proximity chat is on by default.** Public chat *and* private messages (`/msg`, `/tell`, `/w`) only reach players within about **100 blocks** — clear up close, fading to nearly unreadable at the edge, and nothing at all beyond it.
    - Players in **another dimension** (the Nether, the End) are out of earshot entirely.
    - A whisper to someone too far away doesn't vanish silently — **you** get told they can't hear you.
    - Being **overheard by a stranger can reveal your settlement** to them, the same as being seen. Chat has consequences.
    - Server owners restore vanilla world-wide chat with `/gamerule globalChat true`, and can retune the sky, meteors, war rules, and UI language with the other custom **game rules** below.

## Proximity chat

By default, a Bannerbound server treats chat the way sound actually works: it comes out of *your character's mouth*, at your character's position, and reaches only the players near enough to hear it. There is no server-wide chat channel unless the owner turns one on.

This applies to **both** kinds of message:

- **Public chat** — everything you type into the normal chat box.
- **Private messages** — `/msg`, `/tell`, and `/w`. A whisper is still range-limited; the "private" part only means *who* receives it, not *how far* it carries.

### How far your voice carries

Distance is measured straight-line from you to each listener, and it splits into three bands:

| Distance from you | What a listener gets |
| --- | --- |
| Within **~50 blocks** | Full clarity — the message reads at normal, solid brightness. |
| **~50 to ~100 blocks** | Delivered, but **fading** — the text grows steadily dimmer the farther away the listener is, down to a barely-legible ~12% at the very edge. |
| Beyond **~100 blocks** | **Nothing.** The message is never delivered — the distant player has no idea you spoke. |

You always hear your own messages at full clarity, wherever you are.

!!! note "The fade is a feature, not a bug"
    That dimming from 50 to 100 blocks is deliberate. A message from someone at the edge of your range arrives faint and ghostly — enough to know *someone* is out there talking, not always enough to make out every word. If a line looks washed-out, the speaker is far away. Close the distance and it sharpens back up.

### Different dimensions are out of earshot

Range only matters when you share a dimension. If the person you're trying to reach is in the **Nether**, the **End**, or any other dimension, they're out of earshot no matter the coordinates — public chat won't reach them and a private message to them will report that they can't hear you (below). Plan your coordination *before* someone steps through a portal.

### A whisper that can't land tells you so

Send a `/msg`, `/tell`, or `/w` to a player who's out of range — too far away, or in another dimension — and the message isn't quietly dropped. The game tells **you**, the sender, in red:

> *&lt;name&gt; is too far away to hear you.*

So you always know whether your whisper actually arrived. If you don't see that warning, it landed.

### Talking can give you away

Chat isn't consequence-free on a shared world. When another player is **close enough to overhear you** — whether through public chat or a private message that reaches them — that contact can **reveal your settlement to them**, exactly as if they'd spotted your banners in person. This is the same neighbor-discovery that drives [diplomacy](../civilization/diplomacy.md): once a rival knows you exist, the diplomacy tab opens up between you.

!!! warning "Watch who's within earshot"
    If you're trying to stay hidden from a neighbor you haven't met yet, remember that *speaking near them counts*. A careless line of public chat — or even a whisper to a teammate — while a stranger stands within ~100 blocks can put your settlement on their map. When secrecy matters, check who's nearby before you type.

!!! tip "This is on by default"
    Proximity chat is the standard Bannerbound experience — you don't turn it on, it's simply how the world works. A server owner who wants the old world-wide chat back can lift the whole system with a single game rule, covered next.

## Game rules

Bannerbound registers a small set of custom `/gamerule` toggles, styled exactly like the vanilla ones — you set them the same way (`/gamerule <name> <value>`) and they need operator permission (or **Allow Cheats** in single-player). They cover chat, the living sky, war, and the interface language.

| Game rule | Type | Default | What it does |
| --- | --- | --- | --- |
| `globalChat` | true / false | **false** | Governs the [proximity chat](#proximity-chat) above. Left **false**, chat and private messages are range-limited and fade with distance. Set **true** to switch it all off and restore vanilla **server-wide** chat — every message reaching every player at full clarity, regardless of distance or dimension. |
| `celestialSpeed` | number | **1** | Scales the speed of the [living sky](../civilization/faith.md) — the wandering planets, the seasonal star wheel, and the calendar that drives them. **1** is the designed pace. **0** freezes the heavens in place; a large value turns the sky into a time-lapse. Primarily a testing knob. |
| `meteorAmount` | number | **2** | Roughly how many ambient **meteors** streak across a clear night per minute. **2** is the designed rate. **0** turns meteor showers off entirely; a large value makes a meteor storm. See the sky section of [Faith](../civilization/faith.md). |
| `allowOfflineWar` | true / false | **false** | Governs whether you can declare [war](../civilization/diplomacy.md) on a settlement with no members online. Left **false**, declaring war requires an online target member, and the war-warning countdown *pauses* if they log out — no one gets conquered in their sleep. Set **true** to lift that requirement and allow war against offline factions. |
| `useCustomLanguage` | true / false | **false** | When **true**, the whole interface switches into your settlement's **invented tongue** — known item titles, job labels, and creature names all render in the generated language, not just citizen names (which always use it). Left **false**, only citizen names are translated. See [Culture & Heraldry](../civilization/culture-and-heraldry.md). |

!!! note "`forceMaxAge` is set a friendlier way"
    The mod also owns a `forceMaxAge` rule — the cap on how far any settlement's era may advance — but you don't set it through raw `/gamerule`. Its default is **no cap** (the final era), and you change it with the friendly, tab-completed command **`/bannerbound force_max_age <era>`**. See [Keybinds & Commands](keybinds-and-commands.md#eras-world-age) for the era names and an example.

!!! tip "`celestialSpeed` and `meteorAmount` are mainly for testing"
    These two exist so a server owner (or a screenshot-hunter) can freeze the sky, speed it up, or crank the meteors for effect. They don't change survival balance — the faith sky's *meaning* is the same at any speed. Leave them at their defaults for a normal game.

!!! example "Turning a server back to world-wide chat"
    Running a small, cooperative server where everyone should just hear each other?

    ```
    /gamerule globalChat true
    ```

    Every message — public and private — now reaches every player at full clarity, wherever they are. To return to the default proximity model, set it back to `false`.

## Where to next

- [Keybinds & Commands](keybinds-and-commands.md) — the `/bannerbound` command tree, including `force_max_age` and the operator tools that pair with these rules.
- [Faith](../civilization/faith.md) — the living sky that `celestialSpeed` and `meteorAmount` tune: wandering planets, seasonal constellations, and meteor showers.
- [Diplomacy](../civilization/diplomacy.md) — how neighbors discover one another (including by overhearing your chat) and the war rules that `allowOfflineWar` relaxes.
- [Culture & Heraldry](../civilization/culture-and-heraldry.md) — the invented language that `useCustomLanguage` spreads across the whole UI.
- [How the World Changes](the-world.md) — the other ways Bannerbound reshapes a shared world.
- [Glossary](glossary.md) — quick definitions for the terms above.
