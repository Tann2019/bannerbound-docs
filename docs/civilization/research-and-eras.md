---
title: Research & Eras
description: How your settlement builds knowledge — the Science, Culture, and Faith trees, Insight bursts, tool ages, and the nine eras that carry you from bone tools to the future.
---

# Research & Eras

<p class="bb-lead"><em>Every civilization begins with a banner, a handful of kin, and tools of stick and bone. Everything you become after that — the jobs your people can hold, the blocks they can shape, the borders they can keep — is knowledge you chose to pursue. Research is the beating heart of your settlement's story.</em></p>

!!! abstract "The short version"
    Open the **Research** window from the town hall. It holds three trees — **Scientific Research**, **Culture Research**, and **Faith** — each fuelled by a resource your settlement generates over time (Science, Culture, and Devotion). Pick a node and it fills toward completion; finishing it unlocks items, jobs, crafts, [policies](government.md), build palettes, sometimes a new [crisis](crises.md), or an advance to the next **era**. Only the **Chief** may start a research; everyone else may *suggest*. Do the right work at the right moment and you earn an **Insight** — a burst that shoves a research toward the finish, sometimes completing it outright.

## The three trees

Open the town hall and choose **Research**. Inside are three separate knowledge trees, each on its own tab, each paid for with its own resource:

=== ":material-flask: Scientific Research"

    The backbone of your civilization. Tools, jobs, crafts, metallurgy, walls, roads, and era advancement all live in the **Science** tree. It is fuelled by **Science per second** that your settlement produces as it works and grows.

=== ":material-drama-masks: Culture Research"

    The **Culture** tree, paid for with **Culture per second**. Culture research shapes how your people express themselves — and completing Culture nodes grants more **Heraldry points** for your banner (the game even reminds you: *"Culture researches grant more Heraldry points."*). See [Culture & Heraldry](culture-and-heraldry.md).

=== ":material-hands-pray: Faith"

    The **Faith** tab draws on **Devotion**, the resource your shrines and worshippers accrue. Raising gods, charting the pantheon, and completing faith research all work through the same node system as the other two trees. See [Faith](faith.md) for how Devotion is earned and spent.

All three run on the same Chronicle-driven unlock system, so a node in one tree can light up an entry in another. When the Create mod is present, some nodes even carry a **Ponder** scene you can watch to see the mechanic in motion — see [Codex & Ponder](../reference/codex-and-ponder.md).

## How a node fills

Every research is a **node**. Each has a point cost — Storage Logistics needs 12, Pottery 48, Iron Working a steep 200 — and the node's header shows your progress toward it as `banked/total · rate /s`. Pottery's header climbs from `0/48` to `48/48` as your Science per second pours in; hover the node and it lists its **Unlocked Items** and effects so you know exactly what you are buying.

A node fills only while it is the **active** research. You advance one node at a time — start it, and queue up what should come next (*"That research is already queued."* if you double-book). A finished node reads **Completed**, a settlement-wide banner announces *"Research completed: …"*, and every member personally hears *"You now understand '…'."*

!!! tip "Watch your generation rate"
    The ` /s` figure in the header is your real throughput, and it climbs as your population and workshops grow — the game announces shifts outright: *"Science generation changed by … (now …/s)."* If a research feels glacial, you rarely need a different node; you need a bigger, busier settlement. Certain gods and policies can nudge the rate higher too — belief and knowledge feed each other.

## Only the Chief directs research

Research is a decision of state, and the state has one head. **Only the Chief may start, queue, or cancel a research.** Click a node as anyone else and you are told:

> Only the Chief may direct research. Click a node to suggest it instead.

That *suggest* is the lever ordinary members hold. Clicking a node sends the Chief a suggestion — *"So-and-so suggested getting Knapping in the Scientific Research"* — and you can withdraw it just as easily. A wise Chief reads the room before committing the settlement's Science to a whim. See [Government](government.md) for who becomes Chief and how the office changes hands.

## Insight: knowledge earned by doing

