# Decision 0004 — LinkedIn: 3-legged OAuth via a local callback script

**Date:** 2026-08-03
**Status:** Accepted
**Author:** Project owner

---

## Context

Unlike Facebook (which offers a Business Manager System User token that can be generated entirely through the UI), LinkedIn's API only supports standard OAuth 2.0 3-legged authorization for personal-profile posting (`w_member_social` scope via "Share on LinkedIn"). This requires a real authorization-code exchange: redirect the user to LinkedIn's consent screen, catch the redirect with a code, and exchange that code for an access token using the app's Client ID and Client Secret.

## Decision

Built `src/linkedin_auth.py` — a one-time local script that starts a temporary local HTTP server on `localhost:8765`, opens the user's browser to LinkedIn's authorization URL, catches the redirect, exchanges the code for an access token, and writes it into `.env`. `src/linkedin_post.py` then uses that stored token for actual posting.

## Rationale

- LinkedIn doesn't offer a simpler token-generation path for this scope — the 3-legged flow is required.
- Running the callback server locally means the app's Client Secret never has to be typed into a browser field or handled outside the project's own `.env`.

## Consequences

- **The access token is short-lived (LinkedIn's standard is ~60 days) with no refresh token for this app type.** Unlike the Facebook System User token (decision 0002), this one *will* expire and require re-running `src/linkedin_auth.py` manually — a real gap against the "reliability, no silent failures" constraint (`context/constraints.md`) once this runs unattended on a schedule (decision 0002's GitHub Actions plan). This needs to be addressed before or shortly after the GitHub Actions wiring — either by monitoring for auth failures and alerting, or investigating LinkedIn's refresh-token program.
- **`src/linkedin_auth.py` only works when run locally** (it needs a browser and a reachable `localhost` callback) — it cannot run inside GitHub Actions. The access token must be generated locally and stored as a GitHub Actions secret, then refreshed locally and re-uploaded whenever it expires.
- One real debugging note for future reference: the token exchange initially failed with `invalid_client` even with seemingly correct credentials — the fix was regenerating the Client Secret on LinkedIn's Auth tab and copying the fresh value. If this recurs, regenerating the secret is the first thing to try.

---

*Phase 3 file — Documentation. See `documentation/README.md` for the framing.*
