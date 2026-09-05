# WEB-BOOT-001 – Codex Technical Baseline

## Task / Status
WEB-BOOT-001; baseline executed, follow-up needed for sitemap.xml and missing source/staging access. Sheet status: Theo dõi.

## Environment
Public HTTP via Python urllib in Work terminal, no browser viewport, 2026-09-05 13:48–13:50 UTC / 20:48–20:50 ICT. Five direct URL requests, plus public web-tool cross-checks. No forms or logins.

## Facts observed / Evidence
- http://takihouse.vn/: 301, Location https://takihouse.vn/.
- https://takihouse.vn/: 200; canonical https://takihouse.vn/; meta robots follow,index,max-snippet:-1,max-video-preview:-1,max-image-preview:large.
- robots.txt: 200, general Allow: /; declares https://takihouse.vn/sitemap.xml; includes bot-specific restrictions. Not a blanket Googlebot block.
- sitemap_index.xml: 200; valid sitemapindex XML with post/page/blocks/featured_item sitemap URLs (not fetched). X-Robots-Tag noindex applies to this XML response; it does not prove homepage noindex.
- sitemap.xml: 403; body error code: 1010 for this client. No 5xx among the five directly tested URLs.
- Headers of first four responses report Server: cloudflare; this does not establish admin access or configuration.
- Python/git/curl/node are present. Codex CLI and Lighthouse were not found on PATH. No website source repository or staging access supplied. No production login attempted.
- Public web tool returned homepage content but failed for robots/sitemaps; terminal evidence above is more specific. No mobile/desktop CWV measured in this baseline.

Raw evidence: evidence/20260905T134845Z/baseline.json, numbered response bodies with SHA256 in JSON, evidence/sitemap-discovered.json and .body.

## Diagnosis
No proven site-wide outage or blanket noindex. Hypothesis: client-specific protection affects sitemap.xml. Actual cause and Googlebot access are NOT VERIFIED. The mismatch between declared sitemap URL and fetch outcome needs corroboration.

## Confidence
High for measured response and extracted tags in this client/time; low for cause or impact on Google indexing.

## Proposed change
None to website. Verify sitemap.xml from an independent client and read-only CDN request logs or GSC Sitemaps before proposing a configuration change.

## Files/config affected
Only local bootstrap files, four personal skills and four appended Sheet rows. No website changes.

## Risk
Limited observation cannot establish all URLs, all clients, SSL expiry, full security, lead delivery, indexing or CWV. Medium follow-up priority, not an emergency declaration.

## Backup / rollback
Website: not applicable (no changes). Remove task-specific local additions and appended Sheet rows only if rollback requested. Do not restore website backup.

## Tests
Baseline script executed. HTMLParser extracted canonical/robots; ElementTree parsed sitemap index. Four personal skills passed validators and were verified after installation. Sheet values/validation/format metadata re-read after writes. No browser visual verification; text-fit unverified.

## Before / after
Previously available report lacked directly verified HTTP/robots/canonical/sitemap. This run supplies that evidence. No performance or website before/after change comparison applies.

## Approval gate
No production approval granted. READ-ONLY technical work READY for public/local checks; source-specific tasks blocked until source provided. Staging changes NOT READY: no isolated staging/access or verified backup. Production changes NOT READY: no approved scope, test, backup/rollback or deployment connection.
