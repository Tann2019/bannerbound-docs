---
title: Jobs & Labor
description: How to put citizens to work — the Foreman's Rod, every gatherer and workshop job, tools and drop-offs, and the Labor board that runs it all.
---

# Jobs & Labor

<p class="bb-lead">A settlement is only as strong as the hands that feed it. This is how you point those hands at the world — mark a forest, a field, a pen, a vein — hand your people the right tool, and tell them where to put what they gather.</p>

!!! abstract "The short version"
    - Craft a **Foreman's Rod** — it turns menu decisions into real places in the world.
    - Open a citizen's **Job tab**, pick a job, then give them the two or three things that job needs: a **tool**, a **source** (field, pen, seeds), and a **drop-off** (where their goods land).
    - Mark work regions with the rod: **shift-right-click** to pick the job type, **left-click point A**, **right-click point B**, **shift-left-click** to remove. Everything must sit inside your **claimed chunks**.
    - A worker missing any requirement just goes **idle** — the Job tab tells you exactly what's wrong.
    - The **Labor board** in the Town Hall balances everyone automatically by priority; turn it off to hand-assign. Under **anarchy**, you can only *ask* citizens to switch jobs, and they may refuse.

## The Foreman's Rod

Most jobs live half in a menu and half in the world. The **Foreman's Rod** is the bridge. When a screen asks you to mark a field, a pen, a drop-off, or a work site, the rod is how you answer — your next click in the world becomes the reply.

Craft one on a [Crafting Stone](../antiquity/knapping.md) from **one stick** and **one plant fiber**. Keep it in your inventory; the Job tab and Labor board will tell you "(need a Foreman's Rod)" whenever one is missing.

### Marking a work region

Some jobs (diggers, quarry crews, tree plantations) work an *area* you paint on the ground:

- [ ] **Shift-right-click** with the rod to open the picker and choose a workstation type.
- [ ] **Left-click** a block to set **Point A**.
- [ ] **Right-click** another block to set **Point B** — the region between them is committed.
- [ ] **Shift-left-click** inside a region to remove it.

The rod's tooltip narrates the whole thing — which workstation is chosen, where Point A sits, and the size of the region once committed.

!!! warning "It must be your land"
    A region has to sit **entirely within your settlement's claimed chunks**. Stray over the border and the rod refuses with *"Selection must be entirely within your settlement's claimed chunks"* — or *"That land belongs to another settlement"* if a neighbour owns it. Two regions can't overlap, and there's a size limit per selection. See [Territory](territory.md) for how to claim more ground.

### Marking a point (pens, mines, guard posts)

Other jobs bind to a single spot rather than a painted box. For these you point the rod at the block itself:

- A **herder's pen** is bound by right-clicking inside a fenced enclosure.
- A **miner's** or **digger's** deposit is marked by clicking an ore boulder or stone deposit in the chunk.
- A **guard post** is placed by right-clicking where you want a guard to stand watch.

For posts, pens, and deposits, **shift-right-click** the marker to reassign it to a *specific* worker (or open it to everyone), and **shift-left-click** to remove it. A pen or deposit will tell you if it's already claimed by another worker.

## Putting one citizen to work

Every job starts the same way. Walk up to a citizen (or click them from the Town Hall **Citizens** list) and open their **Job tab**.

1. Click **Assign Job ▾** and pick an unlocked job. The citizen is now **pinned** to it — the labor balancer won't touch them until you release them back to **Auto-assign**.
2. Give them their **tool**, if the job needs one — drop it in the tool slot, or let them pull it from marked tool storage.
3. Mark their **drop-off** — click the drop-off row, then right-click a chest, basket, barrel, or stockpile with the rod.
4. Add whatever **source** the job needs (seeds, a pen, a field, water).

The Job tab is also your live dashboard: it shows the worker's current **status**, whether a tool is set, whether a drop-off and storage are available, and any job-specific options.

