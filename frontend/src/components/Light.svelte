<script>
  let { color, state, onclick } = $props();
</script>

<button class={`light ${color}`} class:active={state} {onclick} />

<style style="scss">
  .light {
    position: relative;
    height: 1.875rem;
    height: 10vh;
    aspect-ratio: 3 / 1;
    margin: 10px auto;
    border-radius: 1rem;
    background-color: #ccc;
    cursor: pointer;
    transition:
      transform 0.1s ease,
      box-shadow 0.2s ease,
      background-color 0.2s ease;

    border: none;
    display: block;
  }

  .green {
    background-color: #2ecc71;

    &.active {
      background-color: #2ecc71;
      box-shadow:
        0 0 25px rgba(46, 204, 113, 0.9),
        0 0 20px rgba(46, 204, 113, 0.5);
      transform: scale(1.1);
    }
  }
  .orange {
    background-color: #f39c12;

    &.active {
      background-color: #f39c12;
      box-shadow:
        0 0 25px rgba(243, 156, 18, 0.9),
        0 0 20px rgba(243, 156, 18, 0.5);
      transform: scale(1.1);
    }
  }
  .red {
    background-color: #e74c3c;

    &.active {
      background-color: #e74c3c;
      box-shadow:
        0 0 25px rgba(231, 76, 60, 0.9),
        0 0 20px rgba(231, 76, 60, 0.5);
      transform: scale(1.1);
    }
  }
</style>
