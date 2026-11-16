# kingpost.studio

Static site for King Post Studio.

Astro 5, TypeScript, Pirata One for headings and Manrope for body/UI (brandbook stand-in for Proxima Nova), one global CSS file. No UI islands.

## Routes

| Route | Purpose |
|-------|---------|
| `/` | Home |
| `/work` | Clients and tools |
| `/about` | Studio |
| `/contact` | Email and profiles — no form |

## Develop

```bash
bun install
bun run dev
```

## Build

```bash
bun run build
bun run preview
```

Output is static (`dist/`).

## Docs

Razor Profiles standing context — the dossier, decisions, and Rio's design proposals — lives in [`docs/razor-profiles/`](docs/razor-profiles/) on this branch. It is not part of the site build.

