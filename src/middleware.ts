import { defineMiddleware } from "astro:middleware";
import { luciaInstance } from "./lib/auth";

export const onRequest = defineMiddleware(async (context, next) => {
	if (context.url.pathname.startsWith("/discussion")) {
		const session = await luciaInstance.readSession(context.request, {
			cookieName: "auth_session",
		});

		if (!session) {
			return context.redirect("/login");
		}
	}

	return next();
});
