# Decision 0002 — Build on official platform APIs, scheduled via GitHub Actions

**Date:** 2026-08-01
**Status:** Accepted
**Author:** Project owner

---

## Context

I needed a way to automatically post generated content to Facebook, Instagram, and LinkedIn on a schedule, with $0 monthly budget and no browser/UI requirement for the automation itself. Options considered:

1. **Browser automation / scraping bots.** No API approval needed, but fragile — breaks on every UI update — and risks accounts being flagged for violating platform terms of service.
2. **A paid scheduling tool** (e.g., Buffer, Hootsuite). Reliable and well-supported, but costs money, which conflicts with the $0 budget constraint.
3. **Official platform APIs (Meta Graph API, LinkedIn API), run as a scheduled script.** Free for personal use, sanctioned by the platforms, but requires more setup (app registration, tokens, Meta's Instagram-via-Facebook-Page requirement).

For hosting/scheduling, options considered:

1. **Run locally** (e.g., Windows Task Scheduler). No cloud cost, but only posts when the machine happens to be on — undermines the "consistent posting" goal.
2. **GitHub Actions (free tier).** Free, runs on a schedule regardless of whether any personal machine is on.

## Decision

Build the automation as a **Python script using official platform APIs** — Meta Graph API for Facebook Page and Instagram Business account posting, LinkedIn API for personal profile posting — **scheduled via GitHub Actions** (free tier), with credentials stored only in GitHub Actions secrets.

## Rationale

- Matches the $0 budget constraint — every piece (APIs, GitHub Actions) is free for this scale of use.
- Avoids the ToS risk and fragility of browser automation (rule 11 in `rules/build-rules.md`).
- GitHub Actions runs on schedule independent of any personal machine being powered on, which directly serves the "consistent posting" goal from `context/user.md`.
- Keeps credentials out of the codebase by using GitHub Actions secrets (rule 12 in `rules/build-rules.md`).

## Consequences

- **Instagram posting requires a Business/Creator account linked to a Facebook Page.** This is a Meta platform requirement, not a design choice — it constrains account setup before any code runs.
- **LinkedIn posting is scoped to the personal profile.** Posting to a LinkedIn Company Page would require separate, harder-to-get API approval — explicitly out of scope for v1 (see `context/constraints.md`).
- **Secrets management becomes a real operational requirement.** API tokens for three platforms must be generated, stored in GitHub Actions secrets, and rotated if they expire or leak — not an afterthought.
- **No visual/browser interface for v1.** The automation is a background job; any future dashboard or approval UI would be a new decision, not an extension of this one.

---

*Phase 3 file — Documentation. See `documentation/README.md` for the framing.*
