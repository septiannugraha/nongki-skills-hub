---
name: vault-notetaking
description: Capture durable learnings, research findings, and session outcomes into an Obsidian second brain. Configure the vault location with the VAULT_DIR environment variable. Use after research tasks, debugging sessions that produced a real insight, architecture decisions, tool/library evaluations, or whenever the user says "note this", "add to the vault", "second brain", or "write this up".
license: MIT
tags: [obsidian, note-taking, second-brain, knowledge-management, para]
---

# Vault Note-Taking

Write durable, re-readable notes into an **Obsidian** vault configured via the `VAULT_DIR` environment variable:

```bash
export VAULT_DIR="$HOME/code/writing_discussion/ObsidianVault"   # your vault path
```

Notes written here are meant to be re-read months later by someone who has
forgotten all the context.

## Setup check

Before first use, confirm the vault exists:

```bash
test -d "$VAULT_DIR" && echo "vault: $VAULT_DIR" || echo "VAULT_DIR not set or missing"
```

If unset, ask the user where their vault lives and suggest exporting `VAULT_DIR` in their shell profile. If the folder layout below doesn't match (no PARA-style folders), adapt to the vault's actual structure — read a few existing notes first and follow what's there.

## When to write a note

Write one when a session produced **durable, transferable knowledge**:

- Research into a codebase, library, protocol, or paper
- A non-obvious debugging root cause (especially version-related)
- An architecture or tooling decision, plus the reasoning behind it
- A tool/library evaluation or comparison
- A workflow that took effort to figure out and will be reused

Do **not** write a note for: trivial edits, routine commands, or anything the
user can trivially rediscover. Noise degrades the vault.

## Where notes go

Assuming the standard PARA-style layout (adapt if the vault differs):

| Folder | Use for |
|---|---|
| `00-Inbox/` | Quick unsorted captures |
| `01-Projects/` | Active, goal-bound work with a deadline |
| `02-Areas/` | Ongoing responsibilities, no end date |
| `03-Resources/` | **Durable reference material — most research notes land here** |
| `04-Archive/` | Inactive/completed |
| `05-Sessions/` | Session logs and digests, named `YYYY-MM-DD <Title>.md` |
| `06-Musings/` | Half-formed thinking |

## House conventions

Match the existing notes — read a neighbouring file before writing.

- Title as `# H1` matching the filename
- `**Tags:** #tag1 #tag2` near the top; reuse the vault's existing tag vocabulary
- `**Created:** YYYY-MM-DD`
- For research notes, cite the **source and exact commit/version**
- Cite specific `file.py:123` line numbers so claims are checkable later
- Cross-link with `[[Wiki Links]]` and close with a `## Related` section
- Session notes: `05-Sessions/YYYY-MM-DD <Title>.md`

## What makes a note worth keeping

1. **Lead with the verdict.** State the conclusion before the evidence. Future-you
   wants the answer, not the journey.
2. **Record what was ruled out**, not just what was found. "X is not the mechanism,
   despite the name" prevents re-investigating the same dead end.
3. **Cite precisely** — file paths, line numbers, commit hashes, version numbers.
4. **Separate fact from inference.** Mark speculation as speculation.
5. **Add a takeaways section** — what would we do differently next time.

## Critical: never persist unvalidated findings

- **Do not write "tool X is broken" / "Y doesn't work"** as a durable claim. These
  harden into self-imposed constraints that get cited for months after the
  underlying problem was fixed. Scope it instead: *"as of v1.2 on 2026-08-07, X
  failed with <error>"*.
- **Do not write up an unresolved debugging session as a working procedure.** If the
  session ended without a confirmed fix, either write nothing or label it explicitly
  as an **open question**. An untested sequence of failed attempts presented as
  guidance will be trusted and repeated.
- Persist **confirmed working** paths. Everything else gets a date and a caveat.

## Workflow

1. Resolve the vault root from `$VAULT_DIR`; if unset, ask the user
2. Check whether a note on this topic already exists — prefer **updating** over
   creating a near-duplicate
3. Read a neighbouring note in the target folder to match tone and structure
4. Write the note
5. Add `[[links]]` to related notes, and where natural, link back from them
6. Tell the user the path you wrote to and give a one-line summary

Never write secrets, credentials, tokens, or API keys into the vault — vaults are often synced.
