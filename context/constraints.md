# Constraints

_What we can't change, won't change, or have to work within. The fences around the build._

**Status:** Provisioning · **Last updated:** 2026-08-01

---

## Time

No hard deadline. Flexible timing — prioritizing getting it right over shipping fast, but scoped to a small first version so "getting it right" doesn't turn into stalling.

## Budget

$0/month on tools. Plenty of personal time available instead. Must run entirely on free tiers (GitHub Actions free tier, free official platform APIs).

## Technical constraints

- No browser automation or scraping — posts go out via each platform's official API only (Meta Graph API for Facebook/Instagram, LinkedIn API for personal profile), to avoid fragile bots and ToS risk.
- Instagram posting requires a Business/Creator account linked to a Facebook Page — a Meta platform requirement.
- LinkedIn posting is scoped to the personal profile (Company Page posting needs a separate, harder-to-get API approval — out of scope for v1).
- Runs as a scheduled background job on **GitHub Actions** (free tier) — not a browser-facing app.
- Platforms for v1: Facebook, Instagram, LinkedIn.

## What we WON'T compromise on

Reliability. Posts have to actually go out, and failures can't be silent — if something breaks, it has to be obvious.

## What we WILL compromise on

"Perfect" up front. First version is intentionally small — one account, three platforms, fully automatic posting, no analytics, no video. Polish and expanded scope come in later iterations, not the first ship.

## Updates log

- **2026-08-01** — Initial provisioning. First version of this file.

---

*Phase 1 file — Context. See `README.md` in this folder for the framing.*
