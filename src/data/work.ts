export interface WorkLink {
  label: string;
  href: string;
}

export interface WorkEntry {
  name: string;
  description: string;
  links?: WorkLink[];
  href?: string;
}

export const clients: WorkEntry[] = [
  {
    name: 'Pinhook Excavation',
    description: 'HubSpot CMS site for a western North Carolina excavation company.',
    links: [{ label: 'pinhookexcavation.com', href: 'https://pinhookexcavation.com' }],
  },
  {
    name: 'IQVIA',
    description: 'HubSpot parent and child themes (IQVIAMaster, RBM) with shared UI.',
    links: [{ label: 'labs.iqvia.com', href: 'https://labs.iqvia.com' }],
  },
  {
    name: 'Tosoh',
    description: 'HubSpot themes, microsites, and HubDB search.',
  },
  {
    name: 'Biocat',
    description: 'HubSpot CMS e-commerce theme for Biocat GmbH.',
    links: [
      { label: 'genes.biocat.com', href: 'https://genes.biocat.com' },
      { label: 'exosomes.biocat.com', href: 'https://exosomes.biocat.com' },
    ],
  },
  {
    name: 'Inotiv',
    description: 'HubSpot theme (InotivTheme2023) for',
    links: [{ label: 'inotiv.com', href: 'https://inotiv.com' }],
  },
  {
    name: 'Steroids and Me',
    description: 'HubSpot CMS and a React app.',
    links: [{ label: 'steroidsandme.com', href: 'https://steroidsandme.com' }],
  },
  {
    name: 'AegisNS',
    description: 'HubSpot theme and a Remix marketing site.',
    links: [{ label: 'aegisns.com', href: 'https://aegisns.com' }],
  },
];

export const tools: WorkEntry[] = [
  {
    name: 'TrussUI',
    description: 'Lit web components for HubSpot themes.',
  },
  {
    name: 'HubSpot Theme Starter',
    description: 'Public Lit, Vite, and Storybook starter.',
    href: 'https://github.com/kingpoststudio/hubspot-theme-starter',
  },
  {
    name: 'hs-fieldkit',
    description: 'TypeScript builders for HubSpot module fields.',
    href: 'https://www.npmjs.com/package/hs-fieldkit',
  },
  {
    name: 'vite-plugin-upload-to-hubspot',
    description: 'Vite plugin that uploads a build to HubSpot.',
    href: 'https://github.com/kingpoststudio/vite-plugin-upload-to-hubspot',
  },
];
