---
title: Walls & Defenses
description: Research Wall Building, design your culture's wall in a 3D editor, preview it on your border, place gates, and set builders to raising it from your stockpiles.
---

# Walls & Defenses

<p class="bb-lead">A border on the map is a claim. A border made of stone is a statement. When you're ready to draw a real line of defense around everything your citizens have built, you design the wall yourself — segment, corner, and gate — and the settlement lays it along your frontier exactly as you drew it.</p>

!!! abstract "The short version"
    - Research **Wall Building** first. It unlocks the wall planner *and* the [**Builder**](jobs-and-labor.md) worker who raises it.
    - Open the **Town Hall → Walls** tab. Two doors: **Open Wall Designer** (author your style) and **Wall Preview & Construct** (lay it on your border).
    - In the **Wall Designer** you build three small designs — a **Segment**, a **Corner**, and a **Gate** — in a 3D editor, then **Save & Set Active**.
    - The layout engine wraps those designs around your [territory](territory.md) border automatically, following every turn and slope.
    - **Preview** the plan as ghost blocks, mark at least one **gate**, optionally **Refine (3D)** the piece heights, then **Construct**. Builders fetch materials from your stockpiles and raise it — or you build it by hand along the ghosts.

---

## First, unlock the trade

Walls don't come for free with your first settlement. You earn them by completing the **Wall Building** research — an Ancient-age project that follows on from **Extensive Quarries**, because a wall is a great deal of cut stone. Open the [research tree](research-and-eras.md) from the Town Hall to run it.

Wall Building unlocks two things at once:

- **The wall planner** — the Walls tab tools that lay a fortification along your borders.
- **The [Builder](jobs-and-labor.md)** — the worker whose whole trade is turning your blueprint into standing stone, block by block.

!!! info "Walls are a physical barrier, not scenery"
    A raised wall is a real obstacle, not a hidden stat. It doesn't change your population or how often raiders come — what it does is stand in the way. A closed line of stone with a defended gate turns a wide-open settlement into a chokepoint: raiders can't pour in from every direction, so they're funnelled toward the [gates your **Guards** hold](jobs-and-labor.md). Because a demolished section refunds its material, a wall can also *grow with you* as your border changes, so it's worth planning even if you build it in stages.

---

## The Walls tab

Everything starts at the **Town Hall**. Open the **Walls** tab and you'll find two menus:

| Menu | What it's for |
| --- | --- |
| **Open Wall Designer** | Author your culture's wall, corner, and gate designs in a 3D editor. Your work autosaves as a draft. |
| **Wall Preview & Construct** | Wrap your active designs around your border, mark gates, refine, and order construction. |

The natural order is left to right: **design once**, then **preview and construct** whenever your border changes. You *can* skip straight to Preview & Construct — a plain starter style (a cobblestone wall, a taller corner post, and a fence-gate opening) is active by default so you have something to build with on day one. But the walls of a proud civilization should look like *your* civilization, so most players open the Designer first.

---

## The Wall Designer

The Designer is a focused little 3D editor with three tabs across the top — **Segment**, **Corner**, and **Gate**. You author each one, and the layout engine handles stitching them into a full wall around any shape of territory. A menu bar runs across the top — **File · Edit · View · Go** — with everything below covered in its menus, and your work autosaves as a draft every time you leave.

=== "Segment"

    The **straight-run** piece. This is the stretch of wall that gets tiled end to end along every flat edge of your border. Give it a silhouette worth repeating — courses of brick, a crenellated top, a walkway.

=== "Corner"

    The **turn** piece — a square tower or post that stamps into every vertex of your border, inside and outside corners alike. A corner one course taller than the segment reads beautifully from a distance. Corner designs are always square.

=== "Gate"

    A segment-sized piece with a **pathable opening** your citizens can walk through. A wall must have at least one gate, or your own people are sealed in. Design it as grand or as humble as you like — an arch, a gatehouse, a simple fence gate.

### Sizing a piece

Each tab has three steppers — **Length**, **Depth**, and **Height**. Left-click a stepper to step it **up**, right-click to step it **down**.

