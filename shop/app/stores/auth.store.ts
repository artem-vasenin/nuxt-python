import type {LoginResponse, User} from "~/types/auth.types";

export const useAuthStore = defineStore('auth', () => {
    const token = ref<string | undefined>();
    const user = ref<User | undefined>();

    function loginUser(dto: LoginResponse) {
        token.value = dto.token;
        user.value = dto.user;
    }

    function logout() {
        token.value = undefined;
        user.value = undefined;
    }

    return { token, user, loginUser, logout };
}, { persist: true });