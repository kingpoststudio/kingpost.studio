# Razor Profiles: design consideration for the website redesign
Rio, for Stuart Grant. Thu Oct 22, 2026 (ET). This is research and synthesis only. No production code was written, nothing was changed, and no one was contacted.
Stuart's steer: what is dated on today's site is not a constraint. Both directions should be a real step up and clearly different from today, while evolving the existing logo (not replacing it) and staying coherent with Stuart's other work.

---

## 1. Kit's dossier: what we actually know
Sources: Kit's dossier `/workspace/razor-profiles/dossier.md` (also the Page "Razor Profiles & Walter Lentfert — dossier"), Kit's transcript, shared memory, and the files in `/workspace/razor-profiles/content/`.

**Company.** Razor Profiles LLC is in Wilmington, NC, and was founded in January 2008 by Walter Lentfert (Founder & President). It does HubSpot CMS and web work, CRM implementation and migration, marketing automation, ABM, e-commerce and integrations, with a focus on life sciences, med device, pharma and biotech. It runs as a networked team on @razorprofiles.com: Walter, Stuart Grant, Charlotte Wilkinson and Matt Wilkinson. LinkedIn lists one employee. The HubSpot Solutions Directory listing (seen only as a search snippet) says remote, English and Dutch, $5k+ budgets, NA/EMEA/SA, and "12 yrs" of HubSpot implementation.

**Walter.** Dutch-born and based in Wilmington. He has a biochemical engineering degree and previously worked at GE Healthcare Life Sciences (NL, SE, US), finishing as Director Commercial Operations. Since 2011 he has been at UP THERE, EVERYWHERE (a HubSpot Platinum partner) as "Head of HubSpot US" / Director of IT & Digital Implementation. He co-founded SAMPS / ACP-LS and claims "over 30 years" of experience. His signature block gives his cell as 732-299-0067. He prefers Google Fonts for licensing (Oct 5, 2026 thread).

**Stuart's role.** Stuart (King Post Studio) does HubSpot CMS engineering under the Razor banner. Walter brings in the clients (Ionetix, BioCat, Tosoh, IQVIA/CRL, Inotiv; Strivenn is a partner) and assigns the work in Asana. Razor pays KPS as a contractor, per the 2025 1099-NEC.

**Site status.** razorprofiles.com is a one-page "under construction" page on HubSpot (portal 46015340). www returns 404. There is a 2025 redesign:
- Laura Pursel did round 1 (Feb to Apr 2025). It ended on Apr 30.
- Maria Lindberg Bogdan (UP) did the round 2 Figma, Jim Nouvakis built HiArc-based modules, and Amber Ortiz did an interactive concept.
- Jim reported "RazorProfiles Done" on Nov 12, 2025, but the "Final website to go live" milestone (due Aug 1, 2025) is still open.
- On Oct 22, 2026 Kit restructured the repo kingpoststudio/razor-profiles into the Ionetix layout as draft PR #2. Nothing was deployed.

**Prior direction (real, from sources).**
- Brand guidelines 2024: "Razor sharp, but seamlessly fluid." The Möbius stands for integrated services. Philosopher for headings, Assistant for body.
- Mar 3, 2025 Zoom: Walter and Stuart both preferred **Macro/Micro 3D Möbius Framing** over Gradient Immersion and Light Refraction. They wanted animation to support the message, not decorate, plus "a sentence of intent for every page", full bleeds over captured images, a balance between showing capability and avoiding a "kitchen sink", and SVG/hardware-accelerated motion. Stuart wanted the designs to feed a white-label component library.
- Walter's Apr 2025 brief:
  - a sticky mega menu on desktop and mobile
  - a condensed, plain footer
  - a hero that is a 10–15 s Möbius story with the Möbius as the transition
  - the Möbius drawn thinner ("too thick")
  - likes the Alt 3 three-block layout and wants its interactivity
  - a full-width CTA with "all registers open"
  - WCAG 2.2 contrast as a recurring concern
  - his words: "a good example and representation of what we can build for them, fresh, interactive, challenging"
