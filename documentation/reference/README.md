# Reference — Static Knowledge

_External knowledge the AI needs to read but doesn't write. API specs, design references, third-party docs, anything that's true regardless of this project's choices._

---

## What goes here

Reference docs are **static** — they describe how something external works, not how this project chooses to work.

Examples:

- **API documentation** for a third-party service (Stripe, Google Calendar, etc.)
- **Schemas or data shapes** the project consumes
- **Design system references** if the project uses a specific design language
- **Glossaries** of terms specific to the domain
- **Reference workflows** the project models after
- **PDF specs or external guides** that the AI should be able to consult

## What doesn't go here

- **Decisions** about what this project does → `../decisions/`
- **Rules** about how this project works → `../../rules/`
- **Active plans** → `../plans/`

If a doc describes *"what this project chooses to do,"* it's not reference — it's decision, rule, or plan.

## How the AI uses reference

When the AI is working on something that depends on external knowledge (e.g., calling an API, matching a schema, applying a design system), it should:

1. **Check reference first** to ground its understanding.
2. **Cite the reference** when its work depends on it (e.g., *"per Stripe's `payment_intent.succeeded` event format..."*).
3. **Flag if reference is missing or stale** rather than guessing.

## File naming

Use descriptive names:

- `stripe-api-reference.md`
- `google-calendar-api-reference.md`
- `domain-glossary.md`
- `design-tokens.md`

Avoid `notes.md`, `misc.md`, `stuff.md` — name the actual subject.

## Keeping reference current

External APIs change. Design systems evolve. **Mark stale reference** with a status line at the top:

```markdown
**Status:** Current as of YYYY-MM-DD · **Source:** [URL]
```

If reference is more than 6 months old and the external thing is fast-moving (APIs, AI tools), re-check before relying on it.

## The Premium-tier discipline

The Build Kit's reference folder is for ad-hoc external knowledge. **AI Code that Works Premium** adds:

- **The KNOWLEDGE.md pattern** — structured infrastructure reference with project IDs, environment specs, account references
- **The reference template library** — credentials checklists, provider API quickstarts, environment maps
- **Live reference syncing** — when an external service changes, the reference auto-updates

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Reference — `documentation/reference/`. Part of Phase 3 in the AI Code that Works method.*
