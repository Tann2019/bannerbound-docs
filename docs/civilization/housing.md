---
title: Housing & Appeal
description: Mark homes with the House Block and Housing Orders, meet each home's needs, and raise the beauty of the world around your people.
---

# Housing & Appeal

<p class="bb-lead"><em>A citizen without a bed is a citizen thinking about leaving. Give them four walls, a warm fire, and a view worth waking up to — and watch your settlement bloom.</em></p>

!!! abstract "The short version"
    - Place a **House Block** inside a finished room, then use **Housing Orders** to mark two corners around a bed. The first box must contain a bed.
    - A home must be **enclosed** (walls + roof), **connected**, hold a **bed**, and be small enough for your **era** — press **Detect** on the House Block to let the game find the room for you.
    - Meet the home's **Needs**: Lighting, Storage, a lit Campfire, Cooked food, and Charcoal (the last two live in the home's own chest).
    - Roomier homes are happier: **Spacious → Comfortable → Snug → Cramped**.
    - **Beauty** matters too. Pretty blocks around a home or [workshop](workshops.md) raise happiness and worker output; ugly ones drag it down.

## Why homes matter

Every adult [citizen](citizens.md) wants a place to call their own. A resident with a good home thinks *"I love my house!"*; one without wanders your streets thinking *"I don't have a place to call home"* — and unhappy citizens work poorly, and eventually pack up and leave.

A **home** is not just any room. It is a space you deliberately mark, that the game then checks against a short list of requirements. Get those right and the home turns **Valid**; miss one and the House Block will tell you exactly what is wrong.

## The House Block

The **House Block** is the anchor for a home. Everything about that dwelling — its status, its residents, its needs, its beauty — is read and reported through this one block.

