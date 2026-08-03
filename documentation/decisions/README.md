# Decisions — Decision Records

_The **why** behind every meaningful choice in this project. One file per decision. Numbered sequentially. Never edited after writing — superseded by a new decision instead._

---

## What goes here

A **decision record** captures a single meaningful choice — typically about architecture, tech stack, scope, or a major trade-off. Examples of choices that deserve a decision record:

- Which tool/stack to build in
- Whether to support multi-user or stay single-user
- A pivot in scope or audience
- A specific way of handling a recurring pattern
- A trade-off that wasn't obvious (chose X over Y because Z)

## What does NOT go here

- **Daily build steps** — those live in `../plans/`.
- **Always-true rules** — those live in `../../rules/`.
- **External knowledge** — that lives in `../reference/`.

If a choice was obvious or trivial, it doesn't need a decision record. The bar: *"Six months from now, would I want to know why I chose this?"* If yes, write it.

## The format

See `0001-example-decision.md` for the worked example. The template is:

```markdown
# Decision NNNN — Title (short, imperative — what was decided)

**Date:** YYYY-MM-DD
**Status:** [Proposed / Accepted / Superseded by NNNN / Reversed]
**Author:** [name or "the team"]

## Context

What was the situation? What problem needed a decision? What options were considered?

## Decision

What we decided — in one or two sentences. Direct, not hedged.

## Rationale

Why we chose this. The reasoning — what made this the right choice given the context.

## Consequences

What this commits us to. What changes downstream. Both the upside and the trade-offs.
```

## Numbering

Decisions are numbered sequentially: `0001`, `0002`, `0003`, etc. **Don't reuse numbers.** When a decision is superseded, the new decision gets the next number — the old one stays with its original number, with its status updated.

## When a decision is wrong

You will write decisions that turn out to be wrong. That's fine. The protocol:

1. **Don't edit the old decision.** It's a historical record of what was thought at the time.
2. **Write a new decision** that supersedes it. Reference the old one explicitly.
3. **Update the old decision's status** to *"Superseded by NNNN"* and link to the new one.

This preserves the *why* — future-you sees not just *"we do it this way"* but *"we tried it the other way and learned this lesson."*

## When to write one

The signal: **you're about to make a choice that future-you will want to know the reason for.** If yes, write the decision first, then act. The act of writing often surfaces a better option.

If you keep deferring writing the decision, write it shorter. Three sentences is better than no decision.

## The Premium-tier discipline

The Build Kit's example is one decision record. The full discipline includes:

- **ADR (Architecture Decision Record)** structure with formal status lifecycle
- **Cross-PR contradiction detection** — AI catches when a new decision contradicts an old one
- **Decision archive** that compounds over months into a real project history
- **The 47-decision archive** from the actual AICTW harness build

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Decision records — `documentation/decisions/`. Part of Phase 3 in the AI Code that Works method.*
