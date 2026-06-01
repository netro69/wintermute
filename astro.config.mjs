import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import nodejs from '@astrojs/node';

export default defineConfig({
  site: 'https://netro69.github.io/wintermute',
  output: 'static',
  adapter: nodejs({
    mode: 'standalone',
  }),
  integrations: [mdx()],
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
    },
  },
});