You do not only *pay* for research — sometimes you *stumble into* it. Many nodes carry a hidden **Insight** trigger tied to an action in the world. Do that thing while the research is active and you are rewarded with a burst:

> Insight - Woodworking surges ahead!

- Chop a stack of logs and **Woodworking** lurches forward.
- Gather stone bricks and **Masonry** leaps.
- Breed a pair of animals and **Animal Husbandry** jumps.
- Mine a vein of copper and **Metal Working** surges.

Each Insight shoves the research a long way toward completion, and if it was close enough it finishes on the spot — *"Insight completes …!"*. Insight rewards playing the game the way the research points: the settlement learns fastest by doing the very work it is trying to master.

!!! example "Earning an Insight, step by step"
    - [x] Your Chief starts **Storage Logistics** in the Science tree.
    - [x] Meanwhile your foragers bundle thatch. Once enough thatch bundles are stockpiled, the Insight fires.
    - [x] *"Insight - Storage Logistics surges ahead!"* — the bar jumps, and the **Basket** and shared **Stockpile** drop into your unlocked list far sooner than raw Science alone would have managed.

## The nine eras

Above individual nodes sits your settlement's **era** — the broad epoch it belongs to. There are nine, and you climb them in order. Each era sits on a point in history, from the deep Stone-Age past to a speculative future:

| # | Era | Timeline year |
|---|-----|--------------:|
| 1 | **Ancient Era** | −15000 |
| 2 | **Classical Era** | −800 |
| 3 | **Medieval Era** | 450 |
| 4 | **Renaissance Era** | 1450 |
| 5 | **Industrial Era** | 1760 |
| 6 | **Diesel Era** | 1900 |
| 7 | **Atomic Era** | 1945 |
| 8 | **Modern Era** | 1990 |
| 9 | **Future Era** | 2100 |

You begin in the **Ancient Era**. Advancing is itself a research payoff: completing **Bronze Age** carries you into the Classical Era (*"… has advanced to the Classical Era!"*), and completing **Iron Working** carries you into the Medieval Era. Those two keystones are the whole of the research-driven climb today: **Iron Working → Medieval is the furthest the tech tree can carry you on its own.**

!!! warning "Eras beyond Medieval aren't in the tree yet"
    The six later eras — Renaissance, Industrial, Diesel, Atomic, Modern, and Future — are already written into the world's timeline, but **no research node advances you into them.** For now they live only as dates on the calendar; a world reaches them only if an operator sets the era by hand with the `/bannerbound set_age` command. Don't plan a tech path around a Renaissance keystone — there isn't one. See [Keybinds & Commands](../reference/keybinds-and-commands.md).

Advancing an era does two big things:

- **It opens higher-tier research.** Many nodes are **age-locked** — their tooltip reads *"Requires the Classical Era"* (or later). Try to start one too early and you are told *"Your settlement isn't advanced enough for this research yet."* Nodes far beyond your era stay hidden entirely: *"Advance to a later era to reveal this research."*
- **It widens your borders.** A higher era raises your territory caps, so your settlement can claim and hold more of the map. It also unlocks larger [homes](housing.md) — a house too grand for your era simply won't count until you catch up. See [Territory & Claims](territory.md).

!!! warning "You can't skip the line"
    Research obeys **prerequisites** and **era** together. Knapping needs Woodworking first; Iron Working needs the Bronze Age; Shearing waits until the Medieval Era. Plan your tech path backward from the goal, and remember that the two era-advancing keystones (Bronze Age → Classical, Iron Working → Medieval) are the gates that open whole new stretches of the tree.

??? info "Some worlds cap the era"
    A server or world can set a maximum era — *"Era cap: the … . Research that would advance past it is blocked."* If an era-advancing keystone refuses to complete, check whether your world has been capped below it.

## Tool ages gate what your workers can hold

Running underneath the era is a second, finer ladder: your settlement's **tool age**. It decides the *best* tool a worker is allowed to equip. A worker can use a tool of the current tool age **or lower** — so a stone-age tribe cannot hand out iron picks even if it happens to find one.

