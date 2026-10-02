# Montoya-Castillo Group Website — Handoff

Hugo + HugoBlox Research Group site for Andrés Montoya-Castillo's lab at CU Boulder. Updated October 1, 2026, after a design-direction pivot and a Team-page prototype that Andrés has approved.

---

## Status, in one paragraph

Structural build is complete (content model, nav, author pages, 12 news posts, About, Join Us, Team page with flat grid and three new undergrad stubs). The visual-design direction has been resettled after reviewing reference sites: **drop the teamsu.org emulation; synthesize signature elements from Andrés's current site with signature patterns from the Schlau-Cohen Lab (MIT)**. A self-contained Team-page prototype at `prototypes/team.html` demonstrates the agreed direction and Andrés has signed off on it ("feels right and it looks great"). Next task is either to mock up a second page (homepage or Research) the same way, or port the Team prototype into Hugo.

---

## Hugo port (Oct 1, 2026): Home, Team and Research are live in the build

These three pages now render from custom templates, not HugoBlox blocks:

- `content/_index.md`, `content/people/_index.md`, `content/research/_index.md` set `type: mcg` + `layout: home|team|research`. All their text lives in front matter.
- `layouts/mcg/baseof.html` is a standalone base (does NOT load the theme's CSS/JS). Templates: `layouts/mcg/{home,team,research}.html`; partials in `layouts/partials/mcg/` (nav, hero, footer, person card, glyphs, bg image helper).
- Styles: `assets/css/mcg.css` (plain CSS, minified + fingerprinted). `assets/scss/custom.scss` is untouched and only affects theme pages.
- Research areas are shared by Home and Research in `data/research.yaml`. To swap in a group illustration, add `image: file.png` (in `assets/media/`) to that area.
- Team grid is generated from `content/authors/*/_index.md`: groups in the order listed in the Team front matter, alphabetical by `last_name`; hover shows `role` (", " → " · "), up to two non-"in progress" education lines, email + Google Scholar from `social`.
- Homepage news = latest 5 posts automatically. Homepage "Recent Publications" is hand-curated in `content/_index.md` (`recent_publications`).
- Nav uses `config/_default/menus.yaml`; collapses to a CSS-only menu button under 1100px.
- Publications, About, Join Us, Alumni & Collaborators use `layouts/mcg/text.html` (`layout: text`): hero + optional `intro`/`toc` + the existing `sections:` list (each `content.title`/`content.text` in markdown). Don't name a layout `page`: it collides with the theme's.
- News: `content/post/_index.md` uses `layout: news` and cascades `layout: post` to every post (slim equation-band header). `layouts/404.html` is also custom.
- Publications list was checked against Google Scholar on Oct 1, 2026; group members are underlined. The per-paper folders in `content/publication/<slug>/` are no longer rendered (cascade `build.render: never`); `generate_publications.py` and those folders are now unused.
- About page front matter was broken (it closed early, so Education and Invited Talks never showed). Fixed; an orphaned bio fragment is kept as a YAML comment at the end of the file.
- Still on the HugoBlox theme: author profile pages (`/author/<slug>/`) and tag/category pages. Nothing in the new nav links to them. Outreach & Mentoring is in the menu but the page doesn't exist yet.
- CI Hugo version bumped to 0.157.0 to match Andrés's Mac (Homebrew). Template lookup for `type: mcg` was verified on 0.157 only.
- Preview: `.claude/launch.json` has `hugo` and `prototypes` (localhost:8765). Because `baseURL` is now the GitHub Pages address (`https://amontoya87.github.io/montoya-castillo-group/`), `hugo server` serves at http://localhost:1313/montoya-castillo-group/. Internal links in the mcg templates go through `strings.TrimPrefix "/" | relLangURL` so they keep the subpath; never hard-code a leading `/`.
- Git: work is on branch `redesign`. This Mac has no GitHub credentials for the shell, so pushes need Andrés to authenticate (e.g. `gh auth login`).
- Pre-port versions of the three `_index.md` files (incl. the longer Research prose) are saved in `prototypes/pre-port/`; they were never committed to git.

---

## Where to pick up next

Pick one of these as the immediate next step. **Ask Andrés which he wants first.**

1. **Mock up the next page prototype — homepage or Research.** Same approach as `prototypes/team.html`: self-contained HTML in `prototypes/`, embedded images, no Hugo dependency, so he can see the design before it's wired into the build.
   - Homepage is the bigger visual statement and should include the equation band from his current site as a signature touch.
   - Research is where the "short, impactful text + custom line-art illustrations" pattern would be demonstrated. He is NOT commissioning illustrations — the group will draw them over time — so launch-day Research page uses text + placeholder graphics.

2. **Port the approved Team prototype into Hugo.** Replicate the design from `prototypes/team.html` in the real site. This means custom layout overrides on `content/people/_index.md` or a custom partial for the people block, plus CSS in `assets/scss/custom.scss` (NOT `template.scss` — see Gotchas).

Still pending from before the pivot, in rough priority order: Outreach & Mentoring page not drafted; several news posts have `# TODO` on their `date:` line; the three undergrad profiles still have placeholder photos and TODO details; `.github/workflows/publish.yaml` exists but has not deployed to GitHub Pages.

---

## The design direction

A **flat, confident, Boulder-rooted** site that uses photography and typography (not graphics) to carry identity on most pages, with one page (Research) reserved for custom line-art illustrations the group will draw themselves over time.

### Carry forward from Andrés's current site (`montoyacastillogroup.com`)

- A different Flatirons/Boulder landscape photograph as the hero on every page. The recurring imagery gives the lab a specific place and reads as personal rather than templated.
- Prose density where appropriate (About, intro paragraphs).
- The equation band on the homepage — handwritten-looking density equations and operators. One of his most personal design touches; stays.
- Numbered-list publications format. He had it right already; keep it. Convention at top: `˚ corresponding · * equal · <u>underlined</u> = group member at CU Boulder`.

### Borrow from the Schlau-Cohen Lab (`schlaucohenlab.com`)

- Big bold **uppercase** title overlaid on full-bleed hero image (sans-serif, weight 900, ~11vw). Replaces the thin-keyline-box treatment from Andrés's current site — reads more confident.
- Flat team grid: circles-only + name by default; **hover reveals a mini-card** with role, education, and social icons. No per-group section headings — ordering alone carries hierarchy.
- Short, impactful text on the Research page (one bold thesis sentence at top + per-area "name + one-sentence pitch + custom illustration") rather than prose density.
- Custom monochrome line-art icons for research areas, with the same icons doing double duty as research-interest glyphs on the team hover cards.

### Explicitly dropped

- **teamsu.org as a reference.** Chasing it was pulling the site into a generic modern-academic genre.
- The thin-keyline-box title overlay from Andrés's current site. Replaced with bolder uppercase.
- Prose density on the Research page. Replaced with short statements + illustrations.
- The image-per-paper publications layout. The current numbered-list prose format is more distinctive now.

---

## The Team prototype

**File**: `prototypes/team.html`

Self-contained HTML, ~690 KB with all images embedded as base64. Open in a browser (not just the Hugo preview panel) to interact with the hover states.

What it demonstrates and what to replicate when porting:

- Full-bleed Boulder-sunny hero (`assets/media/boulder-sunny.jpg`) with a subtle top/bottom dark gradient overlay for text contrast.
- "TEAM" overlaid in bold uppercase white, `clamp(4.5rem, 13vw, 11rem)`, letter-spacing 0.06em.
- Small tracked tagline below the title: "MONTOYA-CASTILLO GROUP · UNIVERSITY OF COLORADO BOULDER".
- Two-sentence intro below the hero, approved text (final):
  > We work at the interface of physical chemistry, condensed matter physics, applied mathematics, and quantum information — building theory and computation to understand charge, energy, and information flow in complex systems.
  >
  > We welcome students and postdocs of every background, and are committed to an inclusive, intellectually generous group environment.
- Small gold rule between intro and grid.
- 3-across people grid (2 on tablet ≤820px, 1 on mobile ≤500px) of all 13 members in order PI → postdoc → grads (alpha by last name) → undergrads (alpha).
- Default card = circular photo (170×170) + name below. On hover, the circle and name fade out and an info card fades in: full name, role in small-caps gold, education (when known), round social icons for email + Google Scholar.
- Outlined "See group alumni & collaborators →" CTA at the bottom; narrow all-caps footer.
- Accent color: `#CFB87C` (CU gold). Text: `#1a1a1a`. Background: `#fff`.
- Fonts: system-ui / SF / Helvetica stack — no external fonts loaded. Looks clean; no need to add a web font unless Andrés wants to.

Generator reference: the Python script that built this is in session memory, not committed. The HTML is self-contained, so edits can be made directly if needed.

---

## The Homepage prototype (draft, awaiting Andrés's reaction)

**File**: `prototypes/home.html` (~1.25 MB, self-contained). Built Oct 1, 2026. Preview with the `prototypes` config in `.claude/launch.json` (serves `prototypes/` on localhost:8765), or open the file directly.

Sections in order: full-viewport `boulder-misty.jpg` hero with "MONTOYA-CASTILLO / GROUP" in weight 900 → intro (lead sentence + two CTAs) → **equation band** (`assets/media/equations.jpg`, pulled from the current site, fixed-background parallax, one overlaid line) → 4 research areas with placeholder line-art glyphs in dashed circles → PI block on warm paper background → News (5) and Recent Publications (4, numbered, underline convention) side by side → full-bleed `boulder-winter.jpg` "JOIN US" band → footer. Same tokens, nav and buttons as the Team prototype.

Andrés approved the homepage direction on Oct 1, 2026, and changed the equation-band line to "Predicting the dynamics of many-body systems with controllable accuracy."

## The Research prototype (draft, awaiting Andrés's reaction)

**File**: `prototypes/research.html` (~790 KB, self-contained). Built Oct 1, 2026.

Sections: `colorado-lake.jpg` hero with "RESEARCH" (Andrés found winter too ominous; lake photo he supplied, saved at `assets/media/colorado-lake.jpg`) → one bold thesis sentence (gold highlighter on "physically transparent theories") + one supporting sentence → 4-tab jump index → four alternating art/text rows (number, uppercase title, one-sentence bold pitch, one short detail sentence, key publications from `content/research/_index.md`) → "We build the tools these frontiers demand" band (Andrés rejected "One toolkit, four frontiers" as too glib) over a darkened `equations.jpg` with the five methods as tiles → publications/join CTAs. The art squares are dashed placeholders with the homepage glyphs, labeled "illustration to come".

---

## Boulder photos (committed to the repo)

Three photos Andrés uploaded, now at `assets/media/`:

| File | Content | Suggested use |
|---|---|---|
| `boulder-sunny.jpg` (1502×1001) | Iconic sunny Flatirons with golden grass meadow and blue sky | **Team** (used in prototype) — warm, welcoming, recruiting |
| `boulder-misty.jpg` (1592×803)  | Misty summer Flatirons with green meadow and yellow wildflowers | **About** or **Join Us** — softer, intimate |
| `boulder-winter.jpg` (1500×1001) | Moody snowy Flatirons in heavy fog | **Research** or **Publications** — stark, focused |

Per-page seasonal rotation is a pattern already established on Andrés's current site. Carry it forward and ask him for more Boulder shots when porting Homepage / Publications.

---

## Reference sites

Both are allowlisted for the Browser pane (`mcp__Claude_Browser__*`) on this computer. Still blocked from WebFetch.

- `montoyacastillogroup.com` — Andrés's current site. Signature: per-page Flatirons heroes, thin-font boxed title overlay, prose density, equation band on homepage, numbered publications list, alternating figure/prose columns on Research.
- `schlaucohenlab.com` — Gabriela Schlau-Cohen (MIT). Signature: full-bleed scientific-image heroes, big bold uppercase titles, custom monochrome line-art research icons that double as research-interest glyphs on hover-revealed team cards, short-sentence Research page.

---

## Research-page illustrations plan

Andrés is **not commissioning** a designer. The group will create the custom monochrome line-art icons for each research area over time. The Schlau-Cohen pattern (one icon per research area, doubling as research-interest glyphs on team cards) is the target.

For launch: text-only or placeholder graphics for research areas. Replace with real line-art as the group draws them.

Research areas to illustrate (from the homepage copy):
- Biophysical Transformations — slow conformational changes driving disease
- Out-of-Equilibrium Energy Flow — spectroscopies and microscopies of charge/energy flow
- Quantum Sensing — temperature, magnetic, electric field fluctuations in microscopic environments
- Mori-Zwanzig Theory — bottom-up and data-driven dynamics for many-body systems

---

## Repository map

```
montoya-castillo-group/
├── HANDOFF.md                  # This file.
├── prototypes/
│   └── team.html               # ⬅ Approved Team-page prototype. Reference for the port.
├── config/_default/
│   ├── hugo.yaml               # `markup._merge: deep` → inherits theme's unsafe HTML.
│   ├── menus.yaml              # Top nav (Home, Research, Publications, Team, Join Us, Outreach & Mentoring, About Andrés).
│   └── params.yaml             # color_theme: custom, primary_color: '#CFB87C'.
├── assets/scss/
│   ├── custom.scss             # ⚠ Correct custom-SCSS file (currently a documented placeholder).
│   └── template.scss           # ⚠ DEAD — theme never loads this. Two orphan rules sit here. See Gotchas.
├── assets/media/
│   ├── boulder-sunny.jpg       # Team hero (in prototype).
│   ├── boulder-misty.jpg       # About / Join Us candidate.
│   ├── boulder-winter.jpg      # Research / Publications candidate.
│   ├── welcome.jpg             # Original homepage hero (will likely be replaced).
│   └── {icon.png, contact.jpg, coders.jpg}
├── content/
│   ├── _index.md               # Homepage. Needs port to new design.
│   ├── about/_index.md         # About Andrés (bio + Education & Career + 24 awards + 83 invited talks).
│   ├── alumni/_index.md        # Alumni (linked from Team page CTA; not in top nav).
│   ├── authors/<slug>/_index.md  # One per person. See File-by-file TODOs.
│   ├── join/_index.md          # Join Us (6 markdown blocks, HTML-comment TODOs).
│   ├── people/_index.md        # Team page — currently uses the HugoBlox people block + inline <style> for flat grid.
│   ├── post/<slug>/index.md    # News posts (12 total).
│   ├── publication/_index.md   # Publications landing — single-markdown-file list, 46 papers.
│   └── publication/<slug>/     # 38 individual publication entries → feed homepage Featured Publications.
├── generate_publications.py    # Andrés's local script to regenerate publication/*/index.md.
├── go.mod, go.sum              # Hugo module pins (theme is a Go module).
└── .github/workflows/publish.yaml  # GitHub Pages deploy (not yet run).
```

---

## Design decisions locked in

- **Primary color**: `#CFB87C` (CU Boulder gold). Accent only, not dominant.
- **Nav**: Home, Research, Publications, Team, Join Us, Outreach & Mentoring, About Andrés. Alumni is NOT in top nav — linked from Team page CTA to `/alumni`.
- **Hero typography**: Large bold uppercase (~11vw, letter-spacing 0.06em) with small tracked tagline below. No thin-keyline box.
- **Hero imagery**: One Boulder/Flatirons landscape photo per page, seasonal rotation.
- **Team page**: Flat continuous grid, no per-group section headings. Default card = circle + name; hover reveals role/edu/socials. Ordering: PI → postdocs (alpha) → grad students (alpha) → undergrads (alpha).
- **Publications**: Single-markdown-file list format (keep the current one).
- **Research page**: One bold thesis sentence + per-area "name + one-sentence pitch + custom line-art" structure. Group draws illustrations over time; text-only or placeholders until then.
- **Equation band**: Keep on the homepage.
- **Homepage CTAs**: All leading slashes.
- **News posts**: `authors: ["admin"]`, `featured: false`.
- **Camille Dreyfus Teacher-Scholar Award (2026)** listed first in `content/authors/admin/_index.md` → "Selected Honors & Awards".
- **Font stack**: System-ui / SF / Helvetica — no web fonts loaded. Looks good; keep unless Andrés asks.

---

## Gotchas — read before touching the project

### 1. OneDrive sync, bash deletion blocked
Repo lives in a OneDrive-synced folder. The sandbox bash mount cannot unlink/delete files. Writes and edits work normally. Any `git rm` or deletion must be done by the user in a Mac Terminal. Watch for stale `.git/index.lock` after failed sandbox git operations.

### 2. SCSS pipeline — only `custom.scss` is compiled
HugoBlox compiles `assets/scss/custom.scss`. **`assets/scss/template.scss` is DEAD** — it was misnamed by an early session and the theme never loads it. Two rules in it (`.universal-wrapper h1` center-align, `.cta-group` center) have never taken effect.

Even with `custom.scss`, when `hugo server` is already running and a new file is created in `assets/`, Hugo sometimes doesn't pick it up until a clean restart. For page-specific CSS that MUST apply regardless of the SCSS pipeline, inline it as a `<style>` block inside a markdown section. That's how the current team-grid flattening works (see `content/people/_index.md`).

### 3. Raw HTML in markdown blocks works
`markup._merge: deep` inherits the theme's `unsafe: true` for goldmark. `<style>`, `<br>`, HTML comments all pass through verbatim.

### 4. CTA shortcode is relative by default
`{{< cta cta_link="path" ... >}}` resolves relative to the current page. **Always use leading slash**: `cta_link="/path"`.

### 5. Author avatar lookup
Default lookup is `avatar.jpg`. Set `avatar_filename:` in front matter if the file is `.jpeg` or `.png`. Current mix:
- `.jpg`: admin, bert-cham, anthony-dominic, ethan-fink, tianchu-li, zach-wiethorn, pranay-venkatesh, min-wang, ella-todd, sophie-collister
- `.jpeg`: srijan-bhattacharyya, matthew-laskowski, nanako-shitara, zhen-cai

### 6. People block sorting
Iterates `content.user_groups` in list order. Within each group sorts by `.Params.last_name`. There is no built-in weight-sort for members.

### 7. Browser pane & WebFetch
`montoyacastillogroup.com` and `schlaucohenlab.com` are allowlisted in the Browser pane (`mcp__Claude_Browser__*`) on this computer, persistent. WebFetch still can't reach them — use the Browser pane instead. If a fresh session gets an "access not allowed" response, call `mcp__Claude_Browser__request_access` and retry.

### 8. Hugo not in sandbox
A plain `hugo` build can't run in the sandbox (no Hugo binary, modules not cached). Verification options: YAML parse via Python; live preview on user's own `hugo server`; view-source the live page to confirm specific HTML/CSS.

---

## File-by-file TODOs

### Highest priority
- **Research page port** (`content/research/_index.md`) — redesign to the new direction once Andrés has reacted to a Research prototype. `boulder-winter.jpg` is the candidate hero.
- **Homepage port** (`content/_index.md`) — new hero image + equation band from his current site + updated typography.
- **Team page port** — replicate `prototypes/team.html` using HugoBlox people block + custom layout overrides and CSS.

### Content stubs & placeholders
- `content/authors/min-wang/_index.md`, `ella-todd/_index.md`, `sophie-collister/_index.md` — three undergrad stubs. Placeholder gray-silhouette `avatar.jpg`; TODO email, interests, bio.
- News posts with placeholder dates — grep `# TODO` in every `content/post/*/index.md` and set real dates.
- `content/outreach/_index.md` not drafted. Low priority.

### Housekeeping
- `assets/scss/template.scss` — dead file. Delete via Mac Terminal (`git rm`) or migrate its two orphan rules into `custom.scss` (and confirm `hugo server` restart picks them up).
- `content/people/index.md` — if still present alongside `_index.md`, delete (causes "ambiguous content" build error). `git rm` from Mac Terminal.
- `.gitignore` — add `.DS_Store`. Consider adding `prototypes/` if Andrés doesn't want prototype files tracked (they can be large).

---

## Verification checklist

Before shipping any change:

- [ ] YAML front matter parses: `python3 -c "import yaml; yaml.safe_load(open('path').read().split('---',2)[1])"`
- [ ] Live preview on `hugo server` (localhost:1313) shows the change without a console error
- [ ] For CSS changes: view-source the live page and confirm the rule is present (or that the inline `<style>` is on page)
- [ ] For new author / people-block changes: person appears in the correct group on `/people` and the sort order within group is alpha-by-last-name
- [ ] Every `cta_link` has a leading slash
- [ ] For prototype preview: open the HTML directly in a browser to interact with hover states

---

## Key debug table

| Symptom | Where to look |
|---|---|
| Styling not applying | View-source live page; is the rule in `custom.scss` compiled into `public/css/wowchemy.css`? Or is it inline on page? |
| Team page members wrong order | `content/people/_index.md` `user_groups` list order; author `last_name` field |
| 404 on a CTA | Missing leading slash in `cta_link` |
| Build error "ambiguous content" | Both `index.md` and `_index.md` in the same folder |
| Avatar not showing | `avatar_filename` mismatch with actual file extension |
| New SCSS file not applied | Restart `hugo server` cleanly; verify file is `custom.scss` not `template.scss` |
| Hero image doesn't load | HugoBlox hero block expects `filename:` relative to `assets/media/` |

---

*Last updated: October 1, 2026 — after the design-direction pivot and Team-page prototype approval.*
