# Razor Profiles — decisions

Dated record of prior decisions and still-open calls, compiled Monday, November 16, 2026 (America/New_York). Times below are in that zone unless a source gives another zone.

Sources used: shared memory (profile and journal entries), the files in this folder, the dossier branch `cursor/add-standing-dossier-b3f6` at `116f935` in `kingpoststudio/razor-profiles`, and Kit's briefings to Stuart on Monday, November 16, 2026. This note does not invent facts that those sources do not support.

## Locked or already acted on

### 2026-10-22 — Dossier compiled
Kit compiled the Walter Lentfert / Razor Profiles dossier from public sources, LinkedIn, Asana, and Stuart's files. The research was read-only at the time. The canonical text is [dossier.md](dossier.md).
- Source: dossier preamble; memory profile, 2026-10-22.

### 2026-10-22 — Rio's first written directions
Rio wrote [design-consideration.md](design-consideration.md): Direction A, "Cross-Section", and Direction B, "One Surface". Both were meant to be a step up from the current under-construction site, evolve the existing logo rather than replace it, and stay coherent with Stuart's other work. Rio leaned toward B for the home and hero, and left the lead pick to Stuart.
- Source: [design-consideration.md](design-consideration.md).

### 2026-11-07 area — Round 1 comps
Rio produced hero and module comps for Direction A (warm paper, line-art Möbius) and Direction B (dark mode), plus a light-mode / light-versus-dark exploration, into `/workspace/razor-profiles/`. Those files are now under [comps/](comps/) and are listed in [design-proposals.md](design-proposals.md).
- Source: memory profile, 2026-11-13; files dated November 7, 2026 in the box folder.

### 2026-11-11, 2:05–2:08 PM — Dossier placed; rejected alias removed
The company name is **Razor Profiles** only. Stuart corrected the record on November 11: do not call it "Raise Your Profiles". That alias must not appear.

The dossier was placed as standing context in the Razor Profiles Cursor Project (`bc-7c175d60-bd5f-4d64-a5e1-75d549bf8979`) and pushed to `kingpoststudio/razor-profiles` on branch `cursor/add-standing-dossier-b3f6` as `docs/dossier.md` (commit `681c27eb`), with a short pointer in `docs/README.md`. The same day, the rejected alias was removed in commit `116f935`. No pull request was opened. Nothing was merged or deployed. Theme work in that project was to follow the 2024 brand and the dossier. Extra HubSpot work was limited to content staging, never production credentials.
- Source: memory journal, 2026-11-11, 2:05 PM, 2:07 PM, and 2:08 PM; memory profile, 2026-11-11.

### 2026-11-12 — Direction A push asked for, then cancelled
Stuart asked for Direction A to be pushed to the Razor Profiles repo. Kit later reported that Stuart cancelled that push, and nothing went into `kingpoststudio/razor-profiles`. Rio's round 2 README, written the same day, also says nothing was pushed, committed, or published, and that the round 1 files were left untouched.
- Source: memory profile, 2026-11-13 (records the ask); Kit briefing to Stuart, Monday, November 16, 2026 (reports the cancellation and that nothing was committed); [round-2/README.md](round-2/README.md).

### 2026-11-12 — Round 2 comps
Rio produced two further visual-identity directions, "Clean Cut" and "Live Build", with heroes, brand boards, and module sheets. Files are under [round-2/](round-2/).
- Source: [round-2/README.md](round-2/README.md), dated Thursday, November 12, 2026.

### 2026-11-16, 10:13 AM — This branch is the source of truth
Stuart, by voice, made branch `cursor/kingpost-studio-site-9887` in `kingpoststudio/kingpost.studio` (King Post Studio Cursor Project, `bc-6c491388-dd99-57da-bfb2-c787b7b3c6f5`) the single source of truth for the Razor Profiles dossier, all prior decisions, and Rio's design proposals. Commits go to that existing branch only. Do not merge, do not open or merge pull requests into `master`, do not deploy, and do not touch Titan or Stuart's local checkout. Going forward, Stuart's requests are to be worked from the King Post Studio project, not 3D Studio.
- Source: Stuart, voice, Monday, November 16, 2026, 10:13 AM (America/New_York).

## Standing facts (not new decisions)

- The live site is an under-construction page on HubSpot portal 46015340. `www` returns 404.
- Walter's Asana project is "RazorProfiles.com", gid `1209525694848848`.
- There is a group chat named "Razor Profiles" (`8633996b-a0a5-46ac-8e17-27f105cf1aea`).
- Stuart's early Astro scaffold is at `C:\Users\stu\Code\razor-profiles` on Titan and is not hooked up to GitHub.
- Stuart's Razor Profiles work email is `stuart.grant@razorprofiles.com` (Google/Gmail, not Outlook).
- In the Razor / KPS working relationship: Stuart owns design and programming; Matt provides content that must fit Stuart's designs; Walter is account manager and data (HubDB, catalog, client), not layout or design.
- Walter prefers Google Fonts for licensing (October 5, 2026 thread, as recorded in the design consideration).
- On March 3, 2025, Walter and Stuart both preferred "Macro/Micro 3D Möbius Framing" over "Gradient Immersion" and "Light Refraction" (Zoom summary in [content/](content/)).
- A 2025 redesign pass already happened: Laura Pursel, round 1 (February–April 2025, ended April 30); Maria Lindberg Bogdan (UP) did a round 2 Figma; Jim Nouvakis built HiArc-based modules; Amber Ortiz did an interactive concept. Jim reported "RazorProfiles Done" on November 12, 2025, but the "Final website to go live" milestone (due August 1, 2025) was still open as of the October 22 dossier. Those are prior, non-Rio directions.
- Source: memory profile, 2026-10-22; [dossier.md](dossier.md); [design-consideration.md](design-consideration.md); content files in this folder.

## Preferred, but not locked

### Direction B was preferred, and is still unpicked
As of November 13, 2026, shared memory recorded that Stuart preferred Direction B, "One Surface" (dark mode). Kit repeated that preference to Stuart on the morning of November 16 and listed "lock in Direction B" as an open call. Later that morning, at 10:13 AM, Stuart asked for all of Rio's Razor Profiles design proposals to be placed in front of him so he can finally pick a direction. Treat B as a recorded preference, not a locked choice.
- Source: memory profile, 2026-11-13; Kit briefing to Stuart, November 16, 2026; Stuart, voice, November 16, 2026, 10:13 AM.

## Still open

- Pick a lead visual direction from the proposals in [design-proposals.md](design-proposals.md).
- Choose a build path: a HubSpot theme on portal 46015340, or Stuart's Astro scaffold on Titan.
- Whether to open or merge a pull request for the older dossier branch `cursor/add-standing-dossier-b3f6` in `kingpoststudio/razor-profiles`. That branch still has no pull request. This King Post Studio branch is now the source of truth.
- Still-needed inputs listed at the end of [design-consideration.md](design-consideration.md) and in [round-2/README.md](round-2/README.md): an export of the copy Google Sheet; Walter's sign-off on which clients and testimonials can be named; a photo or video of Walter, or permission to request one; whether his cell can appear on the site; Razor's own HubSpot partner tier and any real case metrics; access to Maria's and Amber's Figma files. Round 2 comps use placeholders for generated images, Walter's portrait, metrics, and some copy.
- Nothing goes live until Stuart says so.