!!! tip "Pin the tutorial"
    The Chronicle has a pinned **Jobs & Storage** tutorial that walks you through assigning one worker and wiring up their storage. Pin it from the Chronicle header and the checklist rides along in the side tracker while you set things up in-world.

## The three things every worker needs

A worker is only "ready" when their requirements are all satisfied. Miss one and they stand around idle.

=== "A tool"

    Most gatherers need a tool of the right kind — an axe for a Forester, a hoe for a Farmer, a pickaxe for a Miner. Put one in the worker's tool slot, or mark a **tool storage** block for that worker type so anyone in the role equips from it automatically.

    The tool has to match your **tool age**. Hand a worker something their era can't wield yet and you'll be told: *"That tool is too advanced for your current tool age."* Your tool age climbs as you research better toolmaking — see [Tool Tiers](../antiquity/tool-tiers.md).

=== "A source"

    Many jobs draw from something you provide. Farmers need **seed storage** to plant from and a **field** to work. Herders need a fenced **pen**. Diggers and plantation Foresters need a **region** marked with the rod. Without the source, there's simply nothing for them to do.

=== "A drop-off"

    A drop-off is where the worker deposits what they produce. Any **chest, basket, barrel, or stockpile** inside your territory works, as long as your settlement has researched that storage type. The rod will refuse anything that isn't a valid, claimed storage block: *"That isn't a valid drop-off in your territory."*

### Tool storage and preferred storage

You don't have to hand-feed tools to every citizen. Two shortcuts scale this up:

- **Tool storage** (per worker type) — mark a chest and every worker of that role equips their tool from it first. Stockers even deliver hauled or crafted-to-order tools straight there.
- **Preferred storage** (set from the Labor board) — a single default depot for any gatherer that lacks its own drop-off. They deposit here *and* draw their job tool from it. It's the fastest way to get a young settlement working without micromanaging each worker.

## Reading work statuses

Whenever a worker isn't producing, their status tells you why. Learn to read these at a glance:

| Status | What it means | Fix |
|---|---|---|
| **Working** / **Hauling to drop-off** | All good — producing or carrying goods home | — |
| **Idle — no tool** | No valid tool in the slot or in tool storage | Give a tool of the right age |
| **Idle — no drop-off** | No storage marked to deposit into | Mark a drop-off with the rod |
| **Idle — drop-off full** | Storage has no room left | Add storage or clear the chest |
| **Idle — nothing to do** | No work in reach (empty region, nothing to gather) | Mark a source or move the region |
| **Idle — needs saplings / needs seeds** | Out of planting stock | Restock the seed/sapling source |
| **Resting — no stamina** | Exhausted; will recover | Let them rest; check [Housing](housing.md) |
| **Waiting for growth…** | Crops or trees aren't ripe yet | Nothing — just time |
| **Refusing to work** | On strike from low happiness | Improve mood — see [Citizens](citizens.md) |
| **Halted — banner is down** | The settlement banner was lost | Re-plant your banner |
| **Sleeping / Socializing (dusk)** | Off the clock for the night | Normal daily rhythm |
| **Expecting — not working** | A citizen expecting a child steps back from labor | Nothing — temporary |

## The gatherer jobs

These are the workers who bring raw wealth in from the land. Each is unlocked by its own [research](research-and-eras.md) (linked below) and directed from the Job tab.

| Job | Marks | Brings home | Needs |
|---|---|---|---|
| **Forester** | Log drop-off / plantation | Logs, saplings, sticks | Axe |
| **Farmer** | Field + granary | Crops & seeds | Hoe, seed source |
| **Fisher** | Spot near water | Fish (and treasure, later) | Spear *(optional)* |
| **Forager** | Basket / preferred storage | Wild food, fibers, herbs | No tool — Shearing unlocks more targets |
| **Herder** | A fenced pen | Meat now, or a growing herd | Rope, a valid pen |
| **Hunter** | A camp on unclaimed land | Meat, hide, feather | Spear or bow |
| **Digger → Quarryworker** | A region to dig/cut | Dirt & gravel; then stone & coal | Shovel; pickaxe for quarrying |
| **Miner** | An ore deposit | Ore for smelting | Pickaxe |
| **Guard** | A guard post | Safety on the border | A fighter's kit |

