import { defineMiddleware } from "astro:middleware";

// No protected routes — the blog is open to everyone.
// Middleware kept as a hook for future use (analytics, geo, etc.).
export const onRequest = defineMiddleware(async (_context, next) => {
  return next();
});
