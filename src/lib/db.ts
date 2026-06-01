import sqlite3 from 'sqlite3';
import { Database } from 'sqlite3';

export function openDb() {
    return new sqlite3.Database(':memory:'); // For initial setup, using memory. Change to file in prod.
}
