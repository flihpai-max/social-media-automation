# Rules — Phase 2

_What this project will and won't do. The fences around how work gets done. Rules turn AI work from a per-prompt negotiation into a governed process._

---

## Why Rules come second

After we know **what** we're building (Context), we have to know **how** we're going to build it. Rules answer:

- What conventions does the AI follow?
- What patterns are required, and which are forbidden?
- What does "good" look like in this project?

Without rules, every session re-decides things the AI should already know. With rules, the AI stays consistent across hundreds of small choices.

## What's in this folder

| File | What it covers |
| --- | --- |
| `build-rules.md` | The starter rules — 10 universal principles that apply to any project |
| `how-to-add-rules.md` | The format and process for adding new rules as you discover patterns |

## When to add a new rule

When you notice a pattern that should apply to **all future work** in this project. Examples:

- *"I keep telling the AI to write commit messages in present tense" → add a rule.*
- *"I keep correcting the AI about file naming" → add a rule.*
- *"There's a specific way I want errors handled" → add a rule.*

If you find yourself giving the same correction more than twice, that's the signal — write a rule.

## When NOT to add a rule

Don't add rules for one-time decisions. *"For this feature only, use library X"* is a **decision record** (lives in `documentation/decisions/`), not a rule.

Rules are **always-true**. Decisions are **point-in-time**.

## The Premium-tier rules

The Build Kit ships with 10 starter rules. They're enough for a first project. They're not enough for production software.

**AI Code that Works Premium** adds the full rules library:

- Database & data integrity (multi-tenant, RLS, migrations)
- Security (auth, secrets, isolation)
- Testing (unit, contract, E2E, browser verification, the "fix the bug not the test" rule)
- Observability (Sentry, PostHog, audit events, the four-layer feedback loop)
- Integrations (typed clients, contract tests, idempotency)
- Agent rules (structured outputs, approval gates)
- Design rules (semantic tokens, recipes)
- CI/CD (drift checks, lint rules, merge queue)

When the Kit's 10 rules stop being enough, that's the moment to upgrade. See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Phase 2 of the AI Code that Works method. Learn the full method at [https://www.skool.com/aicodethatworks](https://www.skool.com/aicodethatworks).*
