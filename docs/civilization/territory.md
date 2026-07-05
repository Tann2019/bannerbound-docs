---
title: Territory & Outposts
description: How to claim land chunk by chunk, keep outsiders out of your borders, and reach distant ore, stone, herds, and crop land with protected-nothing outposts.
---

# Territory & Outposts

<p class="bb-lead">Every stone your citizens lay, every field they till, every chest they guard — it all happens on land your settlement actually owns. This page is about drawing that border outward, defending what's inside it, and stretching a hand past it to the resources your walls can't reach.</p>

!!! abstract "The short version"
    - Your **territory** is a set of claimed **chunks** (16×16 columns). Claim more from the **Town Hall → Expand Territory** menu by clicking an adjacent chunk.
    - Claims must **touch** land you already own, cost **materials and population**, and are limited by a per-**era** cap. Advance your era to claim more.
    - Inside your border, **outsiders can't break, place, attack, or open your containers** — unless you're at war.
    - An **outpost** is a lone banner planted *beyond* your border to work a distant **deposit** — an ore vein, a stone or clay bed, a wild herd, or a patch of crop land. It is **not** protected. Guard the road to it.

---

## Your border is made of chunks

Land in Bannerbound is owned one **chunk** at a time — the same 16×16 block columns Minecraft already divides the world into (press ++f3+g++ to see their edges). When you found a settlement, your first chunks are claimed around the **Town Hall**. Everything your civilization does — houses, [workshops](workshops.md), [fields](food.md), stockpiles — has to sit on chunks you own.

If a citizen refuses to work a spot, ownership is the first thing to check: the land may simply not be yours yet.

!!! tip "Claim with intent"
    A chunk is a real commitment of materials and population, so don't sprawl blindly. Claim toward the **ore, water, and flat building room** you actually want, and toward beautiful land that will feed your [culture](culture-and-heraldry.md). A tight, deliberate border is cheaper to [wall](walls.md) than a ragged one.

---

## Claiming land: the Expand Territory menu

Open your **Town Hall**, choose **Expand Territory**, and a map of the chunks around your settlement opens. Your owned chunks are filled in your faction color; a claimable ring sits just outside them; land belonging to another settlement is marked as theirs and can't be taken.

Hover any chunk in that ring and the panel tells you exactly what you're buying:

| Line in the menu | What it tells you |
| --- | --- |
| **Biome** | The chunk's biome. Biome changes both the flavor of the land and, for some biomes, the **materials** the claim costs. |
| **Beauty** | The chunk's own scenic rating, on a scale from *Atrocious* up to *Breathtaking*. Beauty drives culture. |
| **Adjacency bonus** | How much the chunk's beauty is lifted (or dragged down) by its neighbors. Claim beside lovely land and the new chunk inherits some of that shine. |
| **culture/s** | The culture this chunk will generate every second once it's yours — its effective beauty turned into steady output. |
| **Required items** | The exact stack of materials this expansion costs. Gather them into your inventory or a settlement chest first. |
| **Population** | The citizen count this expansion demands, shown as *current / required*. Too few people and you can't claim yet. |

At the top of the panel, **Expansions: used / cap** tracks how many claims you've spent against your current limit.

To claim, **click an adjacent chunk**. The rule is strict and worth memorizing:

!!! warning "Claims must be adjacent"
    A new chunk must share an **edge** (north, south, east, or west) with a chunk you already own — diagonals don't count. Try to reach across a gap and you'll get *"This chunk is too far from your settlement. Claims must be adjacent to existing ones."* Your territory grows like a stain, always connected, never leapfrogging.

!!! example "Claiming your fourth chunk"
    1. Open **Town Hall → Expand Territory**.
    2. Find an empty chunk touching your border that has good **Beauty** and the **Biome** you want.
    3. Read its **Required items** line — say it wants stone. Mine or craft that stack and keep it on you (or in a settlement chest).
    4. Check the **Population** line reads green (you have enough citizens).
    5. Click the chunk. It fills with your faction color and the claim rings out in chat — *"[you] claimed territory at chunk (x, z)!"*

