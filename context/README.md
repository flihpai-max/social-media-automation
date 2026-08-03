# Context — Phase 1

_What we know about what we're building, who it's for, and what constraints apply. The foundation underneath every decision._

---

## Why Context comes first

Most builds go wrong here. The builder has an idea, but the AI doesn't have enough context to make good choices — so it makes choices that don't line up with the rest of the project, or it asks the same questions over and over because the answers never got written down.

**The Context phase fixes that.** Before any code or content gets created, the project knows:

- **What** is being built
- **Who** it's for
- **What constraints** apply (time, budget, tech, what we won't compromise on)

## What's in this folder

Three files, all filled in during provisioning:

| File | What it captures |
| --- | --- |
| `project.md` | What we're building, why it matters, the shape of "done," what's NOT in scope |
| `user.md` | Who specifically we're building for (be precise — not "small business owners") |
| `constraints.md` | Time, budget, technical constraints, what we will and won't compromise on |

## When to update context

- **Project scope changes** — update `project.md`. Add to it, don't replace. Note the date and what changed.
- **New information about the user** — update `user.md`. Especially when assumptions turn out to be wrong.
- **Constraints shift** — update `constraints.md`. New deadline, new budget, new technical constraint.

Context is **living**. Stale context produces bad AI work.

## How the AI uses context

When you ask the AI to do anything substantive, it should read the relevant context files first. If you notice the AI making choices that contradict the context, that's a signal it didn't read them — say *"please re-read the context files first."*

For the Premium-tier discipline on context routing (multi-file routers, task-type-specific reading lists, auto-loaded session-start context): see **AI Code that Works Premium**.

---

*Phase 1 of the AI Code that Works method. Learn the full method at [https://www.skool.com/aicodethatworks](https://www.skool.com/aicodethatworks).*
