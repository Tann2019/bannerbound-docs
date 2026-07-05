---
title: The Food Economy
description: How five food sources feed your settlement, how citizens eat, and how to keep the reserve out of the red.
---

# The Food Economy

<p class="bb-lead"><em>Every tribe eats every day. Food is the quiet governor of everything you build — it decides whether newcomers arrive, whether your people work with a smile, and whether your grand plans survive their first hard winter.</em></p>

!!! abstract "The short version"
    Five sources feed your settlement: **Fields**, **Fishing**, **Herds**, **Foraging**, and **Hunting**. Workers put real catches, crops, and meat into your claimed storage, and that stored food quietly turns into food-per-second on the town hall's **Food** line. Your citizens eat a little every day — the more of them, the faster it drains. When income beats appetite you have a **surplus** and can welcome newcomers; when it falls behind you have a **deficit**, growth stops, and the reserve slides toward **starvation**. Keep the food line green and the days-left counter high.

## Food is a settlement stat, not a lunchbox

Your citizens do not walk to a chest and munch an apple. Instead, all the food your workers produce pools into a single settlement-wide **food reserve** — an abstract bar you manage from the [town hall](settlements.md). Growing food, storing it safely, and keeping the reserve topped up is one of the core rhythms of the whole game.

Open the town hall and find the **Food** line (once your scholars have unlocked it, the **Statistics** tab gives the same figures their own breakdown under *Food economy*). Hover the line and you get the whole story at a glance:

- **Net food: +/- N/s** — the single number that matters. Positive means the reserve is filling; negative means it is draining.
- A live **status word** on the line itself — **Surplus**, **Draining**, or **Starving!** — telling you at a glance which way things are heading.
- **Food bar** and **Stored buffer** — how full your reserve is right now, against its **cap**. That cap tracks the food your *next* citizen will cost, so it climbs as your settlement grows; researching **Food Preservation** adds overflow room on top (see [Cooking & Food](../antiquity/cooking-and-food.md)).
- **Stored food value** — how much edible food is sitting in your claimed storage.
- **~N days left** — how long the reserve lasts at the current drain. While you are comfortably ahead it reads **Self-sufficient** instead of a countdown.

Everything below explains what feeds that line and what empties it.

## The five food sources

Every scrap of settlement food comes from one of five sources, and the Food tooltip breaks your income down by each of them, **per minute**, so you can see at a glance which one is carrying your people:

| Source | Town hall label | Who supplies it | Typical catch |
|--------|-----------------|-----------------|---------------|
| Fields | **Fields** | Farmers working a bound field | Wheat, carrots, potatoes, beetroot |
| Fishing | **Fishing** | Spear fishers on a claimed shore | Cod, salmon, tropical fish |
| Herds | **Herds** | Herders culling a bred flock | Beef, mutton, pork, chicken |
| Foraging | **Foraging** | Foragers gathering the wild | Berries, apples, mushrooms |
| Hunting | **Hunting** | Hunters ranging your territory | Wild game and meat |

Each source is powered by a [job](jobs-and-labor.md), and each job needs the same handful of things to actually produce: a **citizen assigned to it**, a **work area** so the worker knows where to go, and — where the job calls for one — the **right tool** in reach. Get those in place and food starts flowing into storage on its own.

!!! tip "Spread your bets"
    A settlement that leans on a single source is one bad season from a deficit. A couple of fishers *and* a small field *and* an occasional hunt gives you a buffer against any one source drying up — and the Food tooltip's per-source lines make it obvious which one to reinforce.

## How your people eat

The instant your settlement grows up — the moment you enact a [government](government.md) — your citizens begin to eat. Before that, during the founding scramble, nobody drains the reserve at all: a fresh camp gets a grace period to set up food production before hunger ever bites.

Once eating begins, it is a **steady per-second drain that scales with your population**. Every mouth eats the same modest amount each day, so ten citizens burn through food roughly twice as fast as five. This is why growth and food are locked together: every newcomer you welcome is another appetite you have promised to feed, forever.

