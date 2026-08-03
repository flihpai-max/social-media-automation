# How to Add a New Rule

_The format and process for adding rules as you discover patterns. Rules compound — a project with good rules is dramatically easier to work in than one without._

---

## When to add a rule

When you notice a pattern that should apply to **all future work** in this project. The signal: **you find yourself giving the same correction more than twice.**

Examples:

- You keep correcting the AI about commit message style → write a rule.
- You keep telling the AI to use a specific library → write a rule.
- You keep saying *"don't do X"* → write a rule.

If a correction recurs, it's not a quirk — it's a pattern. Patterns belong in `build-rules.md`.

## When NOT to add a rule

- **One-time decisions** → write a decision record (lives in `../documentation/decisions/`), not a rule.
- **Things that only apply to one specific feature** → put the constraint in the feature's plan in `../documentation/plans/`.
- **Things you might change tomorrow** → not stable enough to be a rule.

Rules are **always-true**. If you're not sure something will always be true, it's a decision or a plan, not a rule.

## The format

Each rule in `build-rules.md` has the same shape:

```markdown
### N. The rule statement (short, imperative)

One or two sentences explaining *why* this rule exists. The *why* is the load-bearing part — without it, future-you doesn't know whether to bend the rule when it gets in the way.
```

**Examples of good rule statements:**

- *"Be specific about names."*
- *"One canonical way."*
- *"Verify the output, not the input."*

**Examples of bad rule statements:**

- *"Write good code."* — too vague to act on
- *"Don't do bad things."* — same
- *"Use kebab-case for filenames except when..."* — exceptions = it's not a rule, it's a process

## The process

1. **Notice the pattern.** You corrected the AI twice on the same thing.
2. **Phrase it.** Write the rule in one short imperative sentence.
3. **Justify it.** Write one or two sentences on *why* the rule exists.
4. **Add it to `build-rules.md`** under the project-specific rules section, with the next available number.
5. **Tell the AI.** In your next session, mention the new rule so it gets read.

## Bending a rule

Rules can bend — but never silently. If a rule needs to bend in a specific case:

1. **Write a decision record** (`../documentation/decisions/NNNN-bending-rule-X.md`).
2. **Explain why the rule doesn't apply here.**
3. **Note whether this changes the rule going forward** or is a one-time exception.

If a rule bends three or more times, the rule needs to change. Either tighten it, narrow its scope, or remove it.

## Pruning rules

Rules can also be removed. If a rule:

- Has never been useful → remove it.
- Has been bent more than it's been followed → remove or rewrite it.
- Was about a constraint that no longer applies → remove it.

Stale rules are worse than no rules — they make the AI distrust the whole rules file.

## The Premium-tier discipline

The Build Kit teaches the *pattern* of rules. **AI Code that Works Premium** teaches:

- Enforceable rules (CI/lint-level enforcement, not just convention)
- Rule precedence and conflict resolution across nested folders
- The full library of production-grade rules with the incident history that produced each one
- How rules get refactored when patterns shift

See the parent Build Kit's `WHAT-COMES-NEXT.md`.

---

*Phase 2 file — Rules. See `README.md` in this folder for the framing.*