- Admired references (Feb 11, 2025): redantler.com and join9am.com.
- Jul 2025: Stuart told Amber to push the "razor sharp" motif. Light and dark versions were planned.
- Positioning (GET/TO/BY/BECAUSE): "Razor Profiles provides turn key solutions that deliver Razor Sharp actionable contact profiles."
- Sitemap (FlowMapp, 22 pages): Main, About (with an UP block), Services (Digital Strategy/ABM, Website Development, Marketing Campaigns, CRM Implementation/Migration, Bespoke Process Development), HubSpot Partner, Partnerships (Strivenn), Life Sciences/Med Device, Marketing Agencies, Other Experiences, Contact, Blog (after launch), legal pages.

**Real proof on file.** Two client testimonials (Jun 27, 2025) naming 9amHealth, Psomagen, Blip and Kean, with "expecting 5 more". Stuart also had the idea (Aug 16, 2026) of building case studies and a white paper from Playwright screen grabs.

**Gaps (flagged, not filled).**
- The page copy is in a private Google Sheet (401). It needs Stuart or Walter to export it.
- No case-study copy, **no metrics**, and no team bios exist anywhere.
- **No photo or video of Walter** was found.
- Which clients can be named publicly is unknown, and Ionetix is under NDA. The testimonials are unattributed (no names or titles).
- HubSpot partner tier for Razor itself is unconfirmed. UP is Platinum, not Razor.
- The Figma files (Maria, Amber, Laura) and the Slack .fig wireframes were not opened.
- "Deep Blue" is given as both #20386C and #003271 in the guidelines (see the logo notes; the mark actually uses #003271).
- **Razor Profiles team agent:** none turned up in memory, Kit's transcript or the box. Kit holds the dossier.

---

## 2. The existing mark (downloaded from razorprofiles.com/hubfs)
Files are in `/workspace/razor-profiles/logo/`: `rp-left-stacked-dark.svg` (live header), `rp-left-stacked-light.svg`, `rp-left-dark.svg`, `rp-left-light.svg`, `rp-middle-stacked-dark.svg`, `rp-logo.png` (379², symbol), `socialmedia-wordmark.png` (og:image), plus renders (`*-render.png`) and the extracted symbol raster (`*-symbol-raster.png`).

- **Symbol:** a Möbius-style closed loop, a slightly tilted ellipse made of three overlapping swoosh bands. The band is thick at the bottom-left and tapers toward the top-right, where a separate lobe overlaps. The guidelines describe three swooshes for three services.
- **Gradient (sampled):** deep navy #003170/#003271 (bottom), mid blue #0057A8 (left), cyan #0AC0F1 (top), mint #7DDD81 (top-right), chartreuse #BDBA1C to olive (right lobe), then back to navy #0F3965. These stops are **not** the published palette (#20386C, #28ABE2, #D6DF27).
- **Construction flaw:** in every SVG the gradient symbol is a **base64 PNG (≈88–138 px) clipped by a vector path**. Only the wordmark is true vector. The symbol goes soft at large sizes and can't be animated or recolored.
- **Wordmark:** "RAZOR / PROFILES" in all caps, in Philosopher (a flared, calligraphic humanist with tapered stems and a lively R leg), stacked or single-line. Dark #131626, light #EAEAE9.
- **Lockups:** left-aligned combination (primary), middle-stacked, and the symbol alone.
- **Palette (2024):** Midnight Black #131626, Deep Blue #20386C (guideline conflict: #003271), Matte White #EAEAE9, Sky Blue #28ABE2, Urgent Yellow #D6DF27.

---

## 3. Stuart's visual language (recurring patterns across his builds)
Sources: kingpost.studio preview and brand docs, the KPS type specimens (`/workspace/kps-type`), Ionetix `tokens.css` and comps, TrussUI 0.1.57, and Rio/Kit memory.

- **Type:** a grotesk system with one character face used sparingly.
  - KPS: Pirata One on the H1 only, with Manrope for everything else. Candidate pairings are Archivo Condensed + Archivo ("Span") or Instrument Serif + Geist ("Joinery"), with Geist Mono for labels.
  - Ionetix: Oswald display with Neuzeit Grotesk body.
  - Common to both: tracked, uppercase small labels (0.16em, 700), large light H2s, short measures (36–40rem).
