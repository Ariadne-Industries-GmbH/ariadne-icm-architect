# {Workspace name} — the pipeline

The flow in one line: {plan it, make it, check it, ship it — in your workspace's words}.

| Stage | Job | Input | Output | Human check |
|---|---|---|---|---|
| [01_{name}](stages/01_{name}/CONTEXT.md) | {five words} | {what it reads} | `stages/01_{name}/output/{file}` (planned) | {what a person verifies} |
| [02_{name}](stages/02_{name}/CONTEXT.md) | {five words} | `stages/01_{name}/output/{file}` (planned input) | `stages/02_{name}/output/{file}` (planned) | {what a person verifies} |
| [03_{name}](stages/03_{name}/CONTEXT.md) | {five words} | `stages/02_{name}/output/{file}` (planned input) | `stages/03_{name}/output/{file}` (planned) | {what a person verifies} |

Factory (stable, every run): `_shared/{voice.md, rules.md, …}`
Product (new each run): each stage's `output/`

Status is whatever exists: a stage is COMPLETE when its `output/` holds an artifact — a placeholder that only keeps the empty folder in git does not count.
