# kingpost.studio

Static site for King Post Studio.

Astro 5, TypeScript, IBM Plex via Fontsource, one global CSS file. No UI islands.

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
