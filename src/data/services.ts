export interface Service {
  name: string;
  description: string;
}

export const services: Service[] = [
  {
    name: 'Design',
    description: 'Sites and systems that hold up past launch, not a template with a logo swap.',
  },
  {
    name: 'Development',
    description: 'Themes, apps, and the libraries behind them.',
  },
  {
    name: 'Integrations',
    description: 'CMS, CRM, and the tools around them, actually talking.',
  },
  {
    name: 'Normalization',
    description: 'One data model and one set of components, instead of a new one-off every time.',
  },
];
