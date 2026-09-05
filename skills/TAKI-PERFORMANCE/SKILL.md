---
name: taki-performance
description: Diagnose TAKI HOUSE performance and UX with separate lab and field evidence.
---

# Skill: TAKI-PERFORMANCE

Purpose: diagnose speed, Core Web Vitals lab signals, UX and conversion-related technical issues.

## Check
- mobile and desktop separately
- LCP-related assets
- CLS sources
- INP/TBT proxies where available
- image dimensions/formats
- lazy loading
- fonts
- render-blocking CSS/JS
- cache/CDN headers where observable
- responsive layout
- navigation
- CTA visibility
- phone/Zalo controls
- forms without submission

## Rules
- Record tool/source and timestamp
- Separate field data from lab data
- Do not claim public Lighthouse equals real-user CWV
- Do not purge production cache or alter CDN without approval
- Any patch must have before/after measurement

## Project operating rules
Read references/AGENTS.md before execution. Keep roles 00–06; Codex is their shared technical executor. Production approval must be scoped to this task, never inferred from a Sheet status alone.