| Design | Length (along the wall) | Depth (thickness) | Height |
| --- | --- | --- | --- |
| **Segment** | 2, 4, 8, or 16 | up to 4 | up to 16 |
| **Gate** | 2, 4, 8, or 16 | up to 4 | up to 16 |
| **Corner** | square, 1–16 | equals length | up to 16 |

Segments and gates snap to **powers of two** in length so they tile cleanly; corners can be any square footprint from a single post up to a broad tower.

### Building the block-work

Two modes drive the editor. Toggle between them, and pick your material from the block list on the side:

| Control | What it does |
| --- | --- |
| **Build** (++b++) | Places the currently picked block wherever you click in the 3D grid. |
| **Select** (++v++) | Click or drag to select blocks you've already placed (to erase or restyle them). |
| Hold ++k++ | **Eyedrop** — sample a block already placed in the design so it becomes your picked block. |
| **Owned only** | Filter the block list down to just the materials your settlement has actually unlocked, so you only design with what you can build. |
| **Search** | Find a block by name in the list. |
| **Wall context** | Show faint ghost copies of the neighboring wall pieces around the one you're editing, so you can see how the tiling reads. |
| **Outside label** | Marks which face points *outward* — the side that faces the wilderness — so you orient decoration correctly. |

A right-side **Required / piece** panel keeps a running tally of the blocks the current tab's design uses — "5× cut limestone, 2× oak fence," and so on — so you can see the material bill for one piece before you ever commit a wall.

### Editing and camera shortcuts

The **Edit** menu carries the usual editor moves, all with keyboard shortcuts:

| Action | Shortcut |
| --- | --- |
| **Undo** | ++ctrl+z++ |
| **Redo** | ++ctrl+shift+z++ |
| **Select All** (in Select mode) | ++ctrl+a++ |
| **Delete Selection** | ++delete++ |
| **Deselect** | *Edit menu* |

To move the camera around your work:

| Camera | How |
| --- | --- |
| **Orbit** | Drag with the **middle mouse button**, or nudge with ++a++ / ++d++ (turn) and ++w++ / ++s++ (tilt). |
| **Pan** | Hold ++shift++ and drag with the **middle mouse button**. |
| **Zoom** | Scroll the mouse wheel. |
| **Reset Camera** | **View → Reset Camera** snaps the view back to its starting angle and distance. |

!!! tip "Design outward-facing"
    The editor treats one side as the **outside** of your wall. Put your strongest, most imposing face there — the layout engine rotates every placed piece to point that face at the wilderness, no matter which compass direction a given stretch of border runs.

### Saving your style

Name your work in the **Design name** field, then hit **Save & Set Active**. A few things worth knowing:

- **Save & Set Active** saves the designs on **all three tabs** together and makes them your settlement's active wall style in one click.
- Typing a **new** name saves a **new** design into your library; keeping the existing name **overwrites** it. That lets you keep several styles on the shelf — a humble palisade for a young border, a grand rampart for your capital.
- To take a design back *off* the shelf, click its row in the **Library — click to load** list beneath the name field. It drops that saved design straight into the current tab, ready to tweak or re-save. (Save & Set Active to actually make an edited design active again.)
- Your active style is the face of your civilization as surely as your [heraldry](culture-and-heraldry.md) is. Choosing materials and a silhouette that match your culture ties the whole settlement together.

!!! example "Authoring a simple rampart"
    1. Open **Segment**. Set Length **8**, Depth **2**, Height **5**.
    2. In **Build** mode, pick cut limestone bricks and lay two solid courses, then a crenellated top row with gaps for battlements.
    3. Switch to **Corner**. Make it a **4×4** post one course taller than the segment.
    4. Switch to **Gate**. Carve a 2-wide, 3-tall opening through the middle and top it with an arch.
    5. Name it "Limestone Rampart" and hit **Save & Set Active**.

### Sharing designs between worlds

Your library lives inside a single world's save. To carry a design to another world — or hand one to a friend — use the **File** menu:

