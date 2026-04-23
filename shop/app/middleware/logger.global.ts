export default defineNuxtRouteMiddleware((from, to) => {
    if (import.meta.client) return;
    // if (import.meta.server) console.log('global', from, to);
});