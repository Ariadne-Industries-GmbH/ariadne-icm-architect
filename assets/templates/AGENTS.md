# {Workspace name}

{One sentence: what this workspace is and what leaves it.}

Built on ICM: folders carry sequencing, hierarchy carries context, files carry state. The structure is the documentation — if something needs explaining, the explanation goes in that folder's CONTEXT.md, not in your head.

## Where things live

| Folder | What it holds |
|---|---|
| [Stages](stages/01_{stage-name}/CONTEXT.md) | the pipeline, in execution order (link to a real first stage) |
| `_shared/` | factory: rules and reference that never change per run |
| `_templates/` | blank starters — new work is a copy, not a blank page |
| [Setup](setup/questionnaire.md) | one-time factory configuration (omit if unused) |

## Route by what just happened

| If | Go to | Then stop at |
|---|---|---|
| starting a new run | [First stage](stages/01_{stage-name}/CONTEXT.md) | human reads the output |
| {previous stage} output approved | [Next stage](stages/02_{stage-name}/CONTEXT.md) | human reads the output |
| asked for status | scan `stages/*/output/` | report what exists |
| setting up for a new user | [Setup questionnaire](setup/questionnaire.md) | answers written to `_shared/` |

## Workspace-wide linking rules

- **File navigation:** Link existing workspace files with relative Markdown links: `[Document](relative/path.md)`. Never replace intended clickable navigation with a path in backticks. Literal paths in commands, code, and planned output paths may remain inline code.
- **Shared terms:** Write any identifier or term with the same meaning across files as `[[term]]` everywhere it is used, including in text and tables. `[[term]]` is a workspace-wide reference to all its occurrences; it requires no target file, glossary, or separate definition.
- **Maintenance:** Keep relative Markdown links working after moves or renames. Run `python3 _system/check_links.py .` after edits, and check for overlooked bare cross-file labels or conflicting meanings of shared wikilinks. The script validates file paths, not meaning.

## The one rule

Nothing moves to the next stage until a person has read the output of the last one.
