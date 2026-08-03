# Plans — Active Work

_What we're working on right now. Short markdown files naming the current feature, phase, or task. Edited actively; archived or deleted when done._

---

## What goes here

A **plan** is a short document describing what's being built right now. Typical contents:

- The feature or slice being worked on
- The definition of done for THIS specific work (mirrors what's in `../../verification/definition-of-done.md` for the current feature)
- The current state — what's done, what's next, what's blocked
- Any specific notes or constraints for this work

Plans are **living** — you edit them as the work evolves. When the work ships, you archive or delete the plan.

## Format

There's no strict template — plans are utilitarian. A typical plan file might look like:

```markdown
# Plan — Customer Reconciliation Feature

**Started:** 2026-05-27
**Status:** In progress

## What we're building

A weekly reconciliation report that pulls payments from Stripe, matches them to invoices, and flags mismatches.

## Definition of done for this slice

- Pulls Stripe payments for a date range
- Matches to invoice records in the local data
- Produces a markdown report listing matches + mismatches
- Saves the report to `reports/YYYY-MM-DD-reconciliation.md`

## Current state

- ✓ Stripe API connection working
- ✓ Pulling test data
- → Working on matching logic
- ⨯ Mismatch flagging (next)
- ⨯ Report generation (after)

## Notes

- Stripe API rate limits — built-in 100 req/min. Should be fine for weekly use.
- Date range defaults to "last 7 days" but accepts overrides.

## Open questions

- Should mismatches be sorted by amount or by date? — Going with date for v1. Easy to flip.
```

## When to write a plan

When you're about to start a new feature, slice, or significant piece of work. The plan answers *"what am I working on right now?"* in a form the AI can read.

## When to delete or archive

When the work ships and the plan is no longer accurate, **delete it** (or move it to `archive/` if you want a record). Stale plans confuse the AI — they describe a state that no longer exists.

If the work taught you something durable, that goes into:

- **A new decision record** (`../decisions/`) if it was a meaningful choice
- **A new rule** (`../../rules/`) if it's a pattern that applies forever
- **The feedback log** (`../../feedback/feedback-log.md`) for *"here's what we learned"*

The plan itself doesn't need to be preserved.

## The Premium-tier discipline

The Build Kit's plans folder is for active solo work. **AI Code that Works Premium** adds:

- **Phase specs** — formal, dispatchable plan documents that can be handed to AI workers
- **Build session plans** — the per-session work plan with context-loaded, parallelizable tasks, verification steps
- **The full template system** — PHASE_SPEC, BUILD_SESSION_PLAN, HANDOFF templates with sub-spec composition
- **Multi-session orchestration** — running parallel workers against the same plan, integration branches, merge queues

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Plans — `documentation/plans/`. Part of Phase 3 in the AI Code that Works method.*