The tool age climbs as you research, roughly in step with your metallurgy. Each rung works faster and hits harder than the last:

| Order | Tool age | Unlocked by |
|-------|----------|-------------|
| 0 | **Bone Age** | Settlement (at founding) |
| 1 | **Wood Age** | Woodworking |
| 2 | **Stone Age** | Knapping |
| 3 | **Copper Age** | Metal Working |
| 4 | **Bronze Age** | Bronze Age research |
| 5 | **Iron Age** | Iron Working |

Completing one of these announces *"Unlocks the Stone Age for workers"* (or Copper, Bronze, Iron…). Note that the **Bronze Age** here is a *tool* tier — the same research that unlocks it advances your *era* to Classical, so don't confuse the two.

Each worker's job tab shows the tool slot it needs; drop a valid tool in, or mark a **tool storage** so workers pull one automatically. For the full tool-by-tool breakdown — mining speeds, weapon damage, and which craft unlocks which head — see [Tool Tiers](../antiquity/tool-tiers.md) and [Jobs & Labor](jobs-and-labor.md).

!!! info "Research reveals the ore itself"
    Some nodes don't just unlock a tool — they teach your people to *see* the metal in the rock. Their effects read *"Reveals … in stone."* **Quarry** reveals coal; **Ore Mining** reveals copper and tin. Until the settlement knows what a vein looks like, that ore stays hidden inside ordinary stone — and once you can mine it, those veins renew as they are worked rather than running dry. Prospecting research is what turns a mountain into a mine.

## More than items: jobs, policies, and palettes

A completed node can hand you far more than a new block:

- **Jobs.** Most early research opens a new worker role — Woodworking gives the Carpenter and Forester, Masonry the Mason, Storage Logistics the Stocker, Town Watch the Guard, Ore Mining the Miner, Agricultural Revolution the Farmer, Stews the Cook, and so on down the list of foragers, hunters, fishers, and fletchers.
- **Crafts & workstations.** Nodes unlock the benches that anchor a craft: the Woodworking Table, the Mason's Bench, the Fletching Station, and the bellows, casting molds, and stone anvil of Metal Working.
- **Storage.** Baskets, the shared Stockpile, and larger storage all wait on research — try to use one too soon and you'll hear *"Your settlement hasn't researched that storage type yet."*
- **Policies.** Certain researches add no item at all — they unlock a **policy** the Chief can enact in the town hall (*"Research unlocks policies."*). Confirmed doctrines include **Roads**, **Extended Shift**, **Workload Share**, **Opinionated Crowd**, **Domestication**, **Agricultural Effort**, **Rallying Speeches**, and **Glory Tales**. See [Government](government.md).
- **Palettes.** Research also unlocks **build palettes** for your architecture. Until you've researched some, the palette screen simply reads *"Research unlocks palettes."* See [Culture & Heraldry](culture-and-heraldry.md).
- **Crises.** A few nodes even open new [crises](crises.md) — knowledge cuts both ways.
- **Era advancement**, as above — the biggest unlock of all.

## Notable early researches

Here is a representative slice of the Ancient-to-Medieval Science tree — the nodes most players touch in their first civilization. Costs rise steeply as you climb; the era-advancing keystones are the priciest of all.