---

## Expansion caps and eras

You can't claim endlessly. Each **era** grants a fixed number of expansions, and once you've spent them the menu shows:

> *Era cap reached. Advance era to claim more.*

The only way past that wall is to progress your civilization through [Research & Eras](research-and-eras.md). In the opening **Ancient** era a settlement may claim up to **five** expansions. Advancing to a later era adds a fresh allowance on top — and any expansions you *didn't* use carry forward, so there's no penalty for growing slowly and deliberately.

### The cost ladder rises with each claim

Expansions get more expensive as you go. The **first** claim is cheap and needs only a small population; each successive claim asks for a larger population and a heftier stack of materials. In the Ancient era, the default ladder runs like this:

| Expansion | Population needed | Materials |
| --- | --- | --- |
| 1st | 2 | 24 cobblestone |
| 2nd | 3 | 24 andesite |
| 3rd | 4 | 32 stone |
| 4th | 5 | 64 oak logs + 32 oak planks |
| 5th | 6 | 24 raw copper |

!!! info "Your biome may change the bill"
    Some biomes substitute local materials for the stone-family costs. Found in the **desert** and your early claims ask for sandstone, cut sandstone, and sand instead of cobblestone and stone; a **badlands** settlement pays in terracotta and red sandstone. The population requirement stays the same — only the materials shift to match the land.

!!! tip "Resources can come from the whole settlement"
    You don't have to carry every block yourself. The claim can draw its cost from your **stockpiles, workshop chests, and — for councils — the voters' own inventories**, so a well-stocked town can expand from its shared supplies.

### Who gets to claim

How a claim is authorized depends on your [government](government.md):

- **Chiefdom** — the chief claims directly. Other members can *suggest* a chunk, dropping a marker on the map for the chief to act on.
- **Council** — members **vote** on a chunk; once enough votes land, the claim fires and the cost is pulled from the voters and the settlement.
- **No government** — anyone can claim outright.

---

## Territory protection

Owning land means it's *yours*. Inside your claimed chunks, anyone who isn't a member of your settlement is locked out of interfering:

| An outsider tries to… | What happens |
| --- | --- |
| Break a block | *"You cannot break blocks in [settlement]'s territory."* |
| Place a block | *"You cannot place blocks in [settlement]'s territory."* |
| Attack a citizen, animal, or block | *"You cannot harm anything in [settlement]'s territory."* |
| Fire an arrow or projectile in | *"Your projectile was blocked by [settlement]'s territory."* |
| Open a chest, barrel, or stockpile | *"You cannot use [settlement]'s containers unless you are at war."* |

This shield is what makes a settlement a safe place to build. Your fields don't get trampled by wandering players, your storage can't be looted, and your citizens can't be picked off — as long as you're at peace.

!!! danger "War lowers the drawbridge"
    Protection holds **only while you are at peace**. Once a rival [declares war](diplomacy.md), enemy players *can* break in, fight your people, and raid stockpiles inside your border. That is exactly when your [walls](walls.md) and defenders earn their keep. Roaming [barbarians](barbarians.md) are a threat of the same kind — a claim is a legal boundary, not a physical one.

!!! warning "Guard your faction banner"
    Your settlement is anchored by its **[faction banner](culture-and-heraldry.md)**. Take it down and the settlement is *"unbound — no menus, no work — until it is raised again"*; destroy it entirely and you'll be warned to *plant a new banner in your territory*. Either way it's a serious blow, so keep it deep inside your walls, never on the frontier.

---

## Outposts: reaching beyond your border

Sooner or later the resource you need — a copper-rich hillside, a stone bluff, a plain thick with wild horses, a fertile stretch of crop land — sits well outside any land you could reasonably claim. That's what an **outpost** is for: a single claim planted far from home to work one deposit, without dragging your whole border out to meet it.

