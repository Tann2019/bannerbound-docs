---
title: Workshops & Storage
description: Mark production workshops around a work block, staff them with a Crafter and a Stocker, and connect your storage into a single Stockpile.
---

# Workshops & Storage

<p class="bb-lead">A settlement runs on skilled hands and full shelves. Draw a box around a work block to turn it into a managed <em>workshop</em>, put a crafter to work fulfilling orders, and knit your scattered chests into a single, tidy <em>stockpile</em> your haulers can actually reach.</p>

!!! abstract "The short version"
    - **Mark a workshop** with the **Workshop Orders** rod: two corner clicks around a work block (a Crafting Stone, Fletching Station, and so on).
    - A valid workshop needs a **work block**, **storage** inside, an **enclosed** space, a **reachable path**, and **two blocks of headroom**.
    - Staff it with a **Crafter** (works the station, gains skill) and let a **Stocker** haul the ingredients in.
    - Set what it makes on the **Stock tab**: a **Min** to keep on hand, plus one-off **Orders** that jump the queue.
    - Quality climbs the ladder **Crude → Standard → Fine → Masterwork → Perfect → Legendary**, earned through good gear and a well-played crafting minigame.
    - Bind your chests, barrels, and baskets into one **Stockpile** — but you'll need [research](research-and-eras.md) and **fences** first.

## Marking a workshop

Every workshop starts with the **Workshop Orders** rod. It's the same tool you use for [housing](housing.md), pointed at production instead: you sweep out a box around a **work block**, and everything inside becomes a managed region your citizens will tend.

Hold the rod and:

- [ ] **Right-click one corner**, then the opposite corner, to mark a box. You'll get a confirmation naming the new workshop.
- [ ] **Shift-right-click inside** a finished workshop to open its management menu.
- [ ] **Shift-left-click** a box to remove it. Remove the last box and the workshop is deleted and its workers freed.

A workshop can be more than one box — add extra boxes to wrap an L-shaped building, so long as each new box **touches** the rest. Boxes can't overlap a [house](housing.md) or another marked area, and the region has to sit inside your [settlement's](settlements.md) claimed [territory](territory.md).

!!! tip "One rod, many buildings"
    The Workshop Orders rod, the housing rod, and the marking tools all speak the same language: click two corners, shift-click to manage, shift-left-click to erase. Once you've marked your first workshop the rest are muscle memory.

### What makes a workshop *valid*

Marking the box is only half the job. Open the workshop menu and check the **Status** line — a workshop only runs when it reads **Valid**. Everything else is a to-do list:

| Status reads | What it means | The fix |
| --- | --- | --- |
| **No work block inside** | The box has no station a crafter can work | Include a Crafting Stone, Fletching Station, Mason's Bench, etc. |
| **No storage inside** | Nowhere to pull ingredients or drop output | Place a chest, barrel, or basket inside the box |
| **Not enclosed** | The region is open to the world | Wall and roof it in so it reads as a room |
| **Marked blocks are disconnected** | Multiple boxes that don't touch | Re-mark so the boxes share a face |
| **Citizens can't reach a work block** | No walkable path to the station | Clear the doorway and floor so citizens can walk in |
| **Citizens can't reach the storage** | Same problem, for the containers | Open a path to the chests |
| **Roof is too low** | The station is cramped | Give the work block **two blocks of headroom** |

There's also a size limit per box — if a side runs too long the rod will refuse the box and tell you the maximum. Keep workshops room-sized, not warehouse-sized.

!!! warning "Two blocks of headroom is real"
    A crafter needs to *stand* at the station. If your ceiling sits one block above the work block, the workshop stays invalid with **"Roof is too low over the work block."** Give the tile above the station clear air.

## The workshop types

The **type** of a workshop is decided by the work block inside it — you don't pick it from a menu. Each type draws from its own recipe list, wants its own tools, and (for the skilled crafts) unlocks its own specialist job once you've [researched](research-and-eras.md) it.

