---
title: FAQ & Troubleshooting
description: Fixes for the most common "why isn't this working?" problems in Bannerbound — idle citizens, dead stockpiles, starvation, blocked settling, claiming, research, mining, and portals.
---

# FAQ & Troubleshooting

<p class="bb-lead">Something not behaving? Almost every "it's broken" moment in Bannerbound is really a rule you haven't met yet — a missing banner, an un-researched system, a tool that's too crude for the job. This page walks the usual suspects, in the order players hit them.</p>

!!! abstract "The one-minute checklist"
    Nine times out of ten, a stuck settlement fails one of these:

    - [ ] Your **banner is raised** near the Town Hall and intact.
    - [ ] You have a **government** — citizens won't take orders in anarchy.
    - [ ] Workers have a **tool in storage** and a **marked drop-off**.
    - [ ] Your people are **happy enough** to show up for work.
    - [ ] The system you're using is actually **researched** (storage, workers, portals).
    - [ ] The **tool age** is high enough for the block or recipe.

    Read on for the specific message you're seeing.

---

## Citizens & labor

### My citizens won't work

This is the big one, and it has several possible causes. Open a citizen's card (or hover their head) and read the **status line** — it usually names the problem outright. Match it below.

| What you see | What it means | The fix |
| --- | --- | --- |
| *"Halted — banner is down"* / *"Faction banner lost!"* | Your banner is down, destroyed, or walled off | Re-raise the official banner within **24 blocks** of the Town Hall, with a **clear access side** so it registers |
| *"No code of laws — citizens won't obey assignments yet"* | You're in **anarchy** with no government | Form a government at the Town Hall (see [Government](../civilization/government.md)) |
| *"Idle — no tool"* | The job's tool isn't in reachable storage | Craft the tool and drop it in the worker's drop-off or the workshop's storage |
| *"Idle — no drop-off"* | No place to deposit the harvest | Mark a **drop-off** on the citizen's job tab, or set a preferred storage in the Town Hall labor screen |
| *"Idle — drop-off full"* | The drop-off has no free slots left | Empty it, add containers, or point the worker at a roomier stockpile |
| *"Refusing to work"* / *"On strike today"* | Happiness is too low | Improve [housing](../civilization/housing.md), food, and culture — miserable citizens work far slower or strike outright |
| *"Invalid — needs repair"* (workshop) | The workshop or station isn't a valid room | Fix the enclosure, work block, storage, or headroom (see below) |
| *"That tool is too advanced for your current tool age"* | You handed a worker a tool your civilization hasn't unlocked | Advance your [tool tier](../antiquity/tool-tiers.md), or give them an age-appropriate tool |

!!! warning "A banner is not decoration"
    If your standard falls or gets walled off, command breaks across the **whole** settlement — everyone downs tools at once. If your workers all went idle at the same moment, check the banner first. It must sit within 24 blocks of the Town Hall with an open, accessible face.

!!! tip "Read the status, not the vibes"
    Bannerbound almost always tells you what's wrong in plain language. Before you rebuild anything, open the citizen card, the workshop panel, or the stockpile block and read the status line — it's the fastest diagnosis you have.

### My workers won't take job assignments

You see *"No code of laws — citizens won't obey assignments yet."* Until you've founded a **government**, your settlement is in anarchy: you can *ask* citizens to switch jobs (and they may refuse) or set drop-offs, but you can't directly command labor. Hold an election or declare a Chiefdom, and assignments start sticking.

See [Government](../civilization/government.md) and [Jobs & Labor](../civilization/jobs-and-labor.md).

### The job or worker I want is locked

Trying to assign a role with the **Foreman's Rod** and it refuses with *"Your settlement hasn't researched that worker yet"*? That profession is gated behind [research](../civilization/research-and-eras.md) — unlock it first, then assign. The same is true of specialist storage and deposits: if a tool of the trade or a work site is greyed out, you almost certainly haven't researched the system that grants it.

See [Jobs & Labor](../civilization/jobs-and-labor.md) and [Research & Eras](../civilization/research-and-eras.md).

