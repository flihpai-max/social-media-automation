# Feedback Loops — Phase 5

_What we learned from each cycle, fed back into the next. The phase that takes the project from "ran once" to "gets better over time."_

---

## Why Feedback Loops come fifth — and matter most

The first four phases are about **shipping a thing**. The fifth phase is about **shipping a system that improves**.

Without the feedback loop, every cycle repeats the same mistakes. The AI makes the same wrong choices because nothing learned from yesterday gets fed into tomorrow. The project stays the same shape forever.

With the feedback loop, every cycle teaches:

- A new rule (because we kept making the same correction)
- A corrected assumption (because the context was wrong)
- A new decision record (because we made a choice we'll want to remember)
- A revised approach (because what we tried didn't work)

## What's in this folder

| File | What it captures |
| --- | --- |
| `feedback-log.md` | The running log — what we tried, what worked, what didn't, what we learned, what changed |

## How feedback flows

After each meaningful cycle (a feature shipped, a sprint closed, a Build Challenge wrap-up, even a single failed attempt), capture:

1. **What we tried** — the approach, the plan, the tool, the technique.
2. **What happened** — what worked, what broke, what surprised us.
3. **What we learned** — the durable insight.
4. **What changed as a result** — new rule? corrected context? new decision record?

The output isn't just the log entry. The output is the **change to the project** — a rule added, context updated, a decision recorded. The log is the audit trail; the actual learning lives in the upstream files.

## The mistake people make here

The mistake is treating Phase 5 as "write a retro after the project ends." That's too late. **Capture feedback continuously, not at the end.** Every time something surprises you — log it. Every time you correct the AI — log it. Every time an assumption turns out wrong — log it.

The smaller and more frequent the entries, the more valuable the log becomes.

## When to update the upstream files

| If you learned... | Update... |
| --- | --- |
| A pattern that should apply forever | `../rules/build-rules.md` (new rule) |
| An assumption that was wrong | `../context/` (correct the relevant file) |
| A choice you'll want to remember | `../documentation/decisions/` (new decision record) |
| What's currently being built has changed | `../documentation/plans/` (update the active plan) |

The feedback log itself is the **history**. The upstream files are the **living memory.**

## The Premium-tier feedback discipline

The Build Kit teaches the *pattern* of feedback loops. **AI Code that Works Premium** adds:

- **Observability loops** — Sentry + PostHog + audit events + ledger, all fed back into the build cycle
- **Drift checks** — automated detection of when the project's structure diverges from its rules
- **AI review loops** — Codex CLI + Claude reviews on every PR, with the findings feeding back into the rules
- **End-of-phase sweeps** — the `/p2-sweep` skill, the codebase-wide weekly Claude review
- **The "every catch block captures to Sentry" pattern** — failure as input, not as silent loss

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Phase 5 of the AI Code that Works method. Learn the full method at [https://www.skool.com/aicodethatworks](https://www.skool.com/aicodethatworks).*
