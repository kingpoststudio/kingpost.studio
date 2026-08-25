export interface Service {
  name: string;
  description: string;
}

export const services: Service[] = [
  {
    name: 'Design',
    description: 'How the company shows up, not a template with a logo swap.',
  },
  {
    name: 'Strategy',
    description: 'What the work has to do before anyone draws a page.',
  },
  {
    name: 'UI/UX',
    description: 'How people move through it, on the market and inside the company.',
  },
  {
    name: 'Development',
    description: 'Built to last past launch.',
  },
  {
    name: 'Integrations',
    description: 'The systems already in the business, connected instead of bolted on.',
  },
  {
    name: 'Market optimization',
    description: 'Tuned for how the company actually sells and is found.',
  },
];