| Workshop | Work block | Who works it | Learn the craft |
| --- | --- | --- | --- |
| **General Crafts** | Crafting Stone | Crafter | [Founding basics](../getting-started/founding-a-settlement.md) |
| **Fletchery** | Fletching Station | Crafter | [Fletching & Archery](../antiquity/fletching-and-archery.md) |
| **Woodworking** | Woodworking Table | Woodworker | [Woodworking](../antiquity/woodworking.md) |
| **Masonry** | Mason's Bench | Mason | [Masonry](../antiquity/masonry.md) |
| **Pottery** | Pottery Slab | Potter | [Pottery](../antiquity/pottery.md) |
| **Tannery** | Tanning Rack | Tanner | [Tannery](../antiquity/tannery.md) |
| **Kitchen** | Stone Cooking Pot | Cook | [Cooking & Food](../antiquity/cooking-and-food.md) |
| **Brewery** | Fermentation Trough | Brewer | [Brewing](../antiquity/brewing.md) |
| **Smithy** | Stone Anvil | Smith | [Metalworking](../antiquity/metalworking.md) |

The two simplest types — **General Crafts** and **Fletchery** — are the ones you'll meet first, worked by the plain **Crafter** role. The rest are skilled trades: research the craft, and a specialist job (**Woodworker**, **Mason**, **Potter**, **Tanner**, **Cook**, **Brewer**, **Smith**) opens up. Try to assign someone to a workshop whose craft you haven't researched yet and the menu will tell you: *"needs its craft researched before a worker can be assigned here."*

!!! note "One work block per room"
    A workshop's **type is derived from the stations inside it**, and its worker capacity equals the **number of work blocks** it holds — two benches means two crafter slots (*Workers: 0 / 2*). Put two *different kinds* of work block in one box, though, and the room loses its specialty and simply reads **Workshop**. Auxiliary blocks don't count against this: a kitchen's campfires beneath its pots, or a smithy's bloomery and bellows, are supporting equipment, not stations — a smithy with an anvil, a bloomery, and storage stays a clean **Smithy**.

## Staffing: the Crafter and the Stocker

A marked, valid workshop still produces nothing until someone works it. Two [jobs](jobs-and-labor.md) make production flow:

**The Crafter** stands at the work block and actually makes things. Open the workshop's **Workers** tab, pick an available [citizen](citizens.md) from the list, and **Assign**. From then on the crafter pulls ingredients from the workshop's storage and fulfills its orders without stopping to rest at the station — and **gains skill** every time they craft. The menu shows how many workers the workshop holds (*Workers: 1 / 2*) and its **Appeal**; a pleasant, well-built workshop doesn't just keep its crafters happy (*"I love working in such a lovely workshop."*) — happier workers also **learn their craft faster**, so decorating a production building buys you skill, not just mood.

**The Stocker** never touches a station — they're your hauler. A stocker carries ingredients *to* workshops that need them and moves finished goods *between* stores. When a workshop's order is short an ingredient, it's the stocker who fetches it. Without at least one stocker, your crafters will sit idle waiting on materials that never arrive.

!!! tip "The unsung stocker"
    New players staff crafters and forget haulers — then wonder why the smithy is "waiting on inputs." A workshop with a blocked order is skipped until its materials show up, and *something has to bring them*. Keep a stocker or two on the [labor board](jobs-and-labor.md) as your settlement grows.

!!! note "Pinning a worker to one station"
    If a workshop holds **more than one kind of station**, each worker's row on the **Workers** tab grows a small station toggle — a station's name, or **Any**. Pin a crafter to a single station and their experience piles up in that one craft instead of smearing across whichever bench happens to be free. A single-station workshop has nothing to choose, so the toggle never appears.

### Skill and how crafters grow

Crafters climb a skill ladder as they work: **Novice → Apprentice → Journeyman → Veteran → Master**. A citizen's skill is shown on their job panel — it's the hands-on experience they've built up at that craft. Skill isn't permanent, though: citizens **re-skill over time** when you move them between jobs, so a veteran mason you reassign won't stay one forever. Keep your best crafters on the bench that suits them.

