# Verification Checks

_The universal pre-ship checklist. Run this before calling any feature done, alongside the feature-specific Definition of Done._

---

## How to use this file

1. After the AI says *"I've finished,"* don't believe it yet.
2. Open this file. Work through each section.
3. **For each box you check, you must have actually verified it** — not assumed.
4. Find at least one thing wrong. Fix it.
5. When every box is honestly checked, the feature is shippable.

---

## Section 1 — Did the AI actually build what was asked?

- [ ] Re-read `definition-of-done.md` for the current feature. Does what was built match each criterion?
- [ ] Re-read the relevant `context/` files. Does the build respect the project's context (user, constraints)?
- [ ] Re-read `../rules/build-rules.md`. Does the build follow the rules?

If any answer is *"not quite"* — that's the bug. Fix it before continuing.

## Section 2 — Did you run it with real input?

- [ ] You executed the feature end-to-end (not just the AI's demo).
- [ ] You tried at least one **valid** real-world input. It produced the expected output.
- [ ] You tried at least one **edge case** — empty input, very large input, weird-but-valid input, unexpected combinations.
- [ ] You tried at least one **invalid input** to see how the feature fails. The failure was visible and informative, not silent.

## Section 3 — Did you read the output?

- [ ] If the feature produces a file, you **opened the file** and read it.
- [ ] If the feature produces screen output, you **looked at it carefully** — not skimmed.
- [ ] You asked: *"If a stranger used this and saw this output, would I be okay with it?"* The answer is yes.
- [ ] Labels, headers, and names are clear (not placeholder-y like *"Result"* or *"Output 1"*).

## Section 4 — Did the project's memory get updated?

- [ ] Any meaningful decisions made during the build are recorded in `../documentation/decisions/`.
- [ ] Any new rule that emerged from the build is added to `../rules/build-rules.md`.
- [ ] Any plan file in `../documentation/plans/` for this feature is updated to reflect what actually happened.
- [ ] If something in `../context/` is now wrong (assumption turned out incorrect), it's corrected.

## Section 5 — Did you find at least one thing wrong?

- [ ] **You found at least one issue** — a subtle bug, an awkward default, a wrong edge case, an unclear label, a missing thing — and you fixed it.
- [ ] If you found zero issues, you went back and looked harder.

> **This is non-negotiable.** AI-built work almost always has at least one *something*. If your first pass found nothing, you didn't actually verify — you skimmed. Run the checks again, this time looking for what's wrong instead of confirming what's right.

## Section 6 — Did the feedback loop close?

- [ ] You captured what you learned from this build in `../feedback/feedback-log.md`.
- [ ] You know what the **next** build needs (next slice, next feature, next fix).
- [ ] If the build revealed a wrong assumption, the assumption is corrected upstream (in context, rules, or a new decision).

---

## When every box is honestly checked

The feature is **done** — to the standard the Build Kit's discipline produces. Ship it.

If this is your first build, also run through the parent Build Kit's **`../../FIRST-BUILD-CHECKLIST.md`** — the five-phase version of the same check.

After shipping, see **`../../WHAT-COMES-NEXT.md`** — the Build Challenge or Premium path.

---

## Premium-tier verification

The Build Kit's verification is **functional verification** — does it work? **AI Code that Works Premium** adds **production-readiness verification**:

- **Browser verification** — Playwright MCP loops with real interaction, console-error checking, responsive viewport testing
- **RLS verification** — proof that cross-tenant access is impossible by integration test
- **Observability verification** — Sentry breadcrumbs, audit events, usage events all wired correctly
- **Deploy verification** — production artifact reaches READY, not just "build succeeded"
- **Security verification** — pentest skill, secrets scan, RLS audit

The Kit's verification is sufficient for first builds and personal projects. Premium's verification is what you need before real users touch the software.

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Phase 4 file — Verification. See `README.md` in this folder for the framing.*
