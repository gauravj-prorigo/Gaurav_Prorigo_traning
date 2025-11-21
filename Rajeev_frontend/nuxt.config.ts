export default defineNuxtConfig({
  modules: [
    '@pinia/nuxt',
    '@nuxt/devtools',
    ['@nuxtjs/google-fonts', {
      families: {
        'Bebas Neue': true,
        'Knewave':true,
        Poppins: [300, 400, 500, 600, 700],
        Roboto: [100, 300, 400, 500, 700]
      },
      display: 'swap'
    }]
  ],
  runtimeConfig: {
    public: { apiBase: 'http://127.0.0.1:8000/api' }
  },
  // google-fonts options are provided inline in the modules array to satisfy
  // TypeScript typings (avoids unknown root property errors).
  devtools: { enabled: true }
})