## Quality of crafted goods

Skilled crafts don't just come out "an item" — they come out at a **quality**, and quality is worth chasing. The ladder runs:

| Tier | Feel |
| --- | --- |
| **Crude** | Rushed, unskilled work |
| **Standard** | Solid, everyday goods |
| **Fine** | Noticeably better than average |
| **Masterwork** | The pride of a skilled hand |
| **Perfect** | Flawless craftsmanship |
| **Legendary** | The stuff of stories |

Two things set where a craft lands on that ladder: the **gear your crafter is equipped with**, and — on hands-on crafts — **how well the crafting minigame is played**. (Quality comes from the *tools the worker carries*, not from which job they hold.) A [fletcher](../antiquity/fletching-and-archery.md) refines an arrow through a *stretch* timing minigame; a [potter](../antiquity/pottery.md) spins clay on the slab; a [mason](../antiquity/masonry.md) dresses a whole batch of stone with rhythmic chisel strikes; and a [smith](../antiquity/metalworking.md) cold-hammers a part on the Stone Anvil, where the timing of the strikes sets the tool's quality. Play the minigame well with good gear in hand, and quality climbs.

!!! example "From Crude to Fine"
    A crafter at a plain Fletching Station with basic gear will mostly turn out **Crude** and **Standard** arrows. Give that same worker better fletching equipment and a clean run at the stretch minigame, and **Fine** and beyond start appearing in the barrel. Quality isn't a dice roll you can't influence — it's the payoff for good tools and a steady hand.

## Station requirements: the fiddly extras

Beyond the general "*is this a valid workshop*" checklist, individual crafts need their **station** properly set up. A workshop can be enclosed, staffed, and stocked and *still* refuse to produce because the station itself is missing a piece. Watch for these:

| Status reads | The craft needs | Typical fix |
| --- | --- | --- |
| **Missing heat source** | Fire or a forge for the recipe | Light a campfire or fuel the bloomery |
| **Missing crafting surface** | A working surface for the craft | Add the surface the recipe expects |
| **Missing a required tool in storage** | A specific tool kept in storage | Stock the tool — e.g. a **saw** for [woodworking](../antiquity/woodworking.md) |
| **Missing a clay tank to cure hides** | A [tannery](../antiquity/tannery.md) can't cure hides | Place a **Clay Tank** and fill it with curing liquid |

A couple of crafts have their own structural demands worth remembering: a **[Pottery](../antiquity/pottery.md)** workshop needs a **Kiln** inside to fire its wares, and a **[Woodworking](../antiquity/woodworking.md)** workshop needs a **saw** stocked in its storage before the crafter can start sawing.

!!! warning "The tool has to be *in the storage*"
    A required tool like a saw isn't held in the crafter's hand — it lives in the workshop's storage, where the station can find it. Craft it, drop it in the chest inside the workshop, and the "missing tool" warning clears.

## The Stock tab: what a workshop makes

Open a workshop and switch to the **Stock** tab to tell it *what* to produce. Each craftable **output** gets two numbers:

- **Min** — the standing stock level to keep on hand, counted **settlement-wide**. The workshop only tops up when that item's *total across every container in your territory* — stockpiles, other workshops, even loose chests, barrels, and baskets — drops below the Min. Quality doesn't enter into it: eight *crude* arrows satisfy a Min of eight arrows. This is your "always have some" dial.
- **Orders** — a one-off batch you want *now*. Orders run first-in, first-out and **outrank Min production** — a placed order is crafted before the workshop goes back to maintaining its minimums.

