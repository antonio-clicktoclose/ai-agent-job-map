---
name: sales-pipeline-review
description: Weekly read of your pipeline and where it is stuck. Binding happens in the prompt; the skill stays generic.
---

# sales / pipeline review

Weekly read of your pipeline and where it is stuck.

## Inputs
- The real data or context for this job, supplied in the prompt
- Any reference to how this department currently runs

## What to do
1. Read the inputs and bind them to this job.
2. Do the work in the department's voice and format.
3. Return the output ready for a human to review, not a wall of text.

## Output contract
- A concrete deliverable with a clear structure
- The assumptions you made, stated openly
- A short next-action a human should take

## Rules
- Work only from the supplied inputs. Never invent facts or records.
- Flag uncertainty instead of guessing.
- Keep it copy-paste ready. This is a draft a human reviews.
