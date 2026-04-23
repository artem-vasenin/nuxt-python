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
    
    async function tmpFetchData() {
        const data = await $fetch('http://localhost:3000/api/categories');
        console.log(data);
    }

    return { favoriteIds, addToFavorite, delFavorite, tmpFetchData };
});