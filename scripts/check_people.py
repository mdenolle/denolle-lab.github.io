import os, sys, re, yaml, glob, html
DATA = "_data/team_members.yml"
SITE = "_site"
PEOPLE_INDEX = os.path.join(SITE, "people", "index.html")
MEMBER_DIR = "_pages/people"

def read_front_matter(path):
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    if not txt.startswith("---"):
        return {}
    fm = txt.split("---", 2)[1]
    return yaml.safe_load(fm) or {}

def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.strip().lower()).strip('-')
    return s

# 1) canonical member schema from marine-denolle.md
template_path = os.path.join(MEMBER_DIR, "marine-denolle.md")
tmpl = read_front_matter(template_path)
if not tmpl:
    print("ERROR: cannot read template front-matter:", template_path)
    sys.exit(1)
required = {"layout", "title", "permalink"}  # minimal required
tmpl_keys = set(tmpl.keys())

# 2) load team data
with open(DATA, "r", encoding="utf-8") as f:
    team = yaml.safe_load(f) or []
if not isinstance(team, list):
    print("ERROR: _data/team_members.yml must be a list of entries")
    sys.exit(1)

errors = []

# 3) Ensure only one People page exists (_site/people/index.html)
if not os.path.exists(PEOPLE_INDEX):
    errors.append("Missing built People index: _site/people/index.html")
if os.path.exists(os.path.join(SITE, "people.html")):
    errors.append("Found _site/people.html (duplicate People page); ensure a single /people/ route.")

# 4) Validate member pages & slugs
# Map permalinks in source files
permalink_to_src = {}
for path in glob.glob("_pages/**/*.md", recursive=True) + glob.glob("_pages/**/*.html", recursive=True):
    with open(path, "r", encoding="utf-8") as fh:
        head = fh.read(4000)
    if head.startswith("---"):
        fm = head.split("---", 2)[1]
        m = re.search(r'^\s*permalink:\s*(.+)\s*$', fm, re.M)
        if m:
            pl = m.group(1).strip()
            permalink_to_src[pl] = path

# From team YAML, check built pages exist and index links present
if os.path.exists(PEOPLE_INDEX):
    with open(PEOPLE_INDEX, "r", encoding="utf-8") as f:
        people_html = f.read()
else:
    people_html = ""

for p in team:
    name = p.get("name", "").strip()
    slug = p.get("slug") or p.get("id") or slugify(name)
    if not name or not slug:
        errors.append(f"Team entry missing name/slug: {p}")
        continue
    permalink = p.get("url") or f"/people/{slug}/"

    # source exists?
    src_exists = permalink in permalink_to_src
    if not src_exists:
        candidate = os.path.join(MEMBER_DIR, f"{slug}.md")
        if os.path.exists(candidate):
            src_exists = True
    if not src_exists:
        errors.append(f"Missing SOURCE page for {name} -> expected {permalink}")

    # built exists?
    built1 = os.path.join(SITE, permalink.strip("/"), "index.html")
    built2 = os.path.join(SITE, permalink.strip("/"))
    if not (os.path.exists(built1) or os.path.exists(built2)):
        errors.append(f"Missing BUILT page for {name} at {permalink}")

    # index includes link?
    if people_html and (f'href="{html.escape(permalink)}"' not in people_html):
        errors.append(f"People index missing link for {name} ({permalink})")

# 5) Member front-matter validation
for path in glob.glob(os.path.join(MEMBER_DIR, "*.md")):
    fm = read_front_matter(path)
    missing = required - set(fm.keys())
    if missing:
        errors.append(f"{path} missing required front-matter keys: {sorted(missing)}")
    # permalink must be /people/<slug>/
    pl = fm.get("permalink", "")
    m = re.match(r"^/people/([a-z0-9-]+)/?$", pl)
    if not m:
        errors.append(f"{path} has invalid permalink (expected /people/<slug>/): {pl}")

if errors:
    print("\nFAILED People checks:")
    for e in errors:
        print(" -", e)
    sys.exit(2)

print("People checks passed.")
