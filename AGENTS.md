# AGENTS.md — Dra. Gabriella González Pane Strategy Repo

**Client:** Dra. Gabriella González Pane (private dental practice, Luque/Asunción, Paraguay)
**Repo type:** Strategy + launch kit (read-heavy, docs + research, minimal code)
**Language:** Spanish (Paraguayan) + English for system terms

## Ground rules
- Every repo change must keep the strategy coherent and pricing-consistent.
- Do not edit client-template files under `09_TEMPLATES/` without flagging it as a content change.
- Keep clinical content accurate; do not invent new procedures or prices outside `canonical-pricing-reference-v2.md`.

## Workflow expectations
- Read more than you produce: this repo is strategy-first. Confirm facts before changing docs.
- Preserve section IDs, anchor headings, and the PRICING CROSS-REFERENCE blocks in every file that has them.
- If a doc conflicts with the canonical pricing or a higher-priority index, update that doc and note where else should change.

## Quality bar
- Single source of truth for pricing: `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
- Single source of truth for research synthesis: `01_RESEARCH/market/master-synthesis-market-analysis.md`
- Entry points expected to stay accurate: `README.md`, `COMPLETE-INDEX.md`, `start-here.md`, and `TODO.md`

## Boundaries
- Do not push to remote without committing staged changes in logical scopes (messages should fit the change set).
- Do not add AI tool configs that require secrets.
- Do not turn this into software. If any automation would help, implement it as a script in a tools/scripts directory.
