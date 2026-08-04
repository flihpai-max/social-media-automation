# Decision 0003 — Host images for Instagram via the public GitHub repo

**Date:** 2026-08-03
**Status:** Accepted
**Author:** Project owner

---

## Context

Instagram's Graph API (unlike Facebook's) does not accept a direct file upload for posting — its Content Publishing API requires a **public URL** it can fetch the image from. Options considered:

1. **Public GitHub repo raw URL.** Commit the image to an `assets/` folder in the project's GitHub repo (already required for GitHub Actions, per decision 0002) and use its `raw.githubusercontent.com` URL. Free, no new signups, but requires the repo to be public — private-repo raw URLs aren't fetchable without auth, which Instagram's fetcher can't provide.
2. **Free image hosting service** (e.g. imgbb). Keeps images out of git history, but requires signing up for a new account and managing another API key/credential.

## Decision

Use **option 1** — commit images to a public `assets/` folder in the GitHub repo and reference them via their raw GitHub URL for Instagram's API calls.

## Rationale

- No new signups or credentials — the project already needs a GitHub repo for Actions scheduling (decision 0002).
- $0 cost, matching the budget constraint.
- The images being posted are, by definition, going to be published publicly to Facebook/Instagram/LinkedIn anyway — briefly hosting them in a public repo isn't materially new exposure.

## Consequences

- **The project's GitHub repo must be public**, not private. This was set up as public at repo creation.
- **Posted images become part of git history.** They aren't meant to be removed/private later — this fits the use case (public social content), but would need revisiting if the tool were ever used for non-public draft images.
- **The posting flow gains a git-push step** before calling Instagram's API — the script needs to commit and push the image before Instagram can fetch it, adding a dependency on network/GitHub availability at post time, not just at Facebook/LinkedIn post time.

---

*Phase 3 file — Documentation. See `documentation/README.md` for the framing.*
