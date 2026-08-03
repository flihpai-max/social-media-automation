# Verification — Phase 4

_How we know the AI's work actually works. The discipline that turns "it ran" into "it's done."_

---

## Why Verification comes fourth

After **Context** (what we know), **Rules** (what we follow), and **Documentation** (the project's memory), Phase 4 is **proof**. Specifically: proof that what the AI built does what it was supposed to do.

The brand's line for this: ***"Never trust static success alone."*** Lint passes, the AI says it works, the code compiles — none of that is verification. Verification is **running the thing and checking that the output matches the intent**.

## What's in this folder

| File | What it captures |
| --- | --- |
| `definition-of-done.md` | What "done" means for the current feature — the criteria the work must pass |
| `verification-checks.md` | The pre-ship checklist — what to actually do before calling work done |

## The cardinal rule

**Find at least one thing that's wrong, then fix it.**

If you ran verification and found zero issues, you didn't look hard enough. AI-built work almost always has at least one subtle bug, awkward default, wrong edge case, or unclear output. Finding it is what separates *"shipped"* from *"shipped well."*

## When to run verification

- **Before calling any feature done** — even small ones.
- **After the AI says "I've finished"** — that's the moment to verify, not before.
- **Before merging into the project's mainline** (if you're using a branch).
- **Before showing the work to anyone else.**

## The two-layer verification

| Layer | What it checks | When to run |
| --- | --- | --- |
| **Definition of Done** | The specific criteria for this feature | Before *every* feature ships |
| **Verification Checks** | The general "did we do this right?" sweep | Same — paired with the DoD |

Both are required. The DoD is feature-specific; the Verification Checks are universal.

## The Premium-tier verification discipline

The Build Kit's verification is the lite version. **AI Code that Works Premium** adds:

- **Browser verification loops** — Playwright MCP, real end-to-end testing as a real-time self-debugging step
- **Definition of Done templates** for specific work types (UI changes, schema changes, integration changes, infrastructure changes)
- **Preview-deployment verification** — protection-bypass patterns, ephemeral environments per PR
- **Drift checks** — automated checks that catch when the project's structure diverges from its rules
- **Codex CLI integration** — local second-opinion code review before PR
- **Deploy verification** — post-merge production-artifact-READY checks
- **The `verify` skill** — a runnable playbook that automates the verification flow

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Phase 4 of the AI Code that Works method. Learn the full method at [https://www.skool.com/aicodethatworks](https://www.skool.com/aicodethatworks).*