### A workshop or station says "Invalid"

A workshop only runs when it's a genuinely usable room. Open the workshop panel and read the status — common failures:

- **Not enclosed** or **disconnected** — the marked blocks don't form one sealed room.
- **No work block inside** — the craft's core block (kiln, chopping stump, loom, etc.) is missing.
- **No storage inside** — add a chest, barrel, or basket for inputs and outputs.
- **Work block / storage unreachable** — clear a walkable path to it.
- **Roof too low** — citizens need two blocks of headroom over the work block.
- **Missing heat source / crafting surface / required tool** — the recipe needs a fire, a surface, or a tool (like a saw) present.
- **Missing curing liquid** — a [tannery](../antiquity/tannery.md) needs a clay tank filled with curing liquid before it will work hides.

Fix whatever it names, and the status flips to **Valid**. See [Workshops](../civilization/workshops.md).

---

## Storage & food

### I can't place a chest or barrel

Early on, vanilla storage is beyond your people: try to set one and you'll read *"Your settlement hasn't learned to build storage like this yet — use a basket."* Until you research the storage that unlocks it, weave and place a **Basket** instead — it holds goods, accepts a worker's drop-off, and can serve as a job's tool storage. Chests, barrels, and the shared stockpile open up as you progress your [research](../civilization/research-and-eras.md).

### The stockpile does nothing

A **Stockpile** is Bannerbound's shared warehouse, and it has real prerequisites. Right-click **Cobblestone** with a **Basket** to weave it into a Stockpile block — but it won't activate until *all* of these are true:

1. You've researched **Storage Logistics**. Without it you'll see *"Research Storage Logistics before you can weave a basket into a stockpile."*
2. You have **fences** to enclose it. Fences require both **Animal Husbandry** and **Woodworking** — so those come first.
3. The stockpile sits inside a **fenced (or walled) ring** with **no gaps** and no solid block breaking the fence line.
4. The ring has a **fence gate** so citizens can walk in.
5. There's a **roof** over the area to shelter the goods.
6. There are **containers inside** — chests, barrels, or baskets for the goods to live in (up to **8** connect to one stockpile).

The block's own status line names whichever step you're missing:

!!! example "Reading the stockpile status"
    - *"place it inside a fenced, roofed area to activate"* — you haven't enclosed it yet.
    - *"not enclosed. A solid block is breaking the fence/wall ring"* — a wall or block is interrupting the fence line.
    - *"the enclosed area is too large, or the fence ring has a gap"* — shrink the ring or seal the missing fence section.
    - *"needs a fence gate so citizens can walk in"* — add a gate.
    - *"needs a roof to shelter the goods"* — cover it.
    - *"enclosed, but empty. Place chests, barrels, or baskets inside"* — add containers.
    - *"Stockpile ready — X/Y containers connected"* — it works. 🎉

!!! warning "The order of research matters"
    Players often research Storage Logistics, place a stockpile, and wonder why it's dead — the answer is usually **fences**. You can't seal the enclosure without them, and fences are gated behind Animal Husbandry + Woodworking. Plan that chain first.

See [Workshops](../civilization/workshops.md) and [Research & Eras](../civilization/research-and-eras.md).

### Everyone is starving

Starvation is the first crisis most settlements face, and it's solved by building a **stable stored-food rate** — not by any single heroic harvest. Work through this:

- [ ] **Assign gatherer jobs.** Fishers, farmers, hunters, foragers, or herders — pick a food path and staff it. See [Food](../civilization/food.md).
- [ ] **Set their work areas.** Use the **Foreman's Rod** to mark fields, pens, and gathering zones. A jobless or arealess worker produces nothing.
- [ ] **Give them tools.** No hoe, no farming; no fishing tool, no catch.
- [ ] **Keep storage in claimed chunks.** Food only counts toward the settlement when it lands in **claimed** storage (baskets, chests, stockpiles) that's safe from spoilage and poison.
- [ ] **Cook stew.** A hot [stew](../antiquity/cooking-and-food.md) is efficient food and pushes you into a **surplus**, which also lets your settlement take in newcomers.

