export interface User {
    id: number;
    email: string;
    name: string;
    phone: string;
    delivery_address: string;
    created_at: string;
    updated_at: string;
}

export interface LoginResponse {
    token: string;
    user: User;
}