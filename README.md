# nongki-skills-hub

Curated [Claude Code](https://claude.com/product/claude-code) skills — versioned, reusable, and warung-tested.

This repo is the **source of truth** for the skills installed via `~/.claude/skills/` (symlinked). Edit here, take effect everywhere.

## Skills

| Skill | Purpose | Tags |
|---|---|---|
| [changes-committing](skills/changes-committing/) | Secure git commits: credential scanning, file filtering, conventional commit messages, no secrets ever land in history | `git` `security` `conventional-commits` |
| [pdf-comprehension](skills/pdf-comprehension/) | Deep PDF analysis: extracts pages as images, reads them visually, produces structured markdown summaries with visual highlights | `pdf` `analysis` `document` |
| [study-guide-writing](skills/study-guide-writing/) | Manning/No Starch Press-style study guides from source materials — LaTeX to PDF + EPUB, with note/tip/warning boxes and war stories | `latex` `pdf` `epub` `education` |

## Install

### From this repo (fresh machine / another environment)

```bash
git clone git@github.com:septiannugraha/nongki-skills-hub.git ~/code/nongki-skills-hub

# Symlink every skill into Claude Code's skills directory
mkdir -p ~/.claude/skills
for skill in ~/code/nongki-skills-hub/skills/*/; do
  ln -sfn "$skill" ~/.claude/skills/"$(basename "$skill")"
done
```

Or cherry-pick only the skills you want:

```bash
ln -sfn ~/code/nongki-skills-hub/skills/changes-committing ~/.claude/skills/changes-committing
```

### Adding a new skill

1. `mkdir skills/<skill-name> && $EDITOR skills/<skill-name>/SKILL.md`
2. Follow the SKILL.md format: YAML frontmatter (`name`, `description`, `tags`), then the instructions.
3. `ln -sfn ~/code/nongki-skills-hub/skills/<skill-name> ~/.claude/skills/<skill-name>`
4. Commit and push. New machine? Run the install loop above and you're synced.

## Structure

```
nongki-skills-hub/
├── README.md
├── .gitignore
└── skills/
    ├── changes-committing/
    │   └── SKILL.md
    ├── pdf-comprehension/
    │   └── SKILL.md
    └── study-guide-writing/
        └── SKILL.md
```

## Curation policy

Skills in this hub are curated — battle-tested, generic enough to be useful across projects, and documented. Skills that are personal, machine-specific, or "creative" stay in `~/.claude/skills/` directly, outside this repo.

## License

Personal toolkit — no license for now. Flip to private-only or add one later if this ever goes public.