- **File → Export Tab to File** writes the current tab's design out as an `.nbt` file into your game folder's `bannerbound/wall_designs` directory, named for the design and its kind.
- **File → Reload Design Files** re-reads that folder, so any `.nbt` designs you (or someone else) dropped in appear alongside your saved library in the **click to load** list, ready to load into a tab.
- **File → Open Designs Folder** opens `bannerbound/wall_designs` in your system file browser, so you can copy designs in and out. Drop a friend's exported piece in there, Reload, and it's yours to build.

---

## How the layout adapts to your border

You never place a wall chunk by chunk. Once a style is active, the planner **traces the outline of your claimed [territory](territory.md)** and fits your three designs to it:

- **Corners** stamp into every vertex your border makes — the sharp outside corners *and* the concave notches where your claim tucks back in.
- **Straight runs** between corners are tiled with your Segment design. Where a run doesn't divide evenly, the last piece is quietly **truncated to fit** rather than leaving a hole — the line is always closed.
- **Slopes** are handled for you. On gentle ground the wall **drapes** to follow the terrain; on steeper ground it **steps up**, filling foundation underneath so the wall-top walkway stays level for as far as the terrain allows.
- **Deep water** is left as a **gap** — where the border crosses a lake or river too deep to wall cheaply, the water itself is the barrier, and the wall picks up again on the far bank.
- **Vegetation** standing in the wall's footprint (trees, brush, tall grass) is cleared as the wall goes up, so you don't have to hand-clear the line first.

The upshot: you design three small pieces, and get a coherent fortification that hugs whatever shape your civilization has grown into — a shape you can keep reshaping as you claim more land.

---

## Previewing the plan

Open **Wall Preview & Construct**. Nothing is built and nothing is spent yet — this is where you look before you leap.

Click **Preview Ghosts** to project the entire planned wall into the world as translucent **ghost blocks**. Now go for a walk. Follow the line around your border, stand under where the gates will be, look up at the corner towers, and make sure the wall sits where you want it. Hit **Hide Preview** when you're done inspecting.

!!! info "How much is already built"
    Once you've committed a plan, the top of the Preview and Refine screens shows a completeness readout — **"plan committed, X% built"** — so you can see how far your builders have gotten. Change your design, move a gate, or reshape your [territory](territory.md) and it flips to **"an OLDER design is built (X%) — Construct applies this layout,"** a reminder that the wall standing in the world no longer matches the plan you're looking at until you **Construct** again.

### Placing gates

A wall with no way through is a trap, so the planner requires **at least one gate** before it will let you build. To place one, **click the line where you want a gate** — the planner drops a Gate piece there. A few rules keep gates sensible:

- Gates can only sit on a **straight run**, not on a corner.
- A gate needs room to fit **whole**, so you can't cram one right up against a corner where it would be cut off.
- Click a gate again to **toggle it off** if you change your mind.

!!! warning "No gate, no wall"
    Construct **needs at least one gate**. Try to commit a sealed wall and the planner simply refuses — it won't wall your own citizens in. Place at least one before committing, and think about traffic while you're at it. A gate on the road to your fields, another toward your [outposts](territory.md), and you'll save your citizens a long detour every day.

---

## Refine (3D): the final draft

The automatic layout is a strong first draft, but you get the last word. Click **Refine (3D)** to open a rotating, god's-eye view of the whole planned wall where you can adjust it piece by piece.

Select a wall piece, then use:

| Control | What it does |
| --- | --- |
| **Raise +1** / **Lower -1** | Raise or lower the top of the selected piece, course by course — build a taller gatehouse, drop a wall to a low parapet where it overlooks a cliff. |
| **Reset height** | Snap the selected piece back to its design height. |
| **Variant: cycle** | Cycle the selected piece through *your own saved library designs of the same kind and footprint* — the active design shows as **Default** — for a less uniform look. This only does something once you've saved **extra same-size (Length × Depth)** segment or corner designs in the Designer; with none saved, the button just tells you so. (The stepped-slope versions the layout auto-derives on hills are applied for you automatically — they aren't what this button cycles.) |
| **Foundation: on/off** | Toggle the foundation fill under the selected piece. |
| **Toggle gate** | Turn the selected straight-run segment into a gate, or a gate back into wall. |
| **Flat preview** | Swap between the 3D view and a flat, top-down look at the whole line. |

