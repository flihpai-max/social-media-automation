# Feedback Log

_What we tried, what happened, what we learned, what changed. Add entries continuously — not just at the end._

---

## How to use this file

Each entry has a simple format:

```markdown
## [DATE] — [SHORT TITLE]

**What we tried:** [Brief description.]

**What happened:** [What actually occurred. Both what worked and what didn't.]

**What we learned:** [The durable insight.]

**What changed:**
- [Updated file or new artifact 1]
- [Updated file or new artifact 2]
```

Keep entries short — a few sentences each. If you find yourself writing a full essay, the entry probably contains multiple learnings; split them.

## When to add an entry

- After every feature shipped
- After every failed attempt (yes — failures are the highest-value entries)
- Whenever something **surprises** you (good or bad surprise)
- Whenever you find yourself **correcting the AI on the same thing again**
- At the end of every week — even a "nothing new" entry is a valuable signal

## Entries

[Add your entries below. Newest at the top.]

---

## 2026-08-04 — Wiring GitHub Actions surfaced a real bug and a recurring paste problem

**What we tried:** Wired `post_all.py` into a manual-trigger GitHub Actions workflow, added the three secrets, and ran it.

**What happened:** Two separate issues, both worth remembering:
1. Manually pasting long tokens (LinkedIn Client Secret, then all three GitHub Actions secrets) into web UI fields silently corrupted them multiple times — errors showed as "invalid_client" or "cannot parse access token." Switched to setting GitHub secrets via the API (`tools/set_github_secrets.py`, sealed-box encrypted) instead of the web form, which fixed it immediately.
2. Once secrets were correct, all three platforms still failed — on the *image* this time. Root cause: `github_image_host.py` opened the same file for read and write when `image_path` equals the `assets/` destination (exactly what the CI default does), which truncated it to zero bytes before copying. The CI job's own commit pushed that corrupted 0-byte file to the repo, silently breaking every platform's read of it.

**What we learned:** Any time a long secret is hand-typed or pasted through a browser text field, assume it can get corrupted — verify or use an API/clipboard path instead of trusting the paste. Separately: never open the same path for both read and write in one `with` statement — read fully into memory first, or check for the same-path case explicitly.

**What changed:**
- `tools/set_github_secrets.py` — new local tool, sets GitHub Actions secrets via API instead of the paste-prone web UI.
- `src/github_image_host.py` — fixed the same-path truncation bug; raw URLs now use the commit SHA instead of the branch name (avoids a CDN-staleness issue we also hit).
- `assets/test-image.jpg` — restored after the corrupting commit.

---

## 2026-08-01 — Started the project

**What we tried:** Provisioned the project using the AI Code that Works Build Kit. Filled in initial context, reviewed starter rules, wrote the first decision record (choice of the Build Kit itself).

**What happened:** Provisioning was conversational and quick — walked through project/user/constraints context, the starter rules, and the first decision (API-based automation on GitHub Actions) one question at a time.

**What we learned:** Being specific early (e.g. exact platforms, exact scope-out list) paid off later — every downstream technical decision (Instagram's image-hosting approach, LinkedIn's OAuth flow) referenced back to the constraints set during provisioning instead of re-litigating scope each time.

**What changed:**
- `context/project.md` filled in
- `context/user.md` filled in
- `context/constraints.md` filled in
- `documentation/decisions/0002-api-based-automation-on-github-actions.md` (first real decision)
- `verification/definition-of-done.md` set for first feature

---

## How feedback feeds into the upstream files

When you log a learning here, also ask: **does this change something upstream?**

| Learning type | Update |
| --- | --- |
| *"I keep correcting the AI about X"* | Add a rule to `../rules/build-rules.md` |
| *"The user is actually more like Y, not X"* | Correct `../context/user.md` |
| *"We chose to do A over B for these reasons"* | New decision record in `../documentation/decisions/` |
| *"We have to change scope because of Z"* | Update `../context/project.md` |
| *"This approach didn't work; we're trying a different one"* | New decision record + update the active plan in `../documentation/plans/` |

The log is the history. The upstream files are the living memory.

---

## Premium-tier feedback patterns

The Build Kit's feedback log is manual and human-driven. **AI Code that Works Premium** adds:

- **Sentry breadcrumbs** — every catch block captures to Sentry with structured context; the breadcrumb trail IS feedback
- **PostHog session replay** — actual user behavior fed back into the build cycle
- **Audit events** — every state-changing operation logged for retrospective analysis
- **AI review loops** — Codex + Claude review every PR with findings that feed back into the rules
- **Drift checks** — automated detection when the project drifts from its rules; the drift report IS feedback

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Phase 5 file — Feedback Loops. See `README.md` in this folder for the framing.*
