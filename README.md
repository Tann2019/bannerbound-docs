# Bannerbound Wiki

The community field guide for **[Bannerbound](https://github.com/Nitsu430/Bannerbound)** — the
civilization-building Minecraft modpack by Nitsu (Nitsu430). Built with
[MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

**Live site:** https://tannersteorts.com/bannerbound-docs/

## What's here

| Section | Covers |
| --- | --- |
| **Getting Started** | Install, your first hour, founding a settlement, the core gameplay loop |
| **The Civilization** | Settlements, citizens, jobs, housing, workshops, food, territory, government, research, faith, culture, walls, diplomacy, barbarians, crises |
| **The Antiquity Age** | Knapping, tool tiers, woodworking, masonry, metalworking, pottery, tannery, cooking, brewing, herbalism, fletching, hunting, building |
| **Reference** | Recipe Reference, how the world changes, keybinds & commands, multiplayer & game rules, the Chronicle & Ponder, optional mods, glossary, FAQ |

The **Recipe Reference** and every inline recipe grid are **generated from the modpack's own data**, so
they always match the game — see [Updating the recipes](#updating-the-recipes-after-a-mod-change) below.

## Run it locally

You need Python 3.10+.

```bash
pip install -r requirements.txt        # install the tooling (once)
mkdocs serve                           # live-reload preview → http://127.0.0.1:8000/bannerbound-docs/
mkdocs build --strict                  # build the static site into ./site (what gets deployed)
```

> On Windows, if the `mkdocs` command isn't on your PATH, use `python -m mkdocs …` instead.
>
> Always build with `--strict` before pushing — it fails on broken links, missing anchors, or a bad
> recipe include, catching most mistakes before they reach the site.

## Project layout

```
docs/
  index.md                 # home page
  getting-started/         # onboarding
  civilization/            # the Core mod's systems
  antiquity/               # the Antiquity mod's crafts
  reference/               # quick reference (incl. the generated recipes.md)
  assets/                  # logo, favicon, and generated item icons (assets/items/)
  stylesheets/extra.css    # the heraldic theme + recipe-grid styles
includes/recipes/          # generated recipe snippet fragments (embedded into content pages)
tools/
  gen_recipes.py           # generates the Recipe Reference + fragments from the mod data
  iconlib.py               # resolves item ids → icon PNGs (mod textures + vanilla jar)
overrides/                 # theme overrides (custom 404) — custom_dir
mkdocs.yml                 # site config, nav, theme, extensions
.github/workflows/deploy.yml   # builds + publishes to GitHub Pages on push to main
```

---

## Updating the wiki

### Everyday: edit a page

1. Edit the relevant `.md` under `docs/` (find the right page from the **What's here** table above).
2. `mkdocs serve` and check it in the browser.
3. `mkdocs build --strict`, then commit and push to `main`. The site redeploys automatically (see
   [Deploying](#deploying)).

**House style:** second person, practical, player-facing — **no code internals** in the prose. Keep the
YAML front matter and the `<p class="bb-lead">` intro. Reuse the Material admonitions, tables, and
cross-links already in use. When the game and a page disagree, **trust the game** and fix the page; any
specific number should come from the mod source, not memory.

### Reflecting a gameplay / mechanic change

1. Find the page that owns the system.
2. **Verify the new behavior against the mod source** — the sibling checkout at `../Bannerbound`
   (`Core/src/main` and `Antiquity/src/main`). Numbers come from the code constants / `data/*.json`, not
   from memory or stale in-game tooltips (a few of those are known to lag the real values).
3. Make a surgical edit; build `--strict`; push.

### Updating the recipes (after a mod change)

The **Recipe Reference page and every inline "Recipes: …" grid are generated** — do **not** hand-edit
`docs/reference/recipes.md` or anything in `includes/recipes/`; they're overwritten on the next run.

When the mod's recipes, items, or textures change:

1. Make sure the **mod source** is checked out next to this repo as `../Bannerbound`
   (or point at it with `BANNERBOUND_SRC=/path/to/Bannerbound`).
2. For item **icons**, have **Minecraft 1.21.1** installed so its `1.21.1.jar` is found automatically,
   or set `MC_JAR=/path/to/1.21.1.jar`. (Mod textures come from the mod source; vanilla textures from
   the jar.)
3. Regenerate:
   ```bash
   python tools/gen_recipes.py
   ```
   This rewrites `docs/reference/recipes.md`, regenerates every fragment in `includes/recipes/*.md`, and
   copies any new/changed item icons into `docs/assets/items/`. The inline recipe grids on the content
   pages update automatically, because they include the same fragments.
4. Review the diff, `mkdocs build --strict`, commit and push.

To change **how** recipes look (layout, the crafting-grid / knapping-silhouette styling), edit
`tools/gen_recipes.py` + `tools/iconlib.py` and the `.mc-*` rules in `docs/stylesheets/extra.css` — then
regenerate.

### Embedding a recipe grid on a content page

Recipes live in one place and are pulled in with a snippet include, inside a collapsible:

```markdown
??? example "Recipes: <short label>"

    --8<-- "recipes/<slug>.md"

    [Open the full Recipe Reference :octicons-arrow-right-24:](../reference/recipes.md#<slug>)
```

The list of available `<slug>` values (which are also the section anchors on the Recipe Reference page)
is in [`includes/recipes/README.md`](includes/recipes/README.md), regenerated alongside the fragments.
The **4-space indentation** on the include and link lines is required — it places them inside the
admonition.

### Adding a new page

1. Create `docs/<section>/<name>.md` with YAML front matter (`title` + one-sentence `description`), an
   `#` H1, and a `<p class="bb-lead">…</p>` intro.
2. Add it to the `nav:` tree in `mkdocs.yml`.
3. Add a card for it in that section's `index.md` (copy an existing `grid cards` entry).
4. `mkdocs build --strict` — it will flag any broken cross-links or missing nav files.

## Deploying

Every push to `main` triggers the **Deploy wiki to GitHub Pages** Action, which runs
`mkdocs build --strict` and publishes the result (~1–2 minutes). In the repo's **Settings → Pages**, the
source is **GitHub Actions**.

> **If the deploy job goes red** with *"Deployment failed, try again later"*: this is a known
> intermittent GitHub Pages hiccup (more common under a custom domain), **not** a build problem — the
> `build` job stays green and the previous version keeps serving. Open the run and click
> **Re-run failed jobs**; it goes through on the retry.

## Contributing

This wiki is reverse-engineered from the mod and its in-game **Chronicle**. Bannerbound is in active
development, so mechanics and numbers can change — **when the game and a page disagree, trust the game**
and please open a PR (or push) to fix the page. See the [update procedures](#updating-the-wiki) above and
match the house style of the existing pages.

## Credits & license

- **Bannerbound** modpack © Nitsu (Nitsu430), MIT License.
- This wiki is a community project and is not officially affiliated with the mod.
- Minecraft is a trademark of Mojang Studios; this project is not affiliated with Mojang or Microsoft.
- Vanilla item icons under `docs/assets/items/` are extracted from Minecraft assets for identification
  purposes, as is customary for Minecraft wikis.
