# Minimum Access Plan

## Phase 1 – Read-only
Required:
- Public website access
- Repository read access if available
- Local terminal/tool execution

Optional:
- GSC read
- GA4 read
- hosting logs read
- staging read

## Phase 2 – Staging
Required before changes:
- staging write access
- staging database isolated from production where feasible
- backup/restore procedure documented
- source control branch/worktree
- rollback path

## Phase 3 – Production
Only after explicit approval:
- least-privilege deployment method
- no shared administrator credentials in chat
- no secrets committed to repository
- audit trail/changelog
