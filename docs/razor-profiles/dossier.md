# Razor Profiles & Walter Lentfert — dossier

This is the shared dossier for the Razor Profiles Cursor Project. Agents in this project must read this file and treat it as standing context for theme, content, and HubSpot work.

Compiled Thursday, October 22, 2026 (ET) from public sources, LinkedIn, Asana, and Stuart's files. Placed in this project's shared context on Wednesday, November 11, 2026 (ET). The original research was read-only: nothing was sent, created, or changed at the time of compilation. Do not invent details that are not in this document. Gaps and open questions are listed below.


## Summary
- **Razor Profiles LLC** is a small web/CRM/HubSpot consultancy in Wilmington, NC, founded Jan 2008 by **Walter Lentfert** (Founder & President). It does website design and development, HubSpot CRM implementation and migration, marketing automation, e-commerce and integrations, and it specializes in life sciences, medical devices, pharma and biotech. LinkedIn lists 1 employee. In practice it works as a networked team on @razorprofiles.com addresses: Walter, Stuart Grant, Charlotte Wilkinson and Matt Wilkinson.
- **Walter Lentfert** is Dutch-born and based in Wilmington, NC. He has a biochemical engineering degree. He worked in sales/marketing and IT at GE Healthcare Life Sciences in the Netherlands, Sweden and the US, finishing as Director Commercial Operations – Functional Technology (Apr 2010–Jun 2011). Since Nov 2011 he has also been with UP THERE, EVERYWHERE (a Stockholm-based cloud agency and HubSpot Platinum partner) as Director of IT & Digital Implementation / "Head of HubSpot US". He co-founded SAMPS / ACP-LS (Sales and Marketing Professionals in Science), serving 2012–2020. His LinkedIn headline is "(Digital-) Strategy, Marketing, Sales & Execution, Marketing automation/Account-based Marketing".
- **Stuart's relationship:** Stuart (King Post Studio) delivers HubSpot CMS engineering under the Razor Profiles banner, using stuart.grant@razorprofiles.com. Walter brings in the clients (Ionetix, BioCat, Tosoh, IQVIA/CRL, Inotiv), assigns work in the razorprofiles.com Asana workspace, and fronts client communication. OneDrive has a 2025 tax folder "King Post Studio, LLC/Razor Profiles" with a 1099-NEC, so Razor pays KPS as a contractor.
- **Website status:** razorprofiles.com is a one-page "under construction" holding page on HubSpot (portal 46015340). A 2025 redesign was planned in Asana (wireframes → Figma by UP's designer → modules by Jim Nouvakis → design applied by Stuart). Most of its tasks are complete, but the "Final website to go live" milestone (due Aug 1, 2025) is still open. On Aug 21, 2026 Stuart started a fresh local scaffold (Astro + HubSpot theme).

## Sources

### 1. Titan local files (C:\Users\stu)
- `C:\Users\stu\Code\razor-profiles\`: an Astro 6 dev harness plus a HubSpot theme "RazorProfiles", dated Aug 21, 2026. It is not a git repo (no .git) and has 97 files outside node_modules.
  - README: "HubSpot CMS theme with an Astro development harness. Production is HubSpot; Astro is local only." The runtime is HTML, CSS and native custom elements (`razor-nav`, `razor-accordion`), with no framework. Build tools: Bun, Vite 7, @hubspot/cli 8, hs-fieldkit 0.2.1, vite-plugin-upload-to-hubspot.
  - Modules: Hero, CtaBanner, Accordion, globals/Header, globals/Footer. Templates: blank, landing, layouts/base.
  - `docs/component-architecture.md` describes a two-tier model: HubL/Astro markup, with custom elements only where behaviour is needed. Git is meant to be the source of truth, not Design Manager.
  - Copy is placeholder ("A sharper view of the people who matter.").
  - Design tokens (ink/paper/steel/copper, Georgia + Segoe UI) do **not** match the 2024 brand guidelines.
  - `scripts/gen-hubspot-config.js` maps develop/staging/production all to the same portal ID (from env). `.env.example` has HUBSPOT_PORTAL_ID and HUBSPOT_PAK (empty).
  - theme.json author: Stuart Grant / stu@kingpoststudio.com.
- `C:\Users\stu\OneDrive\Documents\King Post Studio\clients\Razor Profiles\`:
  - `Razor Profiles - Visual Brand Guidelines - 2024.pdf` (20 pp, InDesign, Apr 1, 2024) and a `.zip` of the same.
  - `Logos & Marks\PNG|SVG\`: rp-left / rp-middle, stacked and unstacked, in black/dark/light/white, plus social-media icon and wordmark.
  - `SVG\razor-profiles.svg`
  - `Visual Assets\`: gradient-variant1.jpg, gradientvariant2.png, herogradient.jpg
  - `redux.ai` (Illustrator) and `rp.psd`
- `C:\Users\stu\OneDrive\Documents\King Post Studio\Backup\HS Auth (Razor Profiles).pdf` is likely HubSpot credentials or 2FA material. It was **not opened**; treat it as sensitive.
- `C:\Users\stu\Code\hiarc` (github kingpoststudio/hiarc) is the HiArc theme the 2025 Razor modules were "borrowed from". It contains no "razor" references.

### Brand guidelines (2024) highlights
- Positioning: "Razor Profiles specializes in crafting sharp customer profiles through personalized user journeys… Razor sharp, but seamlessly fluid."
- Logomark: a Möbius strip of three swooshes (a nod to the original razor swoosh), representing three services. The left-aligned combination mark is primary.
- Colors: Midnight Black #131626, Deep Blue #20386C, Matte White #EAEAE9, Sky Blue #28ABE2, Urgent Yellow #D6DF27. The gradient runs from the two blues to a pop of yellow. The compliance note mentions Deep Blue #003271, which conflicts with #20386C.
- Type: Philosopher (headings) and Assistant (body), both Google Fonts. Web sample: H1 80px, H2 60px, H3 40px; body 15px in Assistant Light/Medium.

### 2. Box (/workspace) and OneDrive connector
- Box: there were no Razor-specific files before this research (hits were incidental mentions in client work). New folder `/workspace/razor-profiles/` holds this dossier, the brand PDF copy, and the homepage HTML and headers.
- OneDrive connector search for "razor" found the same client folder plus:
  - `Stuart's Notebook/Razor Profiles.one` (OneNote, Jan 15, 2024; not opened)
  - `Documents/Camp Grant/Taxes/2025/King Post Studio, LLC/Razor Profiles/1099-NEC.pdf` (not opened)

### 3. Asana (workspace razorprofiles.com, gid 1201441958896894)
- Walter's user: Walter Lentfert, walter.lentfert@razorprofiles.com (gid 1201441837870467). Stuart: gid 1201441969200259.
- **Existing project "RazorProfiles.com"** (gid 1209525694848848), owned by Walter, private, no team, created Feb 27, 2025. Notes: "Project generated from Razor Profiles.pdf". 39 tasks: 32 done, 7 open. Members: Walter, Stuart, Charlotte Wilkinson, Matt. Custom fields: Content Type (Wireframe/Description/Content) and Team support (people). Link: https://app.asana.com/1/1201441958896894/project/1209525694848848
  - Milestones:
    - Input to wireframes (Stuart, May 2025)
    - Finalise wireframes (Walter)
    - Content developed in a Google Sheet (Matt, done May 27, 2025)
    - Figma designs for the first 3 pages, all modules and mobile (maria@upthereeverywhere.com, Jun–Aug 2025)
    - Module creation "using HiArc modules with stripped-out theme" (Jim Nouvakis)
    - Apply design to site (Stuart, done Aug 19, 2025)
    - Content applied (Walter)
    - **Final website to go live (due Aug 1, 2025): still OPEN**
  - Tickets:
    - Done: Razor card (gradient/frosted), Flex Column, header/menu (dark-mode-ready), footer, hero/CTA, article key cards, polishing, SVG backgrounds, dark mode, a new Svelte theme (Jim), theme boilerplate from HiArc, and the new interactive module (Figma by "Amber").
    - Open: "Horizontal story module for website" (Jim, due Nov 5, 2025).
  - Content sections:
    - Done: Website Development, Digital Strategy, Life Sciences / Medical Device focus, Agency Services.
    - Open: Account Based Marketing, Marketing Campaign Development ("focus on the Persona Journey"), CRM Implementation/Migration, Privacy Policy, Terms & Conditions.
  - Positioning (GET-TO-BY-BECAUSE): *Get* marketing management of clients (Life Science & Med Device) and agency leadership; *To* understand RP's value and unique skill set; *By* highlighting the value/mission statement and range of skills and years of experience; *Because* "Razor Profiles provides turn key solutions that deliver Razor Sharp actionable contact profiles."
- Elsewhere in the workspace, Walter assigns Stuart client tickets (BioCat migration, Tosoh Support Portal Upgrade, Ionetix, Inotiv, IQVIA).

### 4. razorprofiles.com website audit
- Platform: **HubSpot CMS**, portal/hub ID **46015340**, behind HubSpot's Cloudflare edge. The page is a SITE_PAGE (content ID 166463355980), prerendered Jul 7, 2026 7:30 PM ET.
- Theme assets date from Jan 25, 2025 (`template_main.css`, `template_theme-overrides.css`). Modules on the page: menu-section, menu-button, quest-basic. jQuery 3.6.0 loads from code.jquery.com. A legacy HubSpot v2 form embed (`hbspt.forms.create`, formId dd66d9b4-…) is present but not visible.
- Content: logo (rp-left-stacked-dark.svg), phone +1 732-299-0067, "Welcome to Razor Profiles — Our site is currently under construction". The title is "Razor Profiles"; og:image is socialmedia-wordmark.png.
- Fonts are Philosopher and Assistant (on brand). The override CSS mostly uses #0f437f, #425b76 and #1e3d60, which are not the brand palette's #20386C / #28ABE2 / #D6DF27.
- Pages: only `/` exists. /about, /services and /contact return HubSpot 404s, and /blog returns 404. The sitemap lists only the homepage (lastmod Jan 25, 2025).
- **https://www.razorprofiles.com returns 404** (Microsoft-HTTPAPI). www has no CNAME or redirect to the apex, so this needs fixing in the redesign.
- DNS: GoDaddy nameservers (domaincontrol.com); apex A records 199.60.103.41 / .141 (HubSpot); MX is Google Workspace. TXT records include Google and Microsoft site verification, Smartsheet validation, and SPF via a GoDaddy-managed include.
- Redesign observations:
  - It is effectively a greenfield site, with no SEO equity to preserve beyond the homepage.
  - Fix www, add real IA (services, industries, case studies, about/team, contact) and legal pages.
  - Drop the jQuery dependency.
  - Align tokens to the 2024 brand guidelines.
  - Decide whether to build on the 2025 Svelte/HiArc-based theme (location unknown) or the new Aug 2026 Astro scaffold.

### 5. Web & LinkedIn
- LinkedIn company "Razor Profiles LLC" (linkedin.com/company/razor-profiles-llc): IT & Services, founded 2008, HQ Wilmington, 1 employee, 15 followers. About text: "helping you to optimize your relationship with your customers. It all begins with customer profiling…". Also mentions CRM systems (lead, opportunity, incident, proposal management), order processing/e-commerce, CRM–web–marketing automation integration, and SaaS products in development.
- HubSpot Solutions Directory listing (ecosystem.hubspot.com/marketplace/solutions/razor-profiles), from the search snippet (direct fetch hit a cookie wall):
  - Remote. Services include ABM, branding, content, CRM implementation/migration, custom API integrations, email, help desk, knowledge base, programmable automation, SEO, and website design/development/migration.
  - Languages English and Dutch. Budgets $5,000+. Regions: North America, EMEA and South America.
  - "specialized in servicing medical devices/Life Sciences and Pharma/Biotech… 12 yrs experience implementing/migrating… HubSpot."
- Business listing (exa.ai place data): 2722 Shandy Ln, Wilmington, NC 28409; Facebook page id 119273941466350. Unverified.
- Walter, LinkedIn (linkedin.com/in/walterlentfert): Greater Wilmington; 500+ connections, 1,185 followers.
  - Founder President of Razor Profiles since Jan 2008.
  - "E-Strategy, Marketing, Sales & Execution" at UP THERE, EVERYWHERE since Nov 2011.
  - Co-Founder and Board Member of SAMPS, May 2012–Apr 2020.
  - GE HealthCare, Director Commercial Operations – Functional Technology, Apr 2010–Jun 2011.
  - "over 30 years of professional experience".
- UP THERE, EVERYWHERE pages:
  - Member profile (upthereeverywhere.com/up-member-profile-walter-lentfert): "Director of IT & Digital Implementation, Wilmington NC… biochemical engineering degree… GE Healthcare Life Sciences in The Netherlands, Sweden and the United States… customer projects like GE, Tecan, Gyros, Netsize, UL… co-founder and board member of ACP-LS."
  - Leadership team page.
  - Nordic HubSpot event page: "Head of HubSpot US… leads the agency's relationship with HubSpot. Dutch-born but based on the East Coast."

### 6. Gmail (razor), light pass
- Walter writes from walter.lentfert@razorprofiles.com and signs "Walter" or "W". No formal signature block, title or personal phone was found in the messages sampled. The only phone found anywhere is the company line +1 732-299-0067, on the site and LinkedIn.
- He forwards client mail (Ionetix, BioCat) to Stuart, cc's Charlotte Wilkinson and Matt Wilkinson (both @razorprofiles.com; Matt also uses matt@strivenn.com), and assigns Asana tasks.
- Walter prefers Google Fonts for licensing (Oct 5, 2026 thread).
- No email about the Razor Profiles website itself was found in this pass.

## People connected to the website project (from Asana)
| Person | Role seen |
|---|---|
| Walter Lentfert | Owner/founder; wireframes, content review, approvals |
| Stuart Grant | Wireframe input, applied design, Flex Columns; HubSpot engineering |
| Matt (Wilkinson) | Content development (Google Sheet) |
| Charlotte Wilkinson | Project member |
| maria@upthereeverywhere.com | Figma designs (pages, modules, mobile) |
| Amber | Figma designs for the new interactive module |
| Jim Nouvakis | Module/theme development (Svelte theme, HiArc boilerplate, header/footer) |

## Open questions & gaps
1. Where is the 2025 build (Jim's Svelte theme, the modules and Stuart's applied design)? It's not in C:\Users\stu\Code. Is it in HubSpot Design Manager on portal 46015340 or in a GitHub repo? Why didn't it go live?
2. Should the new build continue the 2025 Figma designs or start fresh from the Aug 2026 Astro scaffold? The scaffold's tokens need to be swapped for the brand palette and fonts.
3. Where are the Figma files (UP/Maria, Amber) and the content Google Sheet? The Sheet link is in the Asana "Content developed" task.
4. Brand guideline inconsistency: Deep Blue is given as #20386C and as #003271.
5. Positioning: the LinkedIn copy (customer profiling/CRM, SaaS) is dated. Is the current pitch HubSpot partner for life sciences, per the Directory listing and the GET-TO-BY-BECAUSE?
6. Which case studies or clients can be named publicly (Ionetix, BioCat, Tosoh, IQVIA/CRL, Inotiv)? NDAs apply to at least Ionetix.
7. HubSpot access for portal 46015340: `HS Auth (Razor Profiles).pdf` exists (not opened), and a personal access key will be needed for the CLI.
8. Unverified: the street address (third-party place data), and Walter's exact current UP title (the profile and the event page differ).
9. Not opened: Razor Profiles.one (OneNote), redux.ai, rp.psd, 1099-NEC.

## Blocked / not done
- The HubSpot Solutions Directory page hit a cookie wall on direct fetch, so its content comes from search snippets.
- LinkedIn was not fetched directly; its content comes from search snippets.
- No new Asana or other project was created (outside this brief, and it would be a write).

## Website content found in email & Slack
Added Thu Oct 22, 2026 (ET). Read-only: nothing was sent, changed or shared. Sources: Gmail razor (stuart.grant@razorprofiles.com), Gmail personal, Gmail campgrant, Outlook, and Slack (razorprofilescom workspace, including DMs). Saved files are under `/workspace/razor-profiles/content/`.

**Headline:** There is a real sitemap (FlowMapp, 22 pages), and it is reproduced below. The actual page copy lives in a Google Sheet that Walter sent to the Figma designer. That Sheet is not public, and no Drive connector is available, so its text could **not** be pulled. Two testimonial quotes and the homepage GET/TO/BY/BECAUSE statement were captured. The redesign actually ran in **two rounds**. Round 1 (Feb–May 2025) used freelance designer **Laura Pursel**, and that contract was ended on Apr 30, 2025. Round 2 (Jun–Nov 2025) used **Maria Lindberg Bogdan** (UP THERE, EVERYWHERE) for the Figma designs, **Jim Nouvakis** for the HiArc-based modules, and **Amber Ortiz** for an interactive hero/animation concept.

### Sitemap (FlowMapp, "Razor Profiles Project")
- Link: https://app.flowmapp.com/share/projects/ddf1660c-3284-4cd7-ab3d-d3e9aca875d6/sitemap/5aa1cbed-a951-4951-aebd-34e22bd5f9f9
- Shared by Walter → Laura (cc Stuart) on Feb 11, 2025, and re-posted in Slack #razor-profiles-web on May 17, 2025 ("current status... missing partnership pages... is the original direction with comments").
- The project was created Nov 25, 2024, and the sitemap was last updated May 17, 2025. It was captured from the public share page.
- Files: `content/sitemap-flowmapp.md` (tree) and `content/flowmapp-sitemap-raw-pages.json`.

Page list ([ASAP] = launch scope):
- Main page [ASAP]. Content block: *Get:* marketing management of clients (focus Life Science & Med Device) & marketing agency leadership. *To:* select RP to help define/optimize and implement their Sales and Marketing strategy. *By:* a wide range of skills / years of experience (client statements/testimonials, services overview). *Because:* "Razor Profiles provides turn key solutions that deliver Razor Sharp actionable contact profiles."
  - About us [ASAP]: Content; UP (block)
  - Blog [After launch]: Blog List; topic filter; (hidden) audience filter
  - Contact us [ASAP]: Contact (form); "Support and reach"; Contact 04
  - Services [ASAP]: General intro of services and target personae; Digital Strategy / ABM; Website Development / Marketing Campaigns; CRM implementation / Bespoke process development
    - Digital strategy: Identify business challenge(s) → Prioritize based on benefit to Org and cost → Implementation plan
    - Website development: Briefing → Current & Competitor analysis → Define project scope → Sitemap/WF/Design → Develop; HubSpot themes designers; HubSpot-Algolia Search
    - Account Based Marketing implementation: Content; integration svs
    - Marketing Campaigns: Inbound/outbound
    - CRM implementation/migration: Content; Integration svs
    - Bespoke process development: Content
  - HubSpot partner & service provider [ASAP]
  - Partnerships: Strivenn ("Content strategy with intention - focus on the Persona Journey; Scientific content creation with assistance of 'AI with humanity'; Account Based Marketing strategy & execution")
  - Life sciences / Medical device focus [ASAP] → Medical device / LS services → Indexing and web search
  - Marketing Agencies [ASAP] → Agency services; Product
  - Other Experiences [ASAP]: Consumer; Non-Profit
  - Privacy policy; Terms and conditions

### Items found (newest first within each theme)
| Date (ET) | From / channel | Subject / context | What it contains | Link / path | Excerpt |
|---|---|---|---|---|---|
| Jun 27, 2025 | Walter → Maria Lindberg Bogdan (m.linbog@gmail.com), cc Stuart; Gmail razor | "Copy for Razor Profiles website & Quotes" | **The page copy (Google Sheet link)** plus 2 client testimonials ("expecting 5 more") | Sheet: https://docs.google.com/spreadsheets/d/12naTBRcTThRZv1BwcMCpAJw9FgYrIZ-kKdIWOurdHSw/edit (private, 401). Saved: `content/2025-06-27_Walter_copy-and-quotes-email.md` | "Walter and team have been my go-to for all things HubSpot and web development across multiple companies. From Psomagen to 9amHealth…" |
| Feb 11, 2025 | Walter → Laura Pursel, cc Stuart; Gmail razor | "Thank you and documents as promised" | Sitemap link, brand-guideline zip ("Razor Profiles Visual Brand Guidelines 2024 (2).zip", 10.6 MB), IQVIA Figma/WeTransfer as module reference, inspiration (redantler.com, join9am.com) | Gmail thread 194f6c6673711bcc; we.tl link long expired | (paraphrase) sitemap link + IQVIA site/Figma as the module library reference; Red Antler as admired agency |
| May 17–19, 2025 | Walter in Slack #razor-profiles-web (C07A1NUTGJU) | Wireframes | `RAZOR PROFILES -Wireframes.fig` (F08SL9PDH7V) and `…Wireframes V1.1.fig` (F08TM7M78SC), 5.3 MB each. Matt asked whether to write content into unstyled modules or Word | Slack files (binary; the connector returned corrupted bytes, so they couldn't be extracted. Download from Slack directly) | "current status... missing partnership pages… below is the figma wireframe for input" |
| Jul 1, 2024 | Bea (designer, now deactivated) in #razor-profiles-web | First (2024) attempt: content brief | List of content needed: about/company profile, services with short descriptions, work samples (client/problem/solution/output), contact details. Figma moodboard | https://www.figma.com/board/BcSDvzBl4xGKvwDvEwZ3Rw/Razor-Profiles-Website-Moodboard | "List of services with short descriptions • Sample of work with ff details: Who was the client, Problem, Solution, Final Output" |
| Mar 3, 2025 | Zoom AI summary, fwd by Walter → Laura + Stuart | "Meeting Summary for Razor Profiles design" | 3 moodboard directions (Gradient Immersion, **Macro/Micro 3D Möbius Framing** = preferred, Dynamic Light Refraction); a "sentence of intent for every page"; testimonials from client relationships (e.g. IQVIA); WCAG balance | `content/2025-03-03_Zoom-summary_Razor-Profiles-design.txt` | "The team expressed a preference for the second direction… the Mobius to be used as an element, with animation supporting the brand's message." |
| Feb 17 / Feb 24, 2025 | Laura Pursel ↔ Walter; Gmail razor | "Razor Profiles Design Estimate" / "Scope of work as requested" | Design estimate PDF and agreed SOW PDF. Core pages: Homepage, About, Services + subpages (Digital Strategy, Website Dev, CRM), Contact, Marketing Agencies & Other Experiences, Privacy/Terms; blog post-launch. $8,500 agreed | `content/2025-02-17_Laura-Pursel_Design-Estimate.pdf/.txt`, `content/2025-02_Laura-Pursel_SOW.pdf/.txt` | "Existing assets include a site map, module library, and brand guidelines." |
| Mar 3 / Mar 14 / Mar 31, 2025 | Laura (Google Slides / Figma) | Moodboards R1, Möbius construction deck, Main Page Design R1 | Design artefacts | Slides: https://docs.google.com/presentation/d/1i1cfAIjKvGjsrq65upc068N_5kvytVGqj0Thc5On2xE · https://docs.google.com/presentation/d/1OmODpRfJzDl3SgUiqsYrKNFOTpOXZNRy0bZpNFiDSaY · Figma: https://www.figma.com/design/2H1eyaHA5M7GN1d4j7BSLT/Razor-Profiles (not opened) | "this layer of design isn't showing our desired overlay effects / glass morphism" |
| Apr 28–May 6, 2025 | Walter ↔ Laura; Gmail razor | "Can we set up a meeting pls…", "Project end process", WeTransfer package | **Walter's detailed design brief/feedback**: sticky mega-menu; condensed footer; homepage hero = 10–15 s Möbius story animation; likes Alt 3 three-block; bold full-width CTA; WCAG 2.2; blog list like IQVIA. Project stopped Apr 30 ($3,600 paid; ~10% into Phase 2) | `content/2025-04_Walter-Laura_design-feedback-thread.txt` | "This will be a site that will be seen as a good example and representation of what we can build for them, fresh, interactive, challenging…" |
| Jun 12–20, 2025 | Walter → Maria Lindberg Bogdan + Stuart (calendar invites) | "Moodboard Razor Profiles", "Razor Profiles designs", "3 pages Razor Profiles", "All Razor Profiles modules and mobile treatment of key modules", "other modules Desktop behavior" | Design review meetings for round 2 (no body text) | Gmail razor | Slack (Jun 20): "Monday we will get 3 pages, Friday all modules, and Monday June 30 also mobile treatment… so we are 1 week delayed" |
| Jul 1–7, 2025 | Walter / Charlotte / Stuart in Slack group DMs (C08HN1L8NR1, C08MX8VJ90Q, D07HT262J0L) | Round-2 Figma | **Razor Profiles Design** Figma (Maria) handed to Jim. Build = HiArc modules + Razor styling, with light **and dark** versions. Header/footer/hero first | https://www.figma.com/design/tzTvMplRl69co9FnomfbQZ/Razor-Profiles-Design | Charlotte: "we are using all the functionality and modules as per HiArc and then applying this current design… for Razor there will be the light and dark versions" |
| Jul 8, 2025 | Charlotte in Slack (C08MX8VJ90Q) | Content | Charlotte "added the content to the Razor Profiles project on Asana" (check the Asana tasks for copy) | Asana project 1209525694848848 | "I have added the content to the Razor Profiles project on Asana" |
| Jul 16–28, 2025 | Amber Ortiz ↔ Stuart, Slack DM D08UDPSFDJB | Presentational/interactive module concepts | "Razor Profile Concepts" Figma (static + prototype), ref.mp4 animation reference (F09776BB87J). Stuart's direction: push the "razor sharp" motif | https://www.figma.com/design/EK8U0oaeXhDPOlUgPtCFKa/Razor-Profile-Concepts | Stuart: "ensuring that the 'razor sharp' motif is pushed as best as you can visually." |
| Jul 18 / Nov 12, 2025 | Jim / Charlotte, Slack C08MX8VJ90Q | Build status | Jim sent "the RP theme" to Walter on Jul 18; on Nov 12 Jim: "RazorProfiles Done. I have to review with Stuart." | — | "RazorProfiles Done. I have to review with Stuart." |
| Jun 24, 2025 | Stuart → Jim, Slack DM | Repo | Stuart set up a Razor Profiles GitHub repo for Jim's boilerplate (likely kingpoststudio/razor-profiles) | — | "I'm going to create the Razor Profiles repo within GitHub… This one is more important/higher priority than Tosoh." |
| Oct 22 & 28, 2025 | Stuart / Walter, Slack | Horizontal story module | Spec for the open "Horizontal story module"; Walter wants the "story teller in Razor" | Slack D04CWAR4S5D | (paraphrase) scroll-jacked horizontal story component; Walter: "would like to have the story teller in Razor" |
| Aug 16, 2026 | Stuart → Walter, Slack DM | Case-study idea | Use Playwright screen grabs to build a white paper and Razor case studies | Slack D04CWAR4S5D | "…help build the white paper and subsequent Razor Profiles case studies…" |

### Corrections to earlier sections
- Walter **does** use a signature block in many emails: "Walter Lentfert / Razor Profiles LLC / CellPhone: 732-299-0067 / Email: Walter.Lentfert@RazorProfiles.com / Skype: walter.lentfert". So the 732-299-0067 line is his cell.
- "Maria" in Asana is **Maria Lindberg Bogdan** (maria@upthereeverywhere.com; personal m.linbog@gmail.com). "Amber" is **Amber Ortiz** (Slack). An earlier designer, **Laura Pursel** (laura.pursel.rt@gmail.com, laurapursel.co), did round 1. **Bea (Genato)** did a 2024 moodboard. **Matt Wilkinson** was asked to write the content (May 2025).
- HiArc is a separate UP THERE, EVERYWHERE client site (Figma "HiArc-Website-templates-and-design", also by Maria). Its modules were reused for Razor.

### Searched but empty or blocked
- **Google Sheet of copy** (the key artefact): HTTP 401, and no Drive connector. Needs Stuart or Walter to open or export it.
- **Slack .fig wireframes:** the binary was mangled by the Slack connector, so no text could be extracted.
- **Figma files** (5 Razor files): no Figma connector, and they were not opened.
- **Gmail personal (grantsru@gmail.com):** no Razor website content. There's only a Walter Google Doc "2025/01/23-25 productize idea" (Jan 25, 2025; not opened) and older client shares.
- **Gmail campgrant:** nothing relevant.
- **Outlook:** nothing relevant (4 unrelated hits from 2021–22).
- **Searches with no website content:** "case study", "tagline", "about us" and "bio" turned up no Razor-specific copy beyond what's above. No team bios were found.
- Sensitive data seen in Slack DMs (plaintext passwords for other tools) was deliberately not copied here.
