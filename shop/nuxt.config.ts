// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      apiurl: '',
      imgurl: '',
    },
  },
  app: {
    pageTransition: {
      name: 'page',
      mode: "default",
    },
    head: {
      htmlAttrs: { lang: 'ru'},
      title: 'MegaShop',
      titleTemplate: '%s | Shop',
      link: [
        { rel: 'stylesheet', href: '' },
      ],
      script: [
        { src: '' }
      ],
    },
  },
  sitemap: {
    // не заработало
    // sources: ['/server/api/sitemap/urls'],
    defaults: {
      lastmod: new Date().toDateString(),
      priority: 0.5,
      changefreq: 'weekly',
    },
  },
  modules: [
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/image',
    '@nuxt/scripts',
    '@pinia/nuxt',
    'pinia-plugin-persistedstate/nuxt',
    '@nuxtjs/sitemap'
  ]
})