- [ ] Claim the ground first. The room must sit inside your [settlement's](settlements.md) [claimed territory](territory.md) — a House Block placed on unclaimed land has nothing to belong to.
- [ ] Build (or find) an enclosed room with a **bed** in it.
- [ ] Place the **House Block** somewhere inside that room. It becomes the home's anchor.
- [ ] **Right-click** the House Block to open its status screen and read what the home still needs.

The status screen is your dashboard for that dwelling. It shows the home's **Status**, its **Appeal**, its living **Space** (and how much room each bed gets), overall **Happiness**, the **Needs** checklist, and the current **Residents** — plus a **Detect** button.

## Marking a home with Housing Orders

The House Block anchors a home, but you still have to tell the game *which blocks* make up that dwelling. That is the job of **Housing Orders**.

Hold Housing Orders and **right-click two opposite corners** to draw a box around your room. The very first box you draw **must contain a bed** — that bed is what turns a marked region into a home.

| Action | What it does |
| --- | --- |
| Right-click two corners | Draws a box; the first box (with a bed) **creates the home** |
| Right-click two more corners | Adds another box, extending the home (each new box must touch the existing region) |
| **Shift**-right-click inside a home | Opens the **resident manager** to assign or remove residents |
| **Shift**-left-click a box | **Removes** that box; removing the last box deletes the home and evicts its residents |

!!! tip "Let Detect do the drawing"
    Marking corners by hand is fussy. Instead, build your enclosed room, place the House Block inside, right-click it, and press **Detect**. The game flood-fills the interior and traces the walls for you, turning your real room into the home region it understands. If a corner ends up wrong, the [Home Marker Rod](#fine-tuning-with-the-home-marker-rod) can trim or extend it.

Each box has limits — it can only be so many blocks on a side, a home can only hold so many boxes, and boxes must all connect into one structure. A box that is all air, or that overlaps a [workshop](workshops.md) or another home, is rejected with a message telling you why.

## What makes a home valid

Once a home is marked, the House Block reports one of these statuses. Only **Valid** homes house citizens.

| Status | Meaning | Fix |
| --- | --- | --- |
| **Valid** | Enclosed, connected, has a bed, fits your era | Nothing — assign residents! |
| **Unmarked** | No region marked yet | Use Housing Orders or press Detect |
| **No beds** | Marked, but no bed inside | Place a bed inside the marked region |
| **Broken — no House Block** | The marked region doesn't include its own House Block | The House Block must sit inside the home it anchors |
| **Broken — disconnected** | The marked blocks form more than one separate structure | Merge the boxes into one connected shape |
| **Broken — not enclosed** | Missing walls or roof | Close every wall and cap the roof |
| **Too big for your era** | Larger than your era allows | Build smaller, or research larger homes |

### Enclosed, connected, and roofed

"Enclosed" means the interior is genuinely sealed: every open space inside needs a solid block somewhere above it as a **roof**, and the **walls** must have no open gaps. Small openings — a window's worth — are fine, but leave a doorway-sized hole in a wall and the game can't find an enclosed house at all.

!!! warning "Open walls read as 'too big'"
    If a wall has a real gap, the check leaks out into the open world and the home fails as **not enclosed** or **too big**. If Detect complains it *"couldn't find an enclosed house — there's an open wall or a gap too big to be a window,"* walk the perimeter looking for the missing block, not the roof.

### Fitting your era

Homes have a maximum size that grows as your civilization advances. In the earliest era your people make do with humble one-room dwellings; **research larger homes** through [Research & Eras](research-and-eras.md) and you can mark grander houses without them turning **Broken — too big**. A home that outgrows your era stays broken until you either shrink it or unlock the space.

## The home's Needs

A valid, enclosed home still has to be *livable*. The status screen lists a short **Needs** checklist — each one shows **Met** or **Not met yet**. Satisfy them all for a genuinely happy resident.

| Need | How to satisfy it |
| --- | --- |
| :material-lightbulb-on: **Lighting** | Place a torch, lantern, or other bright light source inside the home |
| :material-treasure-chest: **Storage** | Place a chest or barrel inside the home |
| :material-campfire: **Campfire** | Build and **light** a campfire inside the home |
| :material-food-drumstick: **Cooked food** | Keep cooked food in the home's **own** chest or barrel |
| :material-fire: **Charcoal** | Keep charcoal in the home's **own** chest or barrel |

!!! warning "Stock the home's own storage — not the settlement stockpile"
    Cooked food and charcoal must sit in a chest or barrel *inside that home*, not in your central stockpile. Each dwelling keeps its own pantry and fuel. If the Cooked food or Charcoal need won't turn green, check that the food and charcoal are physically stored inside those four walls — a citizen who *"went to bed hungry"* is a citizen with an empty home chest.

The [Campfire](../antiquity/cooking-and-food.md) and cooked food ties housing directly into your kitchen: as long as your cooks are turning out meals and someone stocks each home, the fire stays warm and the pantry stays full.

## Living space & crowding

A home shares its enclosed room between the beds inside it. The more space each bed gets, the more comfortable the resident — the status screen sums it up in one word:

=== "Roomier"

    | Tier | Feel |
    | --- | --- |
    | **Spacious** | Plenty of room to breathe — the happiest homes |
    | **Comfortable** | A pleasant, well-proportioned dwelling |

=== "Tighter"

    | Tier | Feel |
    | --- | --- |
    | **Snug** | Cozy, but starting to feel close |
    | **Cramped** | Too many beds jammed into too little room — happiness suffers |

The screen spells out the exact math for that home — *"so many blocks of enclosed room shared between so many beds"* — so you can see at a glance whether to add a bed or add a wing. Cramming a second and third bed into a tiny hut is tempting early on, but a **Cramped** rating eats away at the very happiness the home is meant to provide.

!!! tip "One good house beats three shacks"
    If you're short on homes, it's usually better to build one **Spacious** house with a couple of beds than to scatter cramped single-bed boxes. You spend fewer blocks on walls, and every resident lands in a happier tier.

## Managing residents

**Shift**-right-click inside a home with Housing Orders — or open the House Block and use its resident panel — to assign citizens. You'll see a list of your settlement's citizens, each showing how far they live from this house, so you can move someone closer to their [job](jobs-and-labor.md).

- A home only accepts residents once it is **Valid** — an unenclosed or bedless house has *"no spare beds"* to give.
- A home can hold as many residents as it has **beds**. Add beds (and space) to house more.
- Children can't be assigned on their own; they live with family.

## Appeal & Beauty

Homes don't exist in a vacuum. The blocks *around* a home — and around every [workshop](workshops.md) — add up to an **Appeal** rating for that spot. Beautiful surroundings lift the mood of the people who live and work there, raising **happiness** and, at workshops, **worker output**. Squalor does the opposite.

Appeal is graded on a nine-step scale, from ghastly to glorious:

<div class="bb-scale" markdown>

**Atrocious** · Repulsive · Disgusting · Unappealing · **Bland** · Pleasant · Attractive · Stunning · **Breathtaking**

</div>

**Bland** sits in the neutral middle — a plain box of cobblestone. Everything below it is actively unpleasant; everything above it is a place people are glad to be.

### What raises and lowers appeal

Every block carries a small appeal weight, on a hidden scale running from roughly −1 (hideous) to +1 (lovely). The blocks near a home or workshop are tallied into its rating, so decoration is never *just* decoration.

| Block | Effect on appeal |
| --- | --- |
| Bell, Blue Orchid, Lantern, Poppy, Dandelion | Strongly beautiful |
| Glass, Flower Pot, Bookshelf, Chiseled Stone Bricks, Sea Lantern | Beautiful |
| Stone Bricks, Bricks, Glowstone, Moss Block, Mossy Cobblestone, Torch | Pleasant |
| Planks, Leaves, Thatch, Dirt Path, Smooth Stone | Slightly pleasant |
| Stone, Sand, Furnace | Neutral |
| Dirt, Coarse Dirt, Gravel | Slightly ugly |
| Mud, Cobweb, Netherrack | Strongly ugly |

The lesson is simple: **windows, lanterns, flowers, a bell, worked stone, and a swept path** make a place people love. Bare dirt, gravel, mud, and cobwebs make a place they'd rather leave. Even swapping a room's floor from dirt to planks or dirt paths nudges the whole home upward.

!!! tip "Beauty is cultural"
    Which blocks count as beautiful isn't fixed — your [culture](culture-and-heraldry.md) shapes it. A culture style can raise or lower the appeal of the blocks it favors, so the same courtyard may read differently for two peoples. Lean into your own culture's signature materials and your settlement grows lovelier *and* more distinct.

### Seeing appeal in-game

You don't have to guess. Hover any block and its tooltip shows its **Appeal** contribution, and the House Block screen shows the home's overall Appeal.

For a map-wide picture, bind and press the **Toggle Beauty Debug** keybind (see [Keybinds & Commands](../reference/keybinds-and-commands.md)). It overlays appeal values across the world so you can spot the ugly patches dragging a neighborhood down — the mud pit behind the smithy, the gravel yard by the well — and fix them where they'll do the most good.

!!! example "Turning an Unappealing hut into a Pleasant home"
    1. Right-click the House Block — Appeal reads **Unappealing**.
    2. Flip on **Beauty Debug** and see a ring of dirt and gravel around the walls.
    3. Replace the dirt floor and yard with **planks and dirt paths**, hang a couple of **lanterns**, and set a **flower pot** by the door.
    4. Right-click again — Appeal now reads **Pleasant**, and the resident's happiness ticks up with it.

## Fine-tuning with the Home Marker Rod

Most homes never need more than Housing Orders and **Detect**. When you *do* want surgical control — to pull a decorated porch into a home's region, or trim a box Detect drew too wide — reach for the **Home Marker Rod** (it appears in-game as **Selection Orders**).

- **Shift**-right-click a House Block to **bind** the rod to that home.
- Right-click two corners to add a box; the marking must always include the House Block, stay connected to the rest of the house, and not stray too far from the House Block.
- Right-click a marked box again to remove it.
- **Shift**-right-click in the air to unbind and free the rod for another home.

It's the precision tool on top of the broad strokes — use it after Detect to perfect a home's shape and reach.

## Common mistakes

!!! failure "Homes that won't validate"
    - **Food or charcoal in the stockpile.** Both needs read only the home's *own* chest — stock each dwelling individually.
    - **An unlit campfire.** The fire must be lit and inside the walls, not just placed.
    - **A doorway with no door,** or any wall gap wider than a window — the room reads as not enclosed.
    - **A house too big for your era.** Build smaller or [research](research-and-eras.md) more room.
    - **No claimed ground.** The room must sit inside your settlement's territory before a House Block will take.

## Where to next

- [Citizens](citizens.md) — the people who live in your homes, and what makes them happy.
- [Workshops](workshops.md) — appeal boosts worker output here too.
- [Culture & Heraldry](culture-and-heraldry.md) — how your people decide what's beautiful.
- [Building](../antiquity/building.md) & [Masonry](../antiquity/masonry.md) — the materials that raise a home's appeal.