### Forester

The first job most tribes direct, because nearly every craft needs wood. Assign a **Forester**, give them an axe, and mark a **log drop-off**. They fell trees and haul the logs home.

- **Extra drops** toggle — *Kept* stores the saplings, apples, and sticks a tree drops; *Logs only* clears the leaves and discards the rest.
- **Preferred wood** — click to have them favour a particular log type.
- Once your people can plant, a Forester tucks a **matching sapling** into each stump, so a worked grove regrows instead of being stripped bare.
- **Silviculture** turns loose wood-gathering into a **managed plantation** — mark a plantation region with the rod and the Forester tends it like a farm.
- **Lumberjacking** lets them fell the forest's giants — mega trees like dark oak, giant jungle, and mega spruce.

See [Woodworking](../antiquity/woodworking.md) for what all that timber becomes.

### Farmer

The slowest job to set up and one of the most reliable once running. A Farmer needs the full kit: a **hoe**, a marked **field**, a **seed source** to plant from, and a **harvest drop-off** (the granary). Mark a field with the rod, then the Farmer tills, sows, and harvests it on a loop.

- **Sneak + right-click** an edge with the rod to **expand an adjacent field** rather than starting a new one.
- Click a field to set which **crop** it grows and which farmer works it.
- With **Fertilization** researched, flip **Use Fertilizer: On** and the Farmer applies bone meal to speed crops along.

Fields answer hunger slowly but steadily — read [Food](food.md) for how they feed the settlement.

### Fisher

Water into supper. A **Fisher** works near claimed fishable water and drops the catch at nearby storage — one of the cleanest early answers to a starvation crisis, since stocked fish start feeding people before fields or herds mature.

- A **spear** in the tool slot is optional; a fisher will work bare-handed, just slower. A better spear speeds them up.
- **Deep-Sea Lures** lets master fishers in open water occasionally pull up **treasure and curiosities** alongside the ordinary catch.

### Forager

Your cheapest, earliest supply line — no fields or pens required. A **Forager** walks the unclaimed land beyond your borders gathering wild growth, and quietly keeps your crafting and farming chains stocked with fibers and seeds.

Open the **Targets** picker and toggle exactly what they collect:

| Target | Notes |
|---|---|
| Berries · Flowers · Tall Flowers · Mushrooms | Wild food and colour |
| Wild Crops | Untended edible crops |
| Sticks & Fibers | Feeds fletching and crafting |
| Vines · Grass · Leaves | **Locked until Shearing** |

The **Shearing** research ("sharpen flint into a crude blade and the forest opens up") unlocks the vine, grass, and leaf targets. Later, **Herbalism** lets foragers gather signature herbs — poison plants and the remedies that cure them.

### Herder

A living food reserve. A **Herder** uses **fiber rope** to raise and breed penned animals. Keeping the herd alive is passive livestock food; **culling** trades that future income for meat right now.

Build a pen in claimed grassland and bind it with the rod. A valid pen must be **fully enclosed** and contain:

- [ ] a **fence gate** to get in and out
- [ ] **water** inside (a drinking spot)
- [ ] **grass** inside for grazing
- [ ] **livestock** in the chunk to raise

Open the **Herd & harvest** panel to set **"keep N adults"** — the herd grows toward that number, then surplus adults are harvested into your **harvest storage**. Choose *Auto* to breed the pen to full and never cull. Note the two storage roles: **food storage** is needed to *breed*, **harvest storage** is needed to *cull*.

### Hunter

Unlike a herder, a **Hunter** ranges out onto **unclaimed land** to take wild game — meat, hide, and feather that no pen can provide. Mark a hunter's camp and choose which **prey** to pursue.

