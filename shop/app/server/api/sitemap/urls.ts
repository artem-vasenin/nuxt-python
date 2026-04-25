import type {Product} from "~/types/catalog.types";
import type {SitemapUrlInput} from "#sitemap/types";

export default defineSitemapEventHandler(async () => {
    const { data } = await useFetch<{products: Product[]}>(useApi() + '/products');
    const pages = (data.value?.products || []).map(p => ({
        loc: `/catalog/${p.id}`,
        changefreq: 'daily',
        priority: 0.5,
    })) satisfies SitemapUrlInput[];

    return pages;
});
