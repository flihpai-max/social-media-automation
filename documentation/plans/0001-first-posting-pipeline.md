# Plan — First posting pipeline (Facebook, Instagram, LinkedIn)

**Status:** Complete — shipped 2026-08-04

---

## What this covers

Building the first feature end-to-end per `verification/definition-of-done.md`: given one image and a caption, post it to the connected Facebook Page, Instagram Business account, and LinkedIn personal profile, and prove it runs unattended via GitHub Actions.

## Steps taken (in order)

1. Facebook: Meta Developer App → Graph API Explorer → discovered the target Page needed Business Manager System User access (personal token didn't see it) → set up a System User with `pages_manage_posts` + `pages_read_engagement` → `src/facebook_post.py`.
2. Instagram: reused the Facebook System User token with added `instagram_basic` + `instagram_content_publish` scopes → decision 0003 (host images via public GitHub repo raw URL, since Instagram needs a fetchable URL, not a file upload) → `src/github_image_host.py` + `src/instagram_post.py`.
3. LinkedIn: decision 0004 (3-legged OAuth via a local callback script, since LinkedIn has no Business-Manager-style token generator) → `src/linkedin_auth.py` + `src/linkedin_post.py`.
4. Combined runner with per-platform failure isolation → `src/post_all.py`.
5. GitHub Actions wiring (manual trigger only, to avoid auto-posting the placeholder test image on a real schedule) → `.github/workflows/post.yml`.
6. Debugged and fixed two real bugs surfaced by the GitHub Actions run — see `feedback/feedback-log.md` 2026-08-04 entry (secret-paste corruption, image self-truncation bug).

## What's explicitly not in this slice

Per `context/project.md`'s "What we're NOT building": no analytics, no video, no multi-account support, no approval workflow. Per `.github/workflows/post.yml`: no recurring schedule yet — that's the next slice, once there's a real content source instead of the placeholder test image.
