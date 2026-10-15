# ariadne-icm-architect

A focused fork of [RinDig/icm-architect](https://github.com/RinDig/icm-architect). The original MIT license and copyright notice are preserved in [LICENSE](LICENSE).

A Ariadne, Claude or other agents skill that designs any process, idea, or problem into an **ICM workspace** — folder structure as agent architecture — or restructures an existing folder, repo, or vault into one.

ICM (Interpretable Context Methodology) replaces orchestration code with structure: numbered folders carry sequencing, hierarchy carries context scoping, plain markdown files carry state. One agent, reading the right files at the right moment, does the work of a multi-agent framework — and a human can open any folder and see exactly what state the system is in.

The workspace is a library. The routing files are the catalog: small, stable, they point at everything and store almost nothing. One librarian — one model — walks the building, and the question decides which shelf gets walked to.

- Paper: [Interpretable Context Methodology: Folder Structure as Agent Architecture](https://arxiv.org/abs/2603.16021) (Van Clief & McDermott)
- Community: [Clief Notes](https://www.skool.com/cliefnotes)

## What it does

Two modes:

- **Build** — extracts the structure already present in how you describe your work (the stages, the human gates, what's stable vs. per-run), picks one of six proven forms, and scaffolds the smallest workspace that carries it.
- **Restructure** — audits an existing folder, classifies every file (catalog / contract / factory / product / dead), proposes a migration map for approval, then migrates and validates.

Six forms, one skeleton: **Pipeline** (production line), **Umbrella** (portfolio of pipelines), **Record library** (people/clients/sessions), **Knowledge bundle** (a navigable brain), **Context map** (an organization as a graph), **System map** (a folder later agents will edit — nouns, movements, change-impact). They compose and recurse.

Every result is validated with the **walk test**: an agent with no memory must orient, act, and report status from the files alone.

## fork-specific changes

- **Clickable file navigation:** internal file references use relative Markdown links instead of backticked paths.
- **Workspace-wide terms:** shared terms and identifiers use `[[wikilinks]]` across files, including inside tables. They do not require definitions, dedicated pages, or glossaries.
- **Self-contained maintenance:** each generated workspace keeps these rules in its own root `AGENTS.md` or `CLAUDE.md` and receives a small `_system/check_links.py` path checker. A later agent does not need this skill to maintain the convention.

This fork keeps the original six forms, ICM structure, and human review of substantive work. The checker verifies relative links, not the semantic correctness of wikilinks or missing wikilink markup.

## Install

**Claude Code:** copy this folder to `~/.claude/skills/ariadne-icm-architect/` (or `.claude/skills/ariadne-icm-architect/` inside a project). It can coexist with the original skill. Ask Claude to use "ariadne-icm-architect" when creating or restructuring a workspace.

**Claude apps:** package this entire folder as `ariadne-icm-architect.skill` (zip root is `ariadne-icm-architect/`) and upload it via [Customize → Skills](https://claude.ai/customize/skills).

## Layout

```
ariadne-icm-architect/
├─ SKILL.md              the method: invariants, build mode, restructure mode, walk test
├─ references/
│  ├─ core.md                 five principles, five-layer hierarchy, naming, token discipline
│  ├─ forms.md                the six forms in depth: skeletons, moves, failure modes
│  ├─ system-map.md           audit pipeline for the System map form
│  └─ reference-integrity.md  restructure move-safety gate
└─ assets/templates/     original copyable starters with navigable Markdown links,
                         plus check_links.py copied into each workspace
```

MIT licensed, like the protocol it serves.
