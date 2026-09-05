---
name: taki-web-audit
description: Run read-only technical health checks for TAKI HOUSE website WEB tasks.
---

# Skill: TAKI-WEB-AUDIT

Purpose: run a low-impact technical health audit.

## Checks
- HTTP/HTTPS
- redirect behavior
- robots.txt
- sitemap
- meta robots
- canonical
- obvious 404/5xx
- visible schema
- basic security headers when observable
- obvious mixed content/browser console problems when tooling permits

## Rules
- Read-only
- No aggressive crawling
- No form submissions
- Record URL, timestamp, environment and confidence
- Distinguish absence of evidence from confirmed failure

## Output
Use AGENTS.md reporting format.

## Project rules
Read references/AGENTS.md before execution. Keep roles 00–06; Codex is their shared technical executor. Production approval must be scoped to this task, never inferred from a Sheet status alone.