| Research | Era | Cost | What it opens |
|----------|-----|-----:|---------------|
| **Settlement** | Ancient | 0 | The starting node — the Bone Age and the ground everything grows from |
| **Foraging** / **Hunting** | Ancient | 10 / 10 | The Forager and Hunter — the first food off the land |
| **Town Watch** | Ancient | 10 | The **Guard** — a watch that patrols the borders and fights raiders |
| **Storage Logistics** | Ancient | 12 | The Stocker, the Basket, and the shared **Stockpile** |
| **Animal Husbandry** | Ancient | 12 | Breeding and leashing; fences, wool, leather, and eggs |
| **[Herbalism](../antiquity/herbalism.md)** | Ancient | 12 | Poisons, antidotes, darts, the blowgun, and the mortar & pestle |
| **Housing** | Ancient | 24 | The first true [homes](housing.md) — thatch beds and doors, and the housing planner |
| **Agricultural Revolution** | Ancient | 20 | The **Farmer** and crop planting — potatoes, carrots, beetroot, and foresters that replant what they fell |
| **Food Preservation** | Ancient | 16 | Salt and dried meats & fish; adds to your [food](food.md) reserve — see [Cooking & Food](../antiquity/cooking-and-food.md) |
| **Fertilization** | Ancient | 24 | Composter, bone meal, and the manure → dung loop — fed soil that harvests faster |
| **Stews** | Ancient | 5 | The **Cook** and the stone cooking pot — the settlement's first proper meals |
| **Domestic Comfort** | Ancient | 28 | Homes begin asking for light, storage, and a hearth — comforts that draw families |
| **Bartering** | Ancient | 14 | Trade with other settlements via the [Diplomacy](diplomacy.md) tab |
| **[Fletching](../antiquity/fletching-and-archery.md)** | Ancient | 16 | The Fletcher; the Fletching Station and slingshot (bows wait on Archery) |
| **Paving** | Ancient | 24 | Flatten dirt and grass into paths — groundwork the Roads policy later builds on |
| **[Woodworking](../antiquity/woodworking.md)** | Ancient | 24 | **Wood Age**; Carpenter & Forester; sticks, wooden tools, barrels, fences, the Foreman's Rod |
| **[Knapping](../antiquity/knapping.md)** | Ancient | 32 | **Stone Age**; stone tools and the stone spear |
| **[Masonry](../antiquity/masonry.md)** | Ancient | 32 | The Mason; slabs, stairs, walls, bricks, and polished stone |
| **Fishery** | Ancient | 32 | The Fisher; rods and the first patient food |
| **Silviculture** | Ancient | 32 | Foresters tend ordered tree plantations that never strip the land bare |
| **Kilns** | Ancient | 40 | Brick, terracotta, charcoal — the first true furnace, long before metal |
| **[Pottery](../antiquity/pottery.md)** | Ancient | 48 | The Potter; clay pots, buckets, crucibles, mud bricks, plaster |
| **Quarry** | Ancient | 56 | Upgrades Diggers into Quarryworkers; reveals **coal** in stone |
| **Outposts** | Ancient | 56 | Plant a lone banner on distant ground — a claim with no wall to shield it |
| **Ore Mining** | Ancient | 72 | The Miner; reveals **copper and tin** in stone |
| **[Metal Working](../antiquity/metalworking.md)** | Ancient | 80 | The Smith; **Copper Age**; copper & tin tools, bellows, molds, stone anvil |
| **Wall Building** | Ancient | 80 | The Builder and the wall planner — see [Walls](walls.md) |
| **Bronze Age** | Ancient → **Classical** | 120 | Bronze tools and weapons; the **Bronze Age** tool tier; advances your era |
| **Mathematics** | Classical | 80 | Unlocks the **Statistics** tab in the town hall — the settlement can finally see itself clearly |
| **Iron Working** | Classical → **Medieval** | 200 | Iron tools, armor, shields, anvils, buckets — and the **Iron Age**; advances your era |
| **Shearing** | Medieval | 10 | Shears; foragers can gather vines, grass, and leaves |

!!! quote "The point of it all"
    Research is never busywork. Each node is a lever on how your people live — which trade they can take up, which border they can hold, which age they belong to. Choose the levers that fit the civilization you mean to build.

## Where to next

- [Faith](faith.md) — the Devotion tree, raising gods, and how belief feeds your research.
- [Government](government.md) — who becomes Chief and holds the power to direct research and enact policies.
- [Territory & Claims](territory.md) — how advancing an era widens the borders you can hold.
- [Tool Tiers](../antiquity/tool-tiers.md) — the full ladder of tools each tool age unlocks.
