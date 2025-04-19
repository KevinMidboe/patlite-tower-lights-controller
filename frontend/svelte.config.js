import preprocess from "svelte-preprocess";

export default {
  preprocess: preprocess({
    scss: {
      // Optional: includePaths: ['src/styles']
    },
  }),
  compilerOptions: {
    dev: true,
    compatibility: {
      componentApi: 4, // 👈 This enables `new App()` to work
    },
  },
};