Refine is optional — plenty of players build the auto-layout as-is — but it's where a *good* wall becomes a *great* one. Raise your gatehouses, crown your corners, and drop the wall low where the land already defends you.

---

## Construct: raising the wall

When the plan looks right, hit **Construct**. This **commits** the plan: the ghost blocks lock in as the line the settlement will build, and your workers get to work. (Remember, it needs that gate first.)

Two hands can raise a committed wall:

1. **Your builders.** [Builders](jobs-and-labor.md) fetch the materials your design calls for and place every block for you, baking the connections so stairs, walls, and gates all join up correctly without you fixing block shapes by hand. This is the hands-off way to fortify.
2. **Your own hands.** The committed ghosts stay visible in the world, so you can simply follow the blueprint and place the blocks yourself — useful for a small stretch or when you want it up *now*.

!!! warning "Builders need supplies and somewhere to work"
    A builder can only build if they can reach the materials. Two things are easy to forget:

    - **A marked drop-off.** Builders need a designated drop-off point to work from. Without one, they've nowhere to stage the wall and construction never starts.
    - **Stocked stockpiles.** Keep the bricks and blocks your design calls for in your storage. If the shelves run empty, construction **stalls** mid-wall until you restock.

!!! tip "Build in reachable stages"
    A long border is a lot of stone. If your quarries can't keep up, construct a well-supplied stretch at a time — the plan is happy to be raised piecemeal, and a half-finished wall still funnels raiders toward the parts you *have* built.

---

## Changing or tearing down a wall

Your border will change — you'll claim new land, square off a ragged edge, or decide a whole flank should look grander. Walls are built to move with you.

- **Re-run the plan.** Change your active style or expand your [territory](territory.md), reopen Preview & Construct, and the layout redraws itself around the new shape. Construct again and builders adapt the existing wall to match.
- **Cancel Plan.** Click **Cancel Plan** to drop a committed plan entirely. The standing wall blocks aren't forgotten — they're **queued for demolition**, and the material is **refunded** back to your settlement as it comes down. Nothing is wasted; a layout that no longer fits simply returns its stone to your stores for the next design.

!!! note "Nothing is thrown away"
    Because demolition refunds material, you can experiment freely. Raise a wall, live with it a while, then cancel and redesign — the stone comes home either way.

---

## The living defense behind the stone

Walls are the bones of your defense, but they don't stand a watch on their own.

- **[Guards](jobs-and-labor.md)** patrol your borders and man posts along the wall. They're far steadier in a brawl than an ordinary citizen and won't be lured off into the wild — the difference between a wall that merely *looks* defended and one that is. Mark guard posts on your walls and gates where you most expect trouble.
- **[Barbarians and raids](barbarians.md)** are exactly what a wall is for. A closed border with a defended gate turns a chaotic night attack into a chokepoint you control.
- **[Diplomacy](diplomacy.md)** decides whether a neighbor's citizens are welcome guests or besiegers at your gate. In peacetime your border keeps outsiders from meddling; in war, your walls are what stand between them and everything inside.

!!! quote "A border you can defend"
    A tight, deliberate territory is cheaper to wall than a ragged sprawl. When you claim land, claim toward what you can hold — then draw the line in stone.

---

## Where to next

- [Territory & Outposts](territory.md) — the border your wall follows, and how to shape it.
- [Jobs & Labor](jobs-and-labor.md) — assigning the **Builders** who raise the wall and the **Guards** who hold it.
- [Culture & Heraldry](culture-and-heraldry.md) — making your wall's materials and silhouette speak for your civilization.
- [Barbarians & Raids](barbarians.md) — the threats your gates and battlements are built to stop.