The Food tooltip never shows all of this at once. It has **two different faces** depending on whether your settlement has enacted a government yet:

=== "Before a government (pioneering)"

    While you're still in the founding scramble, nobody eats, so the tooltip only ever counts *gains*:

    - **Pioneering spirit** — a small founding trickle, *"founding settlers forage to grow the camp."* It helps a young settlement grow before a real food industry exists, and matters most in the earliest hours.
    - **Stored valid food** — the passive income from food sitting in your claimed storage (see below), shown only once you actually have some.

    There is no "eaten by citizens" line here — nothing is draining the reserve yet.

=== "After a government (citizens eating)"

    The moment you enact a government the pioneering trickle disappears and appetite switches on. The tooltip now reads:

    - **Net food/s** — the single number that matters, positive or negative.
    - **Stored valid food** — your passive stored-food income (see below).
    - **Eaten by citizens** — that population-scaled appetite, shown as a negative.

    Below these it shows either a **days-left** runway (while you're in the red) or **Self-sufficient** (when income covers the drain).

Keep the net number at or above zero and you are secure. Let it go red and the days-left counter starts ticking down.

!!! info "Blessings ease the appetite"
    Some [faith](faith.md) blessings and banner effects list a "food/s" bonus. Rather than adding a separate "+food/s" line, these quietly **slow how fast your citizens eat** — they shrink the drain, so your net food number simply improves without you lifting a hoe. (Before you enact a government, when nobody's eating yet, the same bonus rolls into your pioneering trickle instead.)

## Stored food: your living larder

Here is the heart of the system. **Valid, edible food sitting in your claimed storage passively contributes food-per-second to the reserve while it stays good.** You do not micromanage it item by item — a chest of cod simply "counts" until it spoils or gets used, and the more valuable the food, the more it contributes.

Every food item carries a **settlement food value**, and richer food does more work per stack. A few reference points, all straight from the food tables:

| Food | Value | Notes |
|------|:-----:|-------|
| Raw crops, berries, raw meat & fish | **1** | The floor — better than nothing, quick to spoil |
| Apple, baked potato, cooked fish, dried meat | **2** | A step up |
| **Cooked meat**, bread, beetroot soup | **3** | Cooking roughly triples raw meat |
| Golden carrot, pumpkin pie, mushroom stew | **4** | Rich, worthwhile fare |
| **Rabbit stew** | **5** | The strongest single food in the tables |

The lesson is loud and clear: **cook your food.** Raw beef is worth a single point; cooked, it is worth three. And **stew is the crown jewel** — a pot of rabbit stew banks a large stored-food value in one item, making it the single best thing to stockpile when you need to flood the reserve fast.

!!! warning "Storage only counts once you've learned to keep it"
    A brand-new settlement's chests are just ordinary player storage — the food inside contributes **nothing** to the reserve. Your larder only wakes up once you have researched **Storage Logistics** (see [Research & Eras](research-and-eras.md)). After that, food in your [claimed chunks](territory.md) starts counting toward the food line automatically.

### Spoiled and poisoned food is dead weight

Storage is not a freezer. Food carries a **freshness level** as it ages — first **Fresh**, then **Bland** (worth only half its value), and finally **spoiled**. Critically:

- **Spoiled food and poisoned food contribute nothing to your food rate — even sitting in claimed storage.** A chest of rotten meat is not a reserve; it is clutter.
- Cooked food keeps far longer than raw, and **dried meat and fish never spoil at all** — they trade a little peak value for immortality, which makes them superb long-term insurance.

The full mechanics of freshness, salting, and drying live on the [Cooking & Food](../antiquity/cooking-and-food.md) page. For the food economy, the rule of thumb is simple: **cook it, dry it, or eat through it before it turns.**

## Topping up the reserve by hand

Workers fill the larder on their own, but you can also make an emergency deposit yourself. **Sneak (shift) and right-click your town hall with food in hand** to hand it straight to the settlement — you'll see a cheerful *"Deposited +N food"* and the reserve jumps.

A few guardrails to know:

- You can only deposit at **your own** town hall — *"You can only deposit food at your own town hall."*
- Only **safe** food is accepted. Spoiled or otherwise unsafe items are turned away with *"That food is not safe for the settlement."*
- If the reserve is already brimming, you'll get *"Food stockpile is full!"* — no need to keep stuffing it.

This is perfect for dumping a lucky haul of stew or cooked meat during a crunch. For steady day-to-day supply, though, let your workers and the passive larder do the heavy lifting.

## Surplus, deficit, and who gets to grow

The reserve does double duty. It is both your survival buffer *and* the gate on immigration:

=== "Surplus"

    Net food is at or above zero — the bar holds or climbs, and the tooltip reads **Surplus — the settlement can take in newcomers.** A well-fed tribe is an inviting one; only a settlement in surplus can welcome new citizens. Combined with a healthy [culture](culture-and-heraldry.md), this is how your population climbs.

=== "Deficit"

    Net food has gone negative — the tooltip warns **Deficit — growth pauses until food production recovers.** No newcomers arrive, and the days-left counter starts its countdown. Growth resumes the moment you claw back into the black, so a deficit is a stall, not a death sentence — *if* you fix it in time.

!!! note "A die-off won't cheat hunger"
    Losing citizens to starvation doesn't quietly "solve" the shortage. The settlement remembers the largest tribe it has ever sustained and still expects to feed that many, so shrinking your population is never the answer — **producing more food** is.

## When the reserve runs dry: starvation

If the bar drains to empty while citizens are still eating, your people begin to **starve**. You'll see the escalating warnings — *"Food running low"* and then the blunt *"Your settlement is STARVING"* — and the town hall's population readout starts counting the **hungry** and **starving**. Citizens who go to bed hungry carry a sour thought (*"I went to bed hungry"*, *"I'm starving!"*) that drags down their mood and your settlement's [happiness](citizens.md).

Left unchecked, hunger becomes a full-blown **Starvation [crisis](crises.md)** — the first great turning point most settlements face. It demands a real, permanent answer: pick a food path (Fishers, Farmers, or Herders) and build a stable stored-food rate that can feed a *full* tribe.

!!! danger "Maintainer note: ignore the crisis's talk of a 'drop-off chest'"
    The Starvation crisis's on-screen checklist still tells you in a few places to *"mark a drop-off chest"* or *"mark a harvest storage chest."* **That instruction is stale — there is no such chest to mark anymore.** The real recipe for keeping food flowing is:

    - [ ] **Assign the gatherer job** the crisis asks for (e.g. farmers, fishers, or herders) to real citizens.
    - [ ] **Set that job's work area** — bind the field or pen with the Foreman's Rod, or point fishers at a claimed shore.
    - [ ] **Give the worker its tool** — a hoe, a spear, and so on, in the tool slot or tool storage.
    - [ ] **Keep storage inside your claimed chunks** — usually **baskets** early on — so what they gather actually counts toward the reserve.

    Do those four things and the food rate climbs on its own. Watch the Food line's *Stored valid food: +N/s* figure rise as it works.

!!! tip "Stew is your emergency ration"
    When you're staring at a red food line, nothing digs you out faster than **stew**. A single pot banks a large stored-food surplus, so a batch of rabbit stew — cooked and either stored in your claim or deposited by hand at the town hall — can flip a deficit back to surplus almost instantly and buy you the days you need to get real production running.

## Where to next

- [Jobs & Labor](jobs-and-labor.md) — assign farmers, fishers, herders, foragers, and hunters, and set their work areas and tools.
- [Cooking & Food](../antiquity/cooking-and-food.md) — turn raw catches into high-value, long-lasting meals, and master freshness and drying.
- [Crises](crises.md) — how the Starvation crisis and others force the decisions that shape your settlement.
- [Citizens](citizens.md) — how hunger, mood, and thoughts ripple through your people.
