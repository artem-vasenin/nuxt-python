export interface Category {
    id: number;
    name: string;
    alias: string;
}

export interface CategoriesResponse {
    categories: Category[];
}

export interface Product {
    id: number;
    name: string;
    price: number;
    short_description: string;
    long_description: string;
    sku: string;
    discount: number;
    images: string[];
    category_id: number;
    category: Category;
}

export interface ProductResponse {
    products: Product[];
    total: number;
    limit: number;
    offset: number;
}