Click the numbers to nudge them; **shift-click** jumps them in steps of eight for setting big batches fast. A blocked order (one that's short an ingredient) is skipped until its materials arrive, then picked back up — so it's safe to queue ambitious orders and let the stockers catch up.

!!! note "The gray *+n*: orders you never placed"
    Sometimes a workshop needs an intermediate good it can't make itself — a fletchery short on the **plant string** its arrows require, say. Rather than stall, it **auto-queues that ingredient on the workshop that does make it** (here, your general-crafts stone), and it shows up there as a gray **+n** beside the gold count of your own orders. These derived orders ride *behind* your gold ones, and the production chain manages them for you: you can't nudge them with the ± buttons, and they quietly clear themselves the moment the need disappears.

!!! tip "Min for staples, Orders for projects"
    Keep a small **Min** of everyday goods — cordage, bricks, basic tools — so your settlement never runs dry. Reach for **Orders** when a build or an expedition needs a specific pile of something *right now*.

---

## Storage: the Stockpile

Loose chests scattered around your settlement are hard for haulers to track. The **Stockpile** block solves this: it binds up to **eight** nearby containers — chests, barrels, or baskets — into **one logical store** that your [stockers](jobs-and-labor.md), workshops, and trade all treat as a single set of shelves.

To build a working stockpile:

- [ ] **Research [Storage Logistics](research-and-eras.md)** — without it the block simply won't function (*"Your settlement hasn't researched Storage Logistics yet."*).
- [ ] **Fence in an area** with fences or walls, add a **fence gate** so citizens can walk in, and put a **roof** over it to shelter the goods.
- [ ] **Place the Stockpile block inside** that enclosure, along with your containers.
- [ ] Open the Stockpile and hit **Detect** to connect the containers it can see (up to eight).

The menu spells out its state: *"Enclosure: fenced & roofed"* when the ring is good, and a specific complaint when it isn't — a **solid block breaking the fence ring**, a **missing fence gate**, **no roof**, an **area that's too large or has a gap**, or simply **no containers inside yet**. Chase the message until it reads **"Stockpile ready."**

!!! danger "You need fences first — and that means two more researches"
    A stockpile depends on a proper **fenced enclosure**, and you can't craft fences out of thin air. Before a stockpile will actually work you also need **[Animal Husbandry](research-and-eras.md)** and **[Woodworking](../antiquity/woodworking.md)** — the pair that lets you make **fences** in the first place. Then those fences have to be built **around the stockpile**, enclosing it together with its containers. It's easy to research Storage Logistics, place the block, and be baffled that nothing happens — the missing piece is almost always *fences you can't yet build.*

### Connected, sheltered, searchable

Once ready, the Stockpile is your settlement's pantry in one window. It shows how many containers are connected (*3 / 8*), how many slots are free, and a **Search** box for finding a good across all its shelves at once. Citizens **deposit** finished goods here and **take** ingredients from here, and you can tune how often the store cycles its contents — pick a **30s**, **1 min**, or **3 min** interval, a short one to keep things brisk or a longer one to ease the load on a busy settlement.

Only the owning settlement can use a stockpile — with one pointed exception: an enemy you're in an **active war** with can raid it. Keep valuables behind your [walls](walls.md).

### Show for trading

Each stockpile has a **"Show for trading"** toggle. Flip it **On** and that store becomes a **trading stockpile** — the pool that [diplomacy](diplomacy.md) draws from when you strike a deal, and where incoming trade shipments are delivered. A trade offer is only as good as the goods behind it: if your trading stockpiles can't cover what you promised, the deal won't go through (*"Your trading stockpiles can't back that offer."*).

!!! note "Trade wants a dedicated shelf"
    Cross-settlement [trade](diplomacy.md) needs the **Bartering** research, peace with your partner, and a **trading stockpile on both sides**. A common setup is one everyday stockpile for your own economy and a second, trade-flagged one holding only what you're willing to sell.

## Where to next

- [Jobs & Labor](jobs-and-labor.md) — assign Crafters, Stockers, and specialist trades on the labor board.
- [Research & Eras](research-and-eras.md) — unlock Storage Logistics, Bartering, and each skilled craft.
- [Woodworking](../antiquity/woodworking.md) & [Masonry](../antiquity/masonry.md) — the crafts behind your first specialist workshops.
- [Diplomacy](diplomacy.md) — turn a trading stockpile into deals with your neighbors.
