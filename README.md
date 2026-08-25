# kingpost.studio

Marketing / portfolio site for King Post Studio.

Stack: Astro + Vite + TypeScript. Plain CSS. Minimal dependencies.

## Pages (outline)

| Route | Purpose |
|-------|---------|
| `/` | Homepage outline |
| `/portfolio` | Portfolio listing |
| `/portfolio/[id]` | Portfolio detail (content collection) |
| `/about` | Mission / about |
| `/contact` | Contact links |

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

## Deploy

- Host on Vercel; attach domain `kingpost.studio`.
- Static output by default (`astro build` → `dist/`).

## Related

`kingpoststudio.com` continues to host HubSpot API proxies and should redirect non-API traffic here.
