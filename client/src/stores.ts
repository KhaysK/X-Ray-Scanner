import { writable } from "svelte/store";

export let user = writable<User | null>(null);
export let loginToggle = writable<string | null>(null);