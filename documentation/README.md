# Documentation — Phase 3

_The project's memory. What was decided, what's in flight, what we know. Without documentation, every new AI session starts from scratch — and the AI invents the project anew, every time._

---

## Why Documentation comes third

After **Context** (what we know about the project) and **Rules** (what we will and won't do), the third phase is **the running memory** of decisions made, plans in flight, and reference material.

The big idea: **documentation is a byproduct of the build, not a separate task done later.** Rules make this true — *"Documentation as a byproduct"* is starter rule #3. With that rule in place, the AI updates docs as it works.

## What's in this folder

Three subfolders, each with its own purpose:

| Folder | What lives here |
| --- | --- |
| `decisions/` | Decision records — the **why** behind every meaningful choice. One file per decision. Numbered. |
| `plans/` | Active plans — **what we're working on right now**. Short markdown files naming the current feature/phase. |
| `reference/` | Static reference docs — API documentation, design specs, external resources the AI needs to read. |

## The three kinds of docs — and the canonical separation

The three subfolders matter. Mixing them up is how documentation rots:

- **Decisions** explain *why* — frozen at a point in time, never edited after writing.
- **Plans** explain *what's happening now* — actively edited, replaced or archived when done.
- **Reference** explains *how* — static knowledge the AI consults but doesn't write.

If you find yourself wanting to put something in two of these, ask: *"Which is this primarily?"* Pick one. Cross-reference from the others.

## How the AI uses documentation

When the AI is about to make a decision:

1. **It checks `decisions/`** for past decisions that touch the same area. If a past decision is relevant, the AI should mention it.
2. **It checks `plans/`** for what's currently in flight that this decision affects.
3. **It checks `reference/`** for static facts it needs (API shapes, design specs).

If the AI is making a meaningful choice and there's no relevant decision recorded, that's the signal to **write a new decision record**.

## When to update which

- **Made a meaningful choice** (architecture, tech stack, scope) → new file in `decisions/`. **Don't edit past decisions** — write a new one that supersedes the old one, with a link back.
- **Started a new feature or phase** → new file in `plans/`. Edit it as the work evolves. Archive it (move to `plans/archive/` or just delete) when done.
- **Need to give the AI external knowledge** (an API spec, a design system, a third-party tool's docs) → add it to `reference/`.

## The Premium-tier documentation discipline

The Build Kit teaches the *pattern* of documentation. **AI Code that Works Premium** teaches:

- The 47-decision case-study archive from the actual harness build, with the incident history behind each
- Cross-PR decision-awareness (AI checks new decisions against past ones for contradictions)
- The ADR (Architecture Decision Record) format with status, supersession chains, and impact analysis
- Phase specs, build session plans, and the full templating system
- How documentation engines work (rules that make the AI write docs automatically)

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Phase 3 of the AI Code that Works method. Learn the full method at [https://www.skool.com/aicodethatworks](https://www.skool.com/aicodethatworks).*
