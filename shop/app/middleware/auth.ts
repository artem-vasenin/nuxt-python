import type {LoginResponse} from "~/types/auth.types";

export default defineNuxtRouteMiddleware((from, to) => {
    const auth = useCookie<LoginResponse>('auth');

    if (!auth.value) {
        return navigateTo('/auth')
    }
});
