// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ["~/assets/css/main.css", "nprogress/nprogress.css"],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  modules: ["@pinia/nuxt", "nuxt-primevue", "@nuxt/ui", "nuxt-headlessui"],
  plugins: ["./plugins/nprogress.client.js", "./plugins/axios.js"],
});