Outposts don't exist until you unlock them. Research **Outposts** on the tech tree (it follows the Quarry line); later, **Frontier Logistics** and its kin let a settlement sustain more of them at once. See [Research & Eras](research-and-eras.md) for the path.

!!! quote "From the Chronicle"
    *"Plant a banner on distant ground and work what your borders cannot reach. The claim is yours alone, yet no wall shields it and no guard keeps watch — guard the road, for if the banner falls, the outpost falls with it."*

### What a deposit is — and where to find one

A **deposit** is a special resource baked into a *specific chunk*, not something you place. The overwhelming majority of chunks hold nothing special at all — only a small fraction carry a deposit, and the surrounding **biome** decides which kind can appear there:

| Where you're scouting | Roughly how often a chunk is special | What it tends to hold |
| --- | --- | --- |
| **Water** (lakes, coast, ocean) | ~1 in 8 | Fish |
| **Mountains & hills** | ~1 in 7 | Metals (copper, iron, tin, marble), coal, and stone-family beds |
| **Plains** | ~1 in 8 | Wild **horses**, dry-field crops (wheat, carrot, potato, beetroot), some metals, clay, sand |
| **Forest** | ~1 in 11 | Crops and copper/iron/coal/clay |
| **Desert, badlands, snowy** | ~1 in 25 | Metals and stone/sand/clay only — no herds or crops here |

!!! tip "Read the deposit before you march"
    Two things are worth knowing before you carry a banner out:

    - **Horses and fish are the only animals tied to chunks.** Cows, pigs, sheep, and chickens spawn naturally everywhere, so there's no such thing as a "cattle chunk" to outpost — you raise those in a home [pen](jobs-and-labor.md) instead. (Fish chunks appear on the scout map but aren't workable by an outpost worker *yet*.)
    - **Not every "special" chunk is worth the trip.** Plain **andesite, diorite, and granite** deposits read as special on the map but are low-value — near-worthless rock you'll rarely want an outpost for. Hold out for a metal, coal, clay, or crop deposit instead.

### Planting an outpost

1. **Scout** for a chunk with a workable deposit — ore for a mine, a stone or clay bed for a quarry, a wild herd, or crop land for a field — beyond your border.
2. Carry a **faction banner** out to it and **raise it** on that ground.
3. **Right-click the banner.** If the spot is valid, you'll be offered **Establish outpost here** — confirm it.

The rules for where an outpost can go are firm:

- It must be **beyond your existing border** — you can't "outpost" land you already own (claim it normally instead).
- The chunk must hold a **workable deposit**; bare ground gives you nothing to work.
- It can't be **too far** from your territory — reach is **8 chunks** from your nearest claimed chunk (measured as a square, so diagonals count).
- It must sit on **unclaimed** land — not another settlement's, and never on a **city-state's** territory.
- Outposts are **overworld only**.
- Your settlement can only sustain a **limited number** at once — **2 to start**, and **+1 for each outpost-slot research** (Frontier Logistics and its kin) up to a ceiling of **5**. Each successful plant confirms as *"Outpost established (used / limit)."*

### An outpost is exposed — protect the road, not the post

This is the part that catches people out:

