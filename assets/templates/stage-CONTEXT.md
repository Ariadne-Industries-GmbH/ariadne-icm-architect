# {NN}_{stage-name} — {the job in five words}

One job: {the single thing this stage does}.

## Inputs
- Working (this run): [Previous stage output](../{prev-stage-folder}/output/{file}) — link once it exists; until then, show its planned path as literal code. Renumbering the pipeline means updating the reference.
- Reference (every run): [Shared rules](../../_shared/{rules-file}.md)
- Reference (every run): [Stage guide](references/{stage-specific-guide}.md)

Do NOT load: {anything an eager agent would wrongly pull in — other stages' references, prior runs, the whole _shared folder}.

## Process
1. {Read the inputs.}
2. {Transform, following the reference constraints.}
3. {Hard limits worth restating: length, count, format.}

## Outputs
- `output/{artifact}.md` (planned output; link only after the file exists)

## Human check
{One concrete act: read it aloud / verify the numbers against X / confirm the order survived. Edit the output in place — the next stage reads whatever is here.}
