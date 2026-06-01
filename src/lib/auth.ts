import { lucia } from "lucia";
import { Lucia } from "lucia";
import { BetterSqlite3Adapter } from "@lucia-auth/adapter-sqlite";
import { openDb } from "./db";

export const adapter = new BetterSqlite3Adapter(openDb(), {
	user: "user",
	session: "session",
});

export const luciaInstance = new Lucia(adapter, {
	sessionCookie: "auth_session",
	getUserAttributes: (attributes) => {
		return {
			username: attributes.username,
		};
	},
});
