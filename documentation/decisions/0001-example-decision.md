# Decision 0001 — Use the AI Code that Works Build Kit as the project scaffold

**Date:** 2026-05-27 (example — replace with your real date)
**Status:** Accepted
**Author:** [The project owner — example placeholder]

---

## Context

I needed a starting scaffold for building [PROJECT NAME] with AI-assisted development. Three options were on the table:

1. **Start from a blank folder.** Full flexibility, but every structural decision has to be made from scratch — the AI has nothing to read, no rules to follow, no documentation discipline. Easy to start, fast to drift into chaos.
2. **Use a generic framework template** (e.g., a Next.js starter, a Python project template). Provides structure for code, but no opinion about AI-assisted development. The AI would still be ungoverned even if the code structure is clean.
3. **Use the AI Code that Works Build Kit.** Provides both: folder structure organized around the five-phase method (Context → Rules → Documentation → Verification → Feedback Loops) AND starter rules + templates that govern how the AI works inside that structure.

## Decision

I chose **option 3 — the AI Code that Works Build Kit.**

## Rationale

- The Build Kit is designed specifically for AI-assisted development, not just code organization. It gives the AI structure to work within from day one.
- The five-phase method (Context → Rules → Documentation → Verification → Feedback Loops) covers the lifecycle of any build — not just initial setup.
- The starter rules cover the universal patterns that apply to any project. I can add project-specific rules without throwing away the baseline.
- The pattern is portable — anything I learn building this project applies directly to the next one. I'm investing in a method, not just in this build.
- When this project outgrows the Kit (production users, real data, scaling concerns), there's a known upgrade path: AI Code that Works Premium.

## Consequences

- **This project's structure follows the AICTW conventions.** Anyone familiar with the method can navigate it immediately. Anyone not familiar can learn the method via the free Foundations course on Skool ([https://www.skool.com/aicodethatworks](https://www.skool.com/aicodethatworks)).
- **I'm committing to maintain the five-phase discipline.** If I skip phases (no context, no verification, no feedback loop), I'll regret it — and I'll know exactly which phase I skipped.
- **Project-specific rules and decisions accumulate alongside the starter ones.** The Kit's defaults are starting points, not constraints.
- **The Kit is sufficient for the first build.** When the project hits a wall (e.g., I need RLS, observability, multi-tenancy, CI/CD), Premium's deeper rules are the natural next step rather than a rewrite.

---

## Note: how this decision record is structured

This is an **example** of how to write a decision record. Every meaningful choice should get one. The format:

- **Title** — what was decided, in short imperative form.
- **Date, Status, Author** — metadata.
- **Context** — the situation, the options, the relevant trade-offs.
- **Decision** — what was chosen, in one or two sentences.
- **Rationale** — why that choice.
- **Consequences** — what the choice commits the project to.

For more on decision records, the AICTW method, and the discipline that compounds them: the free Foundations course on Skool — [https://www.skool.com/aicodethatworks](https://www.skool.com/aicodethatworks).

**Premium adds:** the 47-decision archive from the actual harness build, ADR format with full lifecycle, cross-PR contradiction detection, decision-supersession chains. See the parent Build Kit's `WHAT-COMES-NEXT.md`.