- **Color:** one dark ink, one warm paper, one structural mid-tone, and **one accent used sparingly**.
  - KPS: ink #231F20, paper #EFE6E3, purple #5263A4, rust #DF584F.
  - Ionetix: ink #0B1C30, navy #1E3B5F, soft white #FAF4EE, red #C00520.
  - No soft gradients as backgrounds. Grain and dither textures are fine.
- **Grid/layout:** Swiss and neo-industrial.
  - Big generous margins (8vw pads), asymmetric two-column (mark/visual left, index right).
  - Services as a ruled index list (name plus a one-line "why"), hairline rules, HUD-style labels and L-ticks.
  - "One studio" positioning aimed at CEOs, CTOs and CMOs. Truss as alignment, not illustration.
- **Mark treatment:** the official mark is never redrawn. It is used big as a structural element (the KPS "]{" at spine scale), black or white only, and shown off with crops and scale rather than effects.
- **Imagery:** real objects over metaphor. Ionetix uses the real molecule from its own 3D model, real facility photos (MDS), dither "Batch Record" plates and glass walls. Nothing is generated where accuracy matters. No ice, glows or spotlights, and faces stay soft or turned away.
- **Motion:** restrained and purposeful. Turntables, a spin on scroll, a single hard key light. CSS/SVG first, WebGL only as a branch. Never decoration-only.
- **System thinking:** everything resolves to tokens and reusable modules (TrussUI, hs-fieldkit, the Astro + HubSpot monorepo), so the site doubles as a showcase of the build system.

---