!!! danger "The outpost banner is NOT protected"
    None of the [territory protection](#territory-protection) above applies to an outpost. Its banner has **no wall and no guard**. Anyone — a rival raider, a barbarian, a curious wanderer — can walk up and knock it down, and *"the outpost falls with it."* You can't fortify the post itself, so your defense is the **supply road**: keep it short, keep it watched, and keep it close enough to home that trouble can't linger there.

!!! tip "Retiring an outpost to free a slot"
    When a deposit is worked out or you'd rather spend the slot elsewhere, a **member of your settlement can simply break the outpost's own banner**. Done by one of your own people it's a quiet retirement — *"Outpost dismantled — its working claim is released"* — with **no faction alarm**, and the slot opens back up for a new plant. Only an *outsider* smashing the banner sounds the settlement-wide alert.

### Supplying an outpost

An outpost is a *supply commitment*, not free land. Two things make it actually productive:

**A chest on site (required).** Workers need somewhere to drop what they gather. Place a **chest inside the outpost chunk** and the panel confirms *"Storage: chest on site."* Without it you'll see *"no chest in this chunk — miners won't work!"* and the post sits idle.

**Roofed beds (optional but kind).** Appointing a worker doesn't just send them on a shift — it **moves them out for good**. The citizen gives up their house back in town (freeing it for someone else) and becomes a **resident of the outpost**, living, working, and sleeping on site until you recall them. So the beds aren't for a nightly commute — they're a real home. Build a small shelter with **roofed beds** in the chunk and your worker sleeps comfortably; skip it and they "sleep rough at the outpost," a standing hit to their mood. **Recall them** (from the banner panel) and they're re-homed in town like anyone else.

### Appointing a worker

Right-click the established outpost banner to open its panel. Alongside the storage and lodging status, it shows the **deposit**, your **outpost slots (used / limit)**, and a **workforce** list. Appoint the right specialist:

=== ":material-pickaxe: Ore deposits"

    Appoint a **Miner**. They chip the ore boulder on the chunk and haul it back to the site chest. A deposit reads as either a **poor vein** or a **rich vein** — richer veins yield more before they're worked out. When a vein is exhausted it shows *"worked out — it will refresh soon"* and regenerates over time.

=== ":material-shovel: Material deposits"

    Appoint a **Digger** to work a **stone or earth** bed — stone, limestone, and the andesite/diorite/granite family with a pickaxe, or clay and sand with a shovel. It uses the same vein readout (poor/rich, worked-out, refresh) as an ore mine. The stone-boulder deposits need your settlement to have researched the **Quarry** line first.

=== ":material-cow: Livestock deposits"

    Appoint a **Herder** to raise and breed the penned animals on the chunk. As with a home herd, you'll want a proper **pen** marked in the chunk for them to tend. (Only **horses** show up as chunk deposits — the other livestock you keep at home.)

=== ":material-sprout: Crop land"

    Appoint a **Farmer** to plant and harvest the chunk's crop field. A crop deposit is generous: the outpost farmer reaps **double the produce** a home field of the same crop would give, so a good crop chunk is one of the most rewarding outposts you can plant.

The candidate list only shows citizens who already hold the matching **job** — *"give a citizen the right job first"* (Miner for ore, Digger for stone or clay, Herder for a herd, Farmer for crops). Set their profession back home in [Jobs & Labor](jobs-and-labor.md) before you expect them to march out. If a miner's or digger's pickaxe is *"too soft to chip this ore,"* upgrade their tool. The site's storage, vein, and lodging readouts work the same way for every worker type.

!!! note "Outposts manage their own deposit"
    You don't mark an outpost's deposit with the Foreman's Rod the way you would a quarry at home. Point the Rod at one and it simply sends you back to the banner: *"Outposts manage their own... deposit — right-click the Outpost Banner to appoint"* the worker. The banner's own panel is the one and only place you assign it.

### Outpost checklist

- [ ] **Outposts** research completed
- [ ] Free **outpost slot** available (or research **Frontier Logistics** for more)
- [ ] Workable deposit found beyond your border, within reach, on unclaimed non-city-state land
- [ ] Faction banner planted and **Establish outpost here** confirmed
- [ ] **Chest** placed inside the outpost chunk
- [ ] **Roofed beds** built (the worker lives on site now — give them a real place to sleep)
- [ ] The right specialist appointed — **Miner** (ore), **Digger** (stone/clay), **Herder** (horses), or **Farmer** (crops)
- [ ] The **road home** kept short and defended

---

## Where to next

- [Research & Eras](research-and-eras.md) — lift your expansion cap and unlock Outposts and Frontier Logistics.
- [Jobs & Labor](jobs-and-labor.md) — assign the Miners, Diggers, Herders, and Farmers your outposts depend on.
- [Diplomacy](diplomacy.md) — how war strips your territory's protection, and how peace restores it.
- [Walls](walls.md) — turn your claimed border into a defended one.
