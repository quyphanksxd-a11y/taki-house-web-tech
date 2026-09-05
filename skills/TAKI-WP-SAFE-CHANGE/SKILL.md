---
name: taki-wp-safe-change
description: Prepare reversible WordPress changes for TAKI HOUSE using local or approved staging with explicit production approval.
---

# Skill: TAKI-WP-SAFE-CHANGE

Purpose: prepare and validate the smallest safe WordPress change.

## Pre-change gate
- confirm issue
- identify exact component
- confirm backup/rollback
- prefer staging/local
- inspect child theme first
- do not edit WP core or parent theme directly

## Execution
1. Create isolated change.
2. Record exact files/config changed.
3. Run syntax/lint/tests available.
4. Test relevant pages on mobile and desktop.
5. Check console.
6. Check SEO metadata if template output is affected.
7. Check CTA/forms without generating fake leads.
8. Compare before/after.

## Production
Stop at READY_FOR_APPROVAL unless explicit production approval is present.

## Project rules
Read references/AGENTS.md before execution. Keep roles 00–06; Codex is their shared technical executor. Production approval must be scoped to this task, never inferred from a Sheet status alone.
