<script>
  import Lamp from "../icons/lamp.svelte";
  import LampBright from "../icons/lamp-bright.svelte";

  let { color, state, onclick } = $props();
</script>

<button class={`control-btn ${color}-btn`} class:active={state} {onclick}>
  <svelte:component this={state ? LampBright : Lamp} />
</button>

<style lang="scss">
  .control-btn {
    margin-top: 2rem;
    padding: 1rem;
    display: flex;
    flex: 1;
    justify-content: center;
    align-items: center;
    font-size: 1rem;
    font-weight: bold;
    color: white;
    border: none;
    border-radius: 1rem;
    cursor: pointer;
    max-height: 5rem;
    transition:
      transform 0.2s ease,
      box-shadow 0.3s ease,
      background-color 0.3s ease;

    &:hover {
      transform: scale(1.1);
    }

    &:focus {
      outline: none;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    }
  }

  :global(.control-btn svg) {
    max-height: 40px;
  }

  /* Individual Button Colors */
  .green-btn {
    background-color: #2ecc71;
    box-shadow: 0 0 10px rgba(46, 204, 113, 0.6);

    &.active {
      background-color: #27ae60;
      box-shadow: 0 0 25px rgba(39, 174, 96, 0.9);
    }
  }

  .orange-btn {
    background-color: #f39c12;
    box-shadow: 0 0 10px rgba(243, 156, 18, 0.6);

    &.active {
      background-color: #e67e22;
      box-shadow: 0 0 25px rgba(230, 126, 34, 0.9);
    }
  }

  .red-btn {
    background-color: #e74c3c;
    box-shadow: 0 0 10px rgba(231, 76, 60, 0.6);

    &.active {
      background-color: #c0392b;
      box-shadow: 0 0 25px rgba(192, 57, 43, 0.9);
    }
  }
</style>
