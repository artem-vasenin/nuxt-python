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
      link: [
        { rel: 'stylesheet', href: '' },
      ],
      script: [
        { src: '' }
      ],
    },
  },
  modules: [
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/image',
    '@nuxt/scripts'
  ]
})