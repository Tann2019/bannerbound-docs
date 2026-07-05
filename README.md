# Bannerbound Wiki

The community field guide for **[Bannerbound](https://github.com/Nitsu430/Bannerbound)** — the
civilization-building Minecraft modpack by Nitsu (Nitsu430). Built with
[MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

**Live site:** https://tann2019.github.io/bannerbound-docs/

## What's here

| Section | Covers |
| --- | --- |
| **Getting Started** | Install, your first hour, founding a settlement, the core gameplay loop |
| **The Civilization** | Settlements, citizens, jobs, housing, workshops, food, territory, government, research, faith, culture, walls, diplomacy, barbarians, crises |
| **The Antiquity Age** | Knapping, tool tiers, woodworking, masonry, metalworking, pottery, tannery, cooking, brewing, herbalism, fletching, building materials |
| **Reference** | Keybinds & commands, the Chronicle & Ponder, optional mods, glossary, FAQ |

## Run it locally

You need Python 3.10+.

```bash
# 1. Install the tooling
pip install -r requirements.txt

# 2. Serve with live reload (edit a page, the browser refreshes)
mkdocs serve
#   → http://127.0.0.1:8000/bannerbound-docs/

# 3. Build the static site into ./site (what gets deployed)
mkdocs build --strict
```

> On Windows, if the `mkdocs` command isn't on your PATH, use `python -m mkdocs serve` instead.

## Project layout

```
docs/
  index.md                 # home page
  getting-started/         # onboarding
  civilization/            # the Core mod's systems
  antiquity/               # the Antiquity mod's crafts
  reference/               # quick reference
  assets/                  # logo, favicon, images
  stylesheets/extra.css    # the heraldic theme
overrides/                 # theme overrides (custom_dir)
mkdocs.yml                 # site config, nav, theme, extensions
.github/workflows/deploy.yml   # builds + publishes to GitHub Pages on push to main
```

## Deploying

Every push to `main` triggers the **Deploy wiki to GitHub Pages** GitHub Action, which builds the
site with `mkdocs build --strict` and publishes it. In the repo's **Settings → Pages**, set the
source to **GitHub Actions**.

## Contributing

This wiki is reverse-engineered from the mod and its in-game **Chronicle**. Bannerbound is in active
development, so mechanics and numbers can change — **when the game and a page disagree, trust the game**
and please open a PR to fix the page. Prose is second person, practical, and player-facing (no code
internals). See any existing page for the house style, and reuse the Material admonitions, tables, and
cross-links already in use.

## Credits & license

- **Bannerbound** modpack © Nitsu (Nitsu430), MIT License.
- This wiki is a community project and is not officially affiliated with the mod.
- Minecraft is a trademark of Mojang Studios; this project is not affiliated with Mojang or Microsoft.
