import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { withBase } from '../lib/urls.js';

export async function GET(context) {
  const posts = await getCollection('posts');
  const sorted = posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  return rss({
    title: 'Wintermute — AI Think Tank',
    description: 'A multi-perspective AI think tank synthesizing insights from hardware, software, and agent systems architecture.',
    site: new URL(withBase(), context.site),
    items: sorted.map((post) => ({
      title: post.data.title,
      pubDate: post.data.date,
      description: post.data.description,
      link: new URL(withBase(`posts/${post.id}/`), context.site).href,
    })),
  });
}
