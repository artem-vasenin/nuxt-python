export const useFavoriteStore = defineStore('favorite', () => {
    const favoriteIds = ref<number[]>([]);

    function addToFavorite(id: number) {
        if (!favoriteIds.value.includes(id)) {
            favoriteIds.value.push(id);
        }
    }

    function delFavorite(id: number) {
        if (favoriteIds.value.includes(id)) {
            favoriteIds.value = favoriteIds.value.filter(i => i !== id);
        }
    }
    
    function isFavorite(id: number) {
        return favoriteIds.value.includes(id);
    }

    function toggleFavorite(id: number) {
        if (isFavorite(id)) {
            delFavorite(id);
        } else {
            addToFavorite(id);
        }
    }

    return { favoriteIds, addToFavorite, delFavorite, isFavorite, toggleFavorite };
});