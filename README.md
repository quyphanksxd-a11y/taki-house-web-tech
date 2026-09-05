# TAKI HOUSE – WEB TECH Bootstrap

This package initializes Codex as the technical execution layer for the TAKI HOUSE Website Management room.

## Recommended Codex project name

TAKI HOUSE – WEB TECH

## Installation

1. Create/open a Codex project or repository for TAKI HOUSE website technical work.
2. Copy `AGENTS.md` to the repository/project root.
3. Copy the `skills/` folder into the project.
4. Keep `templates/` available for every WEB-xxx task.
5. Do not connect production write access during initial setup.
6. Start with the prompt in `START_PROMPT.md`.
7. First run `WEB-BOOT-001` in read-only mode.

## Initial permission model

Safe:
- Public web read
- Repository read
- Local command execution
- Local branch/worktree write
- Approved staging read/write

Not initially granted:
- Production SSH write
- Production SFTP write
- WP admin write
- DNS/CDN/WAF write
- Database write
- Tracking changes

## Suggested lifecycle

Work/00 identifies or approves a task
→ task is recorded using `templates/WEB-TASK.md`
→ Codex executes technical analysis
→ Codex returns evidence and patch/test plan
→ staging validation
→ Quý approval
→ production deployment
→ post-change verification
→ changelog update

## First objective

Do not fix anything initially. Establish:
- project instructions loaded
- website reachable
- public technical baseline
- repository/staging access status
- explicit missing permissions
- safe rollback expectations
