"""
Resolve Minecraft/Bannerbound item ids to their icon PNG, from mod resources and the
vanilla 1.21.1 jar. Shared by the recipe-icon extractor and the recipe-page generator.
"""
import os, json, zipfile, functools

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
MOD = os.environ.get("BANNERBOUND_SRC", os.path.join(REPO, "..", "Bannerbound"))

# namespace -> assets root (mod resource dirs)
ASSETS = {
    "bannerboundantiquity": os.path.join(MOD, "Antiquity/src/main/resources/assets/bannerboundantiquity"),
    "bannerbound":          os.path.join(MOD, "Core/src/main/resources/assets/bannerbound"),
}

def _find_jar():
    env = os.environ.get("MC_JAR")
    if env and os.path.isfile(env):
        return env
    candidates = [
        os.path.expandvars(r"%APPDATA%/.minecraft/versions/1.21.1/1.21.1.jar"),
        os.path.expanduser("~/AppData/Roaming/.minecraft/versions/1.21.1/1.21.1.jar"),
        os.path.expanduser("~/.minecraft/versions/1.21.1/1.21.1.jar"),
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    return None

JAR_PATH = _find_jar()
_jar = zipfile.ZipFile(JAR_PATH) if JAR_PATH else None

def split(idstr):
    if ":" not in idstr:
        idstr = "minecraft:" + idstr
    return idstr.split(":", 1)

@functools.lru_cache(maxsize=4096)
def _read_asset(ns, kind, path):
    """Return bytes for assets/<ns>/<kind>/<path> from mod dir or jar, else None."""
    if ns in ASSETS:
        fp = os.path.join(ASSETS[ns], kind, path)
        if os.path.isfile(fp):
            with open(fp, "rb") as f:
                return f.read()
        return None
    if _jar is not None:
        name = f"assets/{ns}/{kind}/{path}"
        try:
            return _jar.read(name)
        except KeyError:
            return None
    return None

def _load_model(ns, path):
    """path like 'item/stick' or 'block/cobblestone' (no .json)."""
    b = _read_asset(ns, "models", path + ".json")
    if b is None:
        return None
    return json.loads(b.decode("utf-8"))

_BLOCK_KEYS = ("all", "texture", "side", "front", "top", "end", "cross", "particle",
               "fire", "layer0", "wall", "bottom", "torch", "log", "0")

def _pick_texture(tex):
    for k in _BLOCK_KEYS:
        v = tex.get(k)
        if v and not v.startswith("#"):
            return v
    for v in tex.values():
        if isinstance(v, str) and not v.startswith("#"):
            return v
    return None

def _texture_ref(model, ns, depth=0):
    """Walk a model (and its parents) to a concrete texture ref 'ns:kind/path'."""
    if model is None or depth > 8:
        return None
    # NeoForge separate_transforms loader: the real model is under perspectives.gui or base.
    if "base" in model or "perspectives" in model:
        persp = model.get("perspectives", {})
        sub = persp.get("gui") if isinstance(persp, dict) else None
        if sub is None:
            sub = model.get("base")
        r = _texture_ref(sub, ns, depth + 1) if sub else None
        if r:
            return r
    tex = dict(model.get("textures", {}))
    ref = _pick_texture(tex) if tex else None
    if ref:
        return ref
    parent = model.get("parent")
    if not parent:
        return None
    pns, ppath = split(parent)
    if ppath in ("item/generated", "item/handheld", "builtin/generated",
                 "builtin/entity", "item/template_spawn_egg"):
        return None
    pmodel = _load_model(pns, ppath)
    if pmodel is None:
        return None
    # child textures override parent's; then re-pick
    merged = dict(pmodel.get("textures", {}))
    merged.update(tex)
    ref = _pick_texture(merged)
    if ref:
        return ref
    return _texture_ref(pmodel, pns, depth + 1)

def resolve_png(idstr):
    """id -> (namespace, texture_relpath, bytes) or None. texture_relpath e.g. 'item/stick'."""
    ns, name = split(idstr)
    model = _load_model(ns, "item/" + name)
    if model is None:
        # some blocks have no item model; try block model directly
        model = _load_model(ns, "block/" + name)
    ref = _texture_ref(model, ns) if model else None
    if ref is None:
        # last resort: guess a flat texture, incl. the common per-block subdir pattern
        for cand in (f"item/{name}", f"block/{name}", f"block/{name}/{name}", f"item/{name}/{name}"):
            b = _read_asset(ns, "textures", cand + ".png")
            if b:
                return ns, cand, b
        return None
    rns, rpath = split(ref)  # ref like 'minecraft:item/stick'
    b = _read_asset(rns, "textures", rpath + ".png")
    if b is None:
        return None
    return rns, rpath, b

def safe_name(idstr):
    ns, name = split(idstr)
    return f"{ns}__{name}".replace("/", "-")