## 4. Today's razorprofiles.com: what's dated
- It is a placeholder: logo, phone number, "under construction". No services, proof or people. www 404s.
- Positioning from 2008-era CRM language: "actionable contact profiles" and "customer profiling". It says nothing about strategy, design or development under one roof.
- The gradient is used as a full-bleed wallpaper (the social card). That reads 2018 SaaS and fights WCAG contrast, as Walter himself flagged.
- The override CSS is off-brand (#0F437F, #425B76, #1E3D60). jQuery 3.6 and a legacy v2 form are loaded. The theme dates from Jan 2025.
- The mark is rasterized and the band is heavy.
- **Strength to keep:** the Möbius idea itself (integrated services, one continuous surface) is good and ownable, and Walter has asked for it twice.

---

## 5. Two directions
Both directions assume the same rules:
- **Positioning rewrite (proposal, not sourced copy):** "Strategy, marketing, design and development: one office, one surface." The Möbius becomes literal: a single surface with no seam between disciplines, so the enterprise client never manages a hand-off. This mirrors KPS's "No handoff between shops" without copying it.
- **Capabilities:** four capabilities from the brief (Strategy, Marketing, Design, Development) shown as one ruled index, with sitemap services nested beneath them (ABM, campaigns, CRM implementation/migration, HubSpot, bespoke process).
- **Walter is the front door.** Every page ends with him, not a generic form.
- **Proof is real or absent.** No invented metrics or logos. Placeholders stay labeled until cleared.
- **Fonts are Google-only**, per Walter.
- **WCAG 2.2 AA minimum**, with every color pair below checked at build.

### Direction A: "Cross-Section"
**Idea:** a Swiss precision index. The agency's work is presented as a clean engineering cross-section, a razor-sharp *profile* in the drafting sense.

- **Type:**
  - Display and headings: **Inter Tight**, 500 at H1, 300 at large H2s.
  - Labels and specs: **Geist Mono**, uppercase, tracked 0.14em.
  - Body: **Inter** 400, 17/26.
  - **Philosopher is retired from headings** and lives only in the wordmark, plus one place: Walter's signed note.
  - This is the bigger break from today and puts Razor next to KPS/Ionetix in feel.
- **Color:** paper-first.
  - Matte White #EAEAE9 → warmed to **#F1EFEA** (base)
  - Midnight **#131626** (ink/text)
  - Deep Blue resolved to **#20386C** (structure, rules, dark sections)
  - Sky **#28ABE2** for links and focus **on dark sections only** (2.28:1 on #F1EFEA fails even the 3:1 non-text bar). On paper, links and focus rings use #20386C (9.9:1)
  - Urgent Yellow **#D6DF27** as the single sparing accent, the Ionetix-red role: one mark per screen, a highlighter on the CTA bar, never text on paper (1.27:1)
  - **The gradient appears only inside the Möbius.** It is never a background.
- **Layout and grid:**
  - 12 columns, 8vw outer pads, 1px rules in #20386C at 24% opacity.
  - Home is an asymmetric split: a large cropped Möbius in line-art at left, as the structural spine (KPS move), with H1 and the four-capability ruled index at right.
  - Case studies as **spec sheets**: client, problem, system, output, in mono-labelled rows. This was Bea's 2024 content brief done properly.
  - Sticky mega menu with four columns (one per capability) and a Walter column.
  - Condensed one-line footer.
- **Imagery:**
  - Real client work only: full-bleed Playwright captures of shipped sites (Stuart's Aug 2026 idea), set in thin device-agnostic frames. The UI "plates" use a light dither treatment so they feel like documentation, not mockups.
  - No stock, no handshakes, no glowing brains.
- **Motion:**
  - The Möbius is drawn as a single SVG stroke on load (≈1.2 s), then sits still.
  - Hovering a capability row highlights the matching section of the band.
  - Scroll reveals only. This is CSS/SVG, as Stuart specified in Mar 2025.
- **Personal warmth:**
  - Under the hero, a **signed letter from Walter**: about 80 words, his Philosopher-set signature, the year founded (2008), and Wilmington, NC.
  - "Who you'll work with" is a ruled list of real names (Walter, Stuart, Charlotte, Matt) with one-line roles. Photos only if supplied.
  - The primary CTA is "Talk to Walter", a direct calendar link, not "Contact sales".
- **Enterprise credibility:**
  - A ruled client roster in mono type (text, not logos, until marks are cleared). The candidates (BioCat, IQVIA, Inotiv, Tosoh, Ionetix under NDA; 9amHealth, Psomagen, Blip and Kean from testimonials) need sign-off.
  - The two real testimonials, attributed once names are confirmed.
  - A "Procurement" strip covering HubSpot partnership (state the actual tier once verified), WCAG 2.2, data handling, NDA-friendly process, US + EMEA, English and Dutch.
  - Life-sciences fluency, shown by the industry page.
  - Metrics **only** once real numbers exist. Until then, the spec-sheet "output" row shows shipped scope (pages, integrations, migration size) only if sourced.
- **Logo evolution:** rebuild the symbol as **true vector**, thin the band about 20–25%, and tie the gradient to the palette (see §6). Add a **single-color line version** of the Möbius for UI scale and the line-art hero. Keep Philosopher in the wordmark, with optical re-spacing only.

### Direction B: "One Surface"
**Idea:** Walter's preferred Macro/Micro Möbius, finally built. A dark, cinematic site where one rendered Möbius strip turns through the four capabilities: the 10–15 s story he asked for in 2025.

- **Type:**
  - **Philosopher stays as the display face**, but only at 72px and up, set tight (-1% tracking), never in all-caps runs longer than the wordmark. Big sizes are where its flare reads as "sharp".
  - Body and UI: **Geist** 400/500.
  - Labels and figures: **Geist Mono**.
  - This keeps brand continuity for Walter while the grotesk body gives the Stuart-family discipline.
- **Color:** dark-first, with a light mode for long reads.
  - Base **#0D0F1A** (a deepened Midnight, proposed) and Midnight **#131626** for surfaces
  - Deep Blue **#003271** as structure, decorative only (the mark's own navy; 1.5:1 on the base, so never for text or controls)
  - Text Matte White **#EAEAE9**
  - Sky **#28ABE2** for interaction (7.3:1 on the base)
  - Urgent Yellow **#D6DF27** (13.1:1 on the base) strictly as the one hot edge: the leading edge of the strip and the CTA underline
  - Light mode: #F1EFEA / #131626
- **Layout and grid:**
  - Full-bleed sections (Walter: "full bleeds look more important") on a 12-column inner grid.
  - **Hero:** the Möbius fills the right two-thirds. As you scroll, it twists face by face (Strategy → Marketing → Design → Development), and each face holds one "sentence of intent" (from the Mar 2025 Zoom). This is the horizontal-story module Walter wanted, done vertically and scroll-scrubbed.
  - Below that: the Alt 3 three-block he liked, recast as three proof blocks (Work / Walter / How we engage).
  - A full-width CTA "with all registers open": the strip passes through the frame behind "Let's talk."
- **Imagery:**
  - One hero object: the Möbius rendered from the rebuilt vector as a **solid satin-metal/glass ribbon under one hard key light**. This is the same craft language as the Ionetix glass-rod molecule, with real shadow, no glow and no neon. The brand gradient is mapped onto the ribbon's surface only.
  - Case studies get full-bleed real screen captures, graded to the dark base.
  - Optional macro crops of the strip as section dividers ("micro").
- **Motion:**
  - A 10–15 s scroll-scrubbed hero, then calm. Prefers-reduced-motion falls back to a still.
  - Pre-rendered image sequence or lightweight WebGL as a progressive enhancement over an SVG still, keeping to Stuart's hardware-acceleration rule.
  - No ambient motion elsewhere.
- **Personal warmth:**
  - **"Walter's desk"** section: a short note (or a 30–45 s video if he'll record one) beside a calm portrait, plus "Wilmington, NC · since 2008 · English & Nederlands".
  - The sticky menu always carries a small "Walter →" pill that opens his calendar.
  - Engagement page phrasing: "You'll have Walter's number." The cell is in his signature, but **put it on the site only with his OK**.
- **Enterprise credibility:**
  - A dark "Trusted by" band (text or approved monochrome logos only).
  - Testimonials set large in Philosopher, attributed once cleared.
  - Capability pages each end with a **real** case card.
  - A "How we work with enterprise teams" page: discovery → plan → build → run, plus security, accessibility, HubSpot partnership, and an NDA-first note.
  - No invented stats. Show a stat slot only if the copy Sheet or case work supplies a number.
- **Logo evolution:**
  - The rebuilt vector Möbius becomes a **3D-capable master**: true geometry, so the band can twist, take the hard light and serve as the hero.
  - The 2D lockup stays the official mark.
  - Add a dark-mode lockup where the band's navy is lifted to #20386C so it doesn't "fall away" against the background, which is Walter's exact complaint about the round 1 comps.

**My lean:** B for the home and hero, because it is what Walter has asked for twice and it is unmistakably a step up, built on A's system: ruled capability index, spec-sheet case studies, mono labels, paper-mode interiors. Stuart should pick which one leads.

---

## 6. Logo evolution: concrete notes (both directions)
1. **Re-vectorize the symbol.** Replace the embedded ≈138 px PNG with real paths: three band shapes with SVG gradients. This is a fix, not a redesign.
2. **Thin the band about 20–25%** (Walter, Apr 2025: "too thick") and even out the taper so the three swooshes read as three, with crisper overlaps (the "razor" edge).
3. **Rationalize the gradient to the palette:** #003271 → #20386C → #28ABE2 → (a short mint bridge, #7DDD81 if needed) → #D6DF27. Today's stops (#0057A8, #0AC0F1, #BDBA1C) drift off palette. Resolve the Deep Blue conflict by naming **#003271 "Mark Navy"** and **#20386C "Deep Blue"** as two documented tokens.
4. **Add variants:** a single-color line Möbius (UI and favicon), mono black #131626 / white #EAEAE9 full lockups, a dark-mode lockup with lifted navy, and a minimum size rule.
5. **Wordmark:** keep Philosopher caps and do optical re-kerning only (the R-A and O-R pairs are loose at small sizes). No new typeface in the logo.
6. **Do not:** rotate the symbol as the logo (that breaks the guideline), wrap it in effects, or use the gradient as wallpaper. Motion uses the rebuilt master and always resolves back to the official orientation.

---

## 7. Next inputs needed (not done)
- An export of the copy Google Sheet, and Walter's sign-off on which clients and testimonials can be named, with attribution.
- A photo or video of Walter (or permission to request one), plus confirmation of whether his cell can appear on the site.
- Razor's own HubSpot partner tier, and any real case metrics.
- Access to Maria's and Amber's Figma files to reconcile with round 2.
- Stuart's pick of a lead direction. After that, 1–2 comps of that direction (home hero plus one case-study spec sheet).
