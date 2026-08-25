export interface LinkedNote {
  label: string;
  href?: string;
}

export interface WorkEntry {
  name: string;
  notes: LinkedNote[];
  href?: string;
}

export const clients: WorkEntry[] = [
  {
    name: 'Pinhook Excavation',
    notes: [{ label: 'pinhookexcavation.com', href: 'https://pinhookexcavation.com' }],
  },
  {
    name: 'IQVIA',
    notes: [
      { label: 'labs.iqvia.com', href: 'https://labs.iqvia.com' },
      { label: 'IQVIAMaster/RBM' },
    ],
  },
  {
    name: 'Tosoh',
    notes: [{ label: 'themes, microsites, HubDB search' }],
  },
  {
    name: 'Biocat',
    notes: [
      { label: 'genes.biocat.com', href: 'https://genes.biocat.com' },
      { label: 'exosomes.biocat.com', href: 'https://exosomes.biocat.com' },
    ],
  },
  {
    name: 'Inotiv',
    notes: [
      { label: 'InotivTheme2023 for inotiv.com, not benefits', href: 'https://inotiv.com' },
    ],
  },
  {
    name: 'Steroids and Me',
    notes: [{ label: 'steroidsandme.com', href: 'https://steroidsandme.com' }],
  },
  {
    name: 'AegisNS',
    notes: [{ label: 'aegisns.com', href: 'https://aegisns.com' }],
  },
];

export const tools: WorkEntry[] = [
  {
    name: 'TrussUI',
    notes: [],
  },
  {
    name: 'HubSpot Theme Starter',
    notes: [],
    href: 'https://github.com/kingpoststudio/hubspot-theme-starter',
  },
  {
    name: 'hs-fieldkit',
    notes: [],
    href: 'https://www.npmjs.com/package/hs-fieldkit',
  },
  {
    name: 'vite-plugin-upload-to-hubspot',
    notes: [],
    href: 'https://github.com/kingpoststudio/vite-plugin-upload-to-hubspot',
  },
];
