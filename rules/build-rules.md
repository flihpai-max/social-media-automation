# Build Rules

_The rules this project follows. Read these before writing any code or content. If a rule needs to bend, write a decision record explaining why (lives in `documentation/decisions/`)._

**Status:** Active · **Last updated:** 2026-08-01

---

## The starter rules

Ten universal rules. They apply to any project. Add project-specific rules below them.

### 1. One thing at a time

Build the smallest reasonable slice end-to-end before starting the next slice. **Don't half-build five things.** Half-built work compounds into chaos faster than any other failure mode.

### 2. Define "done" before you build

Every feature gets a clear definition of done in `../verification/definition-of-done.md` **before** code or content gets written. If you can't define done, you don't understand the feature well enough yet.

### 3. Documentation as a byproduct

Decisions get recorded **as they're made**, not later. Active plans live in `../documentation/plans/`. Don't ship without updating the relevant doc. If you find yourself thinking *"I'll document this after,"* the project's memory is already rotting.

### 4. Verify the output, not the input

*"The AI built it"* is not evidence. *"The AI said it works"* is not evidence. **Test it with real input.** Find the thing that's wrong. Fix it. Then call it done.

### 5. Be specific about names

Files, functions, sections, components — names matter. *"utils.md"* is a smell — there's no such thing as utils. *"customer-billing-reconciler.md"* is a name. **Name the thing what it actually is.**

### 6. Plain language for the human, structured language for the AI

README files and walkthroughs are for **humans** — read them aloud and see if they sound natural. Rules files and routers are for the **AI** — they can be terse, structured, list-heavy. Different audiences, different tone.

### 7. No magic numbers

If a value matters, name it. *"24 hours"* not *"86400"*. *"the maximum brief length"* not *"500"*. If you must use a number, **explain what it is** in a comment.

### 8. Errors are visible

If something fails, you should see it fail. Silent failures = compounded debt. If a step might fail, log it. If a fallback runs, log it. If something gets skipped, log it.

### 9. One canonical way

If there are two ways to do the same thing in this project, **pick one**. Document the pick (in `../documentation/decisions/`). Stop using the other. Duplication is the second-fastest path to a broken project.

### 10. Stop when stuck — don't guess

If the AI is about to make a choice that affects the rest of the build and you (the human) aren't sure — **pause and decide first**. The AI guessing wrong at scale produces worse work than the AI waiting for input.

---

## Project-specific rules

### 11. No browser automation or scraping — official APIs only.

*Browser bots break on every UI update and risk getting accounts flagged for violating platform terms of service.*

### 12. API credentials never get committed to the repo — stored only in GitHub Actions secrets.

*This automation holds live tokens for the Facebook, Instagram, and LinkedIn accounts. A leaked token is an account compromise, not just a bug.*

---

## How to add a new rule

See `how-to-add-rules.md` for the format and process.

---

## What's NOT in this file

Production-grade engineering rules — database/RLS, security/auth, testing patterns, observability, integration patterns, design system, CI/CD — live in **AI Code that Works Premium**, not here. The Build Kit covers the universal patterns; Premium covers the engineering-depth rules. See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Phase 2 file — Rules. See `README.md` in this folder for the framing.*
