<script lang="js">
  import { onMount } from "svelte";
  import Tools from "./components/Tools.svelte";
  import Light from "./components/Light.svelte";
  import ErrorPage from "./components/ErrorPage.svelte";
  import ControlButton from "./components/ControlButton.svelte";
  import Github from "./icons/github.svelte";
  import { getState, toggle, setupApi } from "./utils/tower.js";

  const { VITE_APP_TITLE, VITE_DEVICE_URL, VITE_DEVICE_PATH, VITE_GITHUB_SOURCE } = import.meta.env;

  const title =
    VITE_APP_TITLE?.length > 0
      ? VITE_APP_TITLE
      : "Patlite Tower Light Controller";
  setupApi(VITE_DEVICE_URL, VITE_DEVICE_PATH);

  // light tower state, seeded from API
  // & used as APP state
  let state = { a: 0, b: 0, c: 0 };
  let error;

  async function toggleLight(color, value) {
    return toggle(color)
      .then(() => (state[color] = !value))
      .catch((error) => console.log("error while toggling light:\n", error));
  }

  onMount(() =>
    getState()
      .then((s) => (state = s))
      .catch((err) => (error = err)),
  );
</script>

{#if error}
  <ErrorPage {error} />
{/if}

<main class="container">
  <h1>{title}</h1>

  <div class="tower">
    {#each Object.entries(state || {}) as [color, value] (color)}
      <Light {color} state={value} onclick={() => toggleLight(color, value)} />
    {/each}
    <div class="leg"></div>
  </div>

  <div class="actions">
    <Tools updateState={(_state) => (state = _state)} />

    <div class="controls">
      {#each Object.entries(state || {}) as [color, value] (color)}
        <ControlButton
          {color}
          state={value}
          onclick={() => toggleLight(color, value)}
        />
      {/each}
    </div>
  </div>
</main>

<footer>
  <span><a href={VITE_GITHUB_SOURCE || '/'}><Github /></a> &nbsp; with svelte ❤️</span>
</footer>

<style lang="scss">
  h1 {
    max-width: 800px;
    font-size: 3rem;
  }

  .tower {
    margin: 20px 0;
  }

  :global(.tower > .light:first-of-type::before) {
    position: absolute;
    content: "";
    --height: 10px;
    --whitespace: 8%;
    height: var(--height);
    width: calc(100% - var(--whitespace));
    top: calc((var(--height) * -2) + 5px);
    left: calc(var(--whitespace) / 2);
    background-color: grey;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
  }

  :global(.tower > .light:nth-of-type(3)::after) {
    position: absolute;
    content: "";
    --height: 16px;
    --whitespace: 10%;
    height: var(--height);
    width: calc(100% - var(--whitespace));
    bottom: calc(-1 * var(--height) - 5px);
    left: calc(var(--whitespace) / 2);
    background-color: grey;
    border-bottom-left-radius: 6px;
    border-bottom-right-radius: 6px;
  }

  .leg {
    height: 4rem;
    width: 2rem;
    margin: 0 auto;
    background-color: grey;

    border-bottom-left-radius: 6px;
    border-bottom-right-radius: 6px;
  }

  .actions {
    width: 100%;
    max-width: 450px;
  }

  .controls {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }
</style>
