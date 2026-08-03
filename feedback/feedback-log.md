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

## [DATE] — Started the project

**What we tried:** Provisioned the project using the AI Code that Works Build Kit. Filled in initial context, reviewed starter rules, wrote the first decision record (choice of the Build Kit itself).

**What happened:** Provisioning took [FILL IN: e.g., 45 min]. The hardest part was [FILL IN: e.g., being specific about the user in `context/user.md` — defaulted too vague at first].

**What we learned:** [FILL IN: the durable insight from the provisioning experience. E.g., "Specificity in user context isn't optional — vague users → vague AI choices."]

**What changed:**
- `context/project.md` filled in
- `context/user.md` filled in
- `context/constraints.md` filled in
- `documentation/decisions/0002-[NAME].md` (first real decision)
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
