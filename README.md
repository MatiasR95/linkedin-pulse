# Pulse 📊 — remote control for the LinkedIn content engine

A minimal, installable iPhone web app (PWA) that monitors and steers the automated
LinkedIn Writer system. **This repo contains only the app shell — no posts, no data,
no secrets.** All content lives in a private repo the app reads with a personal token
you keep on your phone.

## Install on iPhone (one time)
1. Open the GitHub Pages URL in **Safari**.
2. Share button → **Add to Home Screen** → "Pulse".
3. Open Pulse → Settings → paste a GitHub fine-grained token
   (repo access: only the private content repo; permission: Contents → Read & write).

## What it does
- 📋 **Queue** — upcoming posts (date, category, hashtags, media, EN+ES body), recently published.
- ✏️ **Edit** — change a post's text right on the phone; it commits to the repo, and the
  cloud publisher uses the edited version automatically.
- ⏸ **Hold / release** — block a post from publishing with one tap.
- 📊 **Metrics** — weekly quick-log of LinkedIn profile numbers + trends + suggested actions.
- ✍️ **Compose** — braindump an idea (EN or ES); Claude drafts it on the next cloud run.
- 📰 **News** — daily trending Data/BI/AI topics scouted by a cloud routine.

The engine itself runs fully in the cloud — the app is just the window. Skipping the app
for a week changes nothing.
