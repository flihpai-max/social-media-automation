# Definition of Done

_What "done" means for the current feature. Set this **before** you start building — not after. Update as the project evolves; archive past definitions in the feedback log._

**Current feature:** First posting pipeline — image to published post across Facebook, Instagram, LinkedIn
**Date set:** 2026-08-01
**Status:** In build

---

## What "done" means for this feature

### Required outcomes

- [x] Given one image + caption, the script posts it to the connected Facebook Page. *(Verified 2026-08-03: posted to "Leap High Services" Page, confirmed visible on Facebook.)*
- [x] The same image + caption posts to the connected Instagram Business account. *(Verified 2026-08-03: posted to "Leap High Services" IG account, confirmed visible on Instagram.)*
- [x] The same image + caption posts to the connected LinkedIn personal profile. *(Verified 2026-08-03: posted to personal LinkedIn profile, confirmed visible on LinkedIn.)*
- [ ] The script runs successfully as a scheduled GitHub Actions job — not just locally.

### Required behaviors

- [ ] Given valid credentials and a valid image, all three posts succeed and each platform's result is logged clearly.
- [ ] If a credential is missing/invalid or a post to one platform fails, that failure is logged visibly (not swallowed) — and it doesn't block attempts on the other platforms.
- [ ] Each run produces a log showing per-platform success/failure.

### Required quality bar

- [ ] No silent failures — errors are visible
- [ ] Output is readable by the user without explanation
- [ ] Re-running it doesn't break existing data
- [ ] At least one edge case tested

---

## How to use this file

1. **Before starting the feature:** fill in the specific outcomes, behaviors, and quality criteria. Be concrete — *"Produces a markdown file at `reports/YYYY-MM-DD-reconciliation.md`"* not *"Generates a report."*
2. **While building:** check this file when in doubt. *"Does this satisfy the DoD?"* If not, either keep building or update the DoD (and write a decision record explaining why).
3. **Before calling done:** every box must be checked. If a box can't be checked, the work isn't done.
4. **When shipped:** mark status *"Verified — shipped"* with the date. Archive this file's contents in the feedback log if you want a historical record, then replace this with the next feature's DoD.

## A note on scope

The DoD is **for the current feature, not the whole project**. If the DoD has 20 bullets, you're scoping too big. Break the feature into slices, set a DoD per slice, ship each one.

The Build Kit's starter rule #1: ***"One thing at a time."*** This file enforces that — if you can't tightly define done for the thing you're about to build, the thing is too big.

## What goes in the DoD vs. the verification checks

| Type of criterion | Goes in... |
| --- | --- |
| Feature-specific outcomes ("this report includes X, Y, Z") | This file (`definition-of-done.md`) |
| Universal quality bar ("no silent failures, edge cases tested") | `verification-checks.md` |
| Long-term project standards ("we always use semantic naming") | `../rules/build-rules.md` |

If a criterion appears in two places, the DoD wins — it's specific to this work.

## Past DoDs

[ARCHIVE past Definitions of Done here as you ship features, OR archive in `../feedback/feedback-log.md`. Keeping a record helps with feedback analysis later.]

- **[FEATURE 1 NAME]** — completed [DATE]. See `../feedback/feedback-log.md` for what was learned.
- **[FEATURE 2 NAME]** — completed [DATE].

---

## Premium-tier additions

**AI Code that Works Premium** adds DoD templates for specific work types:

- **UI changes** — DoD includes browser verification at 375/768/1280px, accessibility check, design-system token compliance
- **Schema changes** — DoD includes RLS verification, migration safety, test fixture extension
- **Integration changes** — DoD includes contract tests, error taxonomy mapping
- **Infrastructure changes** — DoD includes post-merge deploy READY check, config drift validation

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Phase 4 file — Verification. See `README.md` in this folder for the framing.*