The hunt is hands-on for the AI: calm animals are stalked in a crouch, while a spooked one flees and must be chased. A **spear** opens with a thrown strike; **Archery** lets a hunter drop game from the treeline before it ever notices. How the kill is made even affects the **hide quality** it yields at the [Tannery](../antiquity/tannery.md).

### Digger → Quarryworker

Your earthmovers. Hand a citizen a **shovel**, assign **Digger**, and mark a region — they clear dirt, sand, and gravel to flatten and reshape the land. Digging is the first labor that changes the terrain itself.

The **Quarry** research promotes them into **Quarryworkers**, cutting **stone, granite, diorite, andesite, tuff, and coal ore** from the living rock. **Extensive Quarries** lets crews carry orders a short way onto **unclaimed ground** near your borders, biting deeper than a claim alone allows. Quarried stone and coal feed the kiln, the [Bloomery](../antiquity/metalworking.md), and your building projects.

### Miner

A **Miner** reads the rock for metal. First, **Early Prospecting** reveals hidden ores in stone — the rust of iron, the green of copper, the dull glint of tin. Then **Ore Mining** puts miners to work.

A miner doesn't destroy blocks. They **chip at an ore deposit**, swapping it to a mined state and letting the vein **regenerate over time** — so a deposit is *worked*, never spent. Mark the deposit like a pen (the rod tells you if there's no workable ore in the chunk), give a **pickaxe**, and their ore feeds the smelting chain toward ingots and bronze.

### Guard

The settlement watch. A **Guard** patrols your borders and fights off raiders and hostile mobs — far steadier in a brawl than an ordinary citizen, and they **won't be drawn off** into the wild. Place a **guard post** with the rod where you want one to stand; shift-right-click the post to assign a specific guard or open it to all.

Guards are your answer to [Barbarians](barbarians.md) and hostile neighbours. Pair them with [Walls](walls.md) for a border that holds.

## Workshop workers: Crafter & Stocker

Two roles keep your buildings humming rather than the wilds:

- A **Crafter** works a bound workshop, filling its orders and gaining skill over time.
- A **Stocker** hauls goods between stores and workshops so orders never stall for want of parts — and delivers tools to worker tool storage.

Both are covered in depth on the [Workshops](workshops.md) page, including how to bind a workshop and queue its orders.

## The Labor board

Open the Town Hall and switch to the **Labor** tab. This is where you stop assigning citizens one at a time and let the settlement run itself.

### Worker priority

Jobs are listed in **priority order**. The higher a job sits, the more workers it gets first. **Drag to reorder** — citizens **re-skill over time** to match, drifting from lower-priority work into higher. Toggle a job **Off** and it drops to zero workers, who re-skill into whatever's still on.

### Per-job caps

Each job has a **Cap** — the most workers it may hold. Set **-1** for no limit. When a job hits its cap, surplus workers **cascade** down to the next job that still has room, so nobody sits idle just because their favourite trade is full.

### Auto-assign

**Auto-assign: On** hands the whole workforce to the balancer, distributing citizens by your priority order and caps. Turn it **Off** (governments only) to **hand-assign** each citizen yourself from their Job tab — useful when you want precise control over who does what.

### Preferred storage

The **Preferred storage** button sets a default depot for gatherers that don't have their own drop-off. They deposit there and pull their job tool from it — a one-click way to wire up a whole workforce.

!!! warning "Anarchy: you can ask, not order"
    Without a [government](government.md), you have no true labor command. You can only **request** that a citizen switch jobs — and they **may refuse**. Just-refused citizens need a minute before you ask again. You can still mark drop-offs and let people gather freely, but to *order* specific jobs, form a government first. This is one of the strongest reasons to leave anarchy behind.

## Where to next

- [Workshops](workshops.md) — bind buildings, queue orders, and put Crafters and Stockers to work.
- [Food](food.md) — how farmers, fishers, foragers, herders, and hunters keep everyone fed.
- [Territory](territory.md) — claim the chunks your work regions have to sit inside.
- [Tool Tiers](../antiquity/tool-tiers.md) — climb the tool ages so your workers can wield better gear.
