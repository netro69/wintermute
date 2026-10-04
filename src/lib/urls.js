// BASE_URL includes the trailing slash (astro.config.mjs).
export const withBase = (path = '') => `${import.meta.env.BASE_URL}${path.replace(/^\/+/, '')}`;