Hover the **Food** line on the Town Hall to see your stored-food rate per second and how many days of reserve you have.

!!! warning "Ignore the crisis' 'drop-off chest' text"
    The in-game Starvation crisis mentions delivering food to a specific *"drop-off chest."* That wording is **stale** — don't go hunting for a special chest. What actually matters is **stored valid food in claimed storage** and a positive stored-food rate. Solve for that and the crisis clears.

See [Crises](../civilization/crises.md) and the [Cooking](../antiquity/cooking-and-food.md) page.

---

## Founding & territory

### I can't found a settlement

Placing your standard gets rejected? It's one of these:

- **Too close to another settlement.** You must be at least **6 chunks** away from any other settlement's claimed chunks. Move further out.
- **Too close to a city-state.** You can't settle on or beside a city-state's territory — give it a wide berth.
- **Banner color already taken.** Each settlement on the server needs a **unique** banner color. Pick another.
- **Invalid name.** Names must be **3–24 characters** — letters, numbers, spaces, hyphens, underscores, or apostrophes. And a name already in use is rejected.

See [Founding a Settlement](../getting-started/founding-a-settlement.md).

### I can't claim territory (Expand Territory)

Open the **Expand Territory** screen and it won't let you claim? Check each requirement — the panel lists them:

- **Not adjacent.** New claims must touch a chunk you already own. *"Claims must be adjacent to existing ones."*
- **Era cap reached.** *"Era cap reached. Advance era to claim more."* Each era caps how far you can expand — [research](../civilization/research-and-eras.md) the next era to lift it.
- **Not enough population.** Larger territory needs more people. Grow first (food surplus draws newcomers).
- **Missing required items.** Each claim has a material cost shown under **Required items** — gather them before clicking.

See [Territory](../civilization/territory.md).

---

## Research & progression

### I can't research X

A research node won't start for one of three reasons:

- **Age-locked.** *"Your settlement isn't advanced enough for this research yet."* You must reach the right era first — later nodes stay hidden or greyed until you get there.
- **Prerequisites unmet** (or a research is already running). Complete the earlier nodes it branches from, and finish any active research first.
- **You're not the Chief.** *"Only the Chief may direct research. Click a node to suggest it instead."* In a Chiefdom, only the seated leader commits research — everyone else can **suggest** nodes for the Chief to pick.

See [Research & Eras](../civilization/research-and-eras.md) and [Government](../civilization/government.md).

### A worker can't mine this ore

You marked a deposit but the miner won't touch it, or you see *"pickaxe is too soft to chip this ore."* The pickaxe is **too crude** for that block — hand the miner a harder tool. Ore hardness climbs with the ages: soft stone tools chip the easy deposits, but tougher ores need bronze and beyond.

You may also see *"Your people don't know how to work this deposit yet"* — that deposit type is locked behind research or a higher **tool age**.

See [Tool Tiers](../antiquity/tool-tiers.md), [Knapping](../antiquity/knapping.md), and [Metalworking](../antiquity/metalworking.md).

### I can't go to the Nether or the End

Lit a portal and nothing happens? *"The old ways into the Nether and the End are closed to you."* Both portals stay **locked** until your civilization researches the way through. This is intentional — the ancient world comes first. Progress your [research](../civilization/research-and-eras.md) and the paths open in time.

---

## Still stuck?

- Read the **status line** on the block, citizen, or panel — it names the exact problem.
- Check the [Glossary](glossary.md) if a term is unfamiliar.
- Confirm your [keybinds](keybinds-and-commands.md) — a missing menu is sometimes just an unbound key.
- Consult the in-game [Chronicle](codex-and-ponder.md), which tracks your objectives and explains each system as you unlock it.

## Where to next

- [Jobs & Labor](../civilization/jobs-and-labor.md) — how work assignment, tools, and drop-offs really function.
- [Research & Eras](../civilization/research-and-eras.md) — what unlocks what, and when.
- [Crises](../civilization/crises.md) — starvation and the other trials your settlement will face.
- [Glossary](glossary.md) — every Bannerbound term in one place.
