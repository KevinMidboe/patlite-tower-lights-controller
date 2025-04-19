<script>
  import { setTower } from "../utils/tower.js";
  import { warningSeq, errorSeq, trafficSeq, sleep } from "../utils/actions.js";

  // action icons
  import RubberDuck from "../icons/rubber-duck.svelte";
  import Warning from "../icons/warning.svelte";
  import Siren from "../icons/siren.svelte";
  import SirenBright from "../icons/siren-bright.svelte";
  import TrafficLights from "../icons/traffic-lights.svelte";
  import Bell from "../icons/bell.svelte";
  import FireHazard from "../icons/fire-hazard.svelte";

  let { updateState } = $props();

  let active = $state("");
  let seqRunning = $state(false);
  let iterator = $state(0);
  let iteratorSelector = 1;
  const ACTIONS = [
    {
      label: "siren",
      icons: [Siren, SirenBright],
      color: "#F63C3D",
      sequence: errorSeq,
    },
    {
      label: "warning",
      icons: [Warning],
      color: "#FFEF10",
      sequence: warningSeq,
    },
    {
      label: "traffic",
      icons: [TrafficLights],
      color: "#828C8A",
      sequence: trafficSeq,
    },
    {
      label: "fire",
      icons: [FireHazard],
      color: "#FF8800",
      sequence: warningSeq,
    },
    {
      label: "duck",
      icons: [RubberDuck],
      color: "#F8CE4C",
      sequence: [
        [0, 1, 0, 10],
        [0, 0, 0, 0],
      ],
    },
    {
      label: "bell",
      icons: [Bell],
      color: "#CDB376",
      sequence: warningSeq,
    },
  ];

  async function runSequence(sequence) {
    iterator = iteratorSelector;

    while (iterator > 0) {
      for (let seq in sequence) {
        const value = sequence[seq];
        const [green, orange, red, timeout] = value;

        await setTower(value.slice(0, 3));
        updateState({ green, orange, red });
        await sleep(timeout);
      }

      iterator -= 1;
    }

    await setTower([0, 0, 0]);
  }

  function toggleAction(action) {
    // abort if currently running
    if (active?.length > 0 || seqRunning) return;

    seqRunning = true;
    active = action.label;

    runSequence(action?.sequence).then(() => {
      seqRunning = false;
      active = null;
    });
  }
</script>

<details class="tools">
  <summary>
    <label
      >Actions <input
        bind:value={iteratorSelector}
        type="number"
        min="1"
      /></label
    >
    <p>Select modes for quick actions</p>
  </summary>

  <div>
    {#each ACTIONS as action (action)}
      <button
        class:active={action.label === active}
        style={`--hover-bg: ${action?.color};`}
        on:click={() => toggleAction(action)}
      >
        {#if action?.icons?.length > 1 && action.label === active}
          <svelte:component this={action.icons[1]} />
        {:else}
          <svelte:component this={action.icons[0]} />
        {/if}
      </button>
    {/each}
  </div>

  <footer>
    {#if seqRunning}
      <p>
        Currently running: {active}, {1 + iteratorSelector - iterator} of {iteratorSelector}
      </p>
    {/if}
  </footer>
</details>

<style lang="scss">
  .tools {
    background-color: #f0f0f0;
    border-radius: 0.5rem;
    padding: 1rem;

    > div {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-evenly;
      margin-top: 1rem;
      gap: 0.5rem;
    }

    summary {
      width: 100%;
      text-align: left;
      cursor: pointer;
      -webkit-user-select: none;
      user-select: none;

      &::-webkit-details-marker,
      &::marker {
        display: none;
      }

      label,
      p {
        width: 100%;
        text-align: left;
        margin: 0;
      }

      label {
        font-size: 1.2rem;
        font-weight: 600;

        input {
          width: 2rem;
          padding: 0.5rem 0.5rem 0.5rem 0.25rem;
          font-size: 1.2rem;
          float: right;
          text-align: right;
          border-radius: 0.5rem;
        }
      }
    }

    button {
      width: 8rem;
      height: 5rem;
      background-color: white;
      padding: 0.5rem;
      border: none;
      border-radius: 0.5rem;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
      transition: all 0.2s ease;
      cursor: pointer;

      &:hover,
      &.active {
        scale: 1.1;
        background-color: var(--hover-bg, rgba(0, 0, 0, 0.7));
        fill: white;
      }
    }
  }

  footer {
    p {
      margin-bottom: 0;
    }
  }

  :global(.tools button svg) {
    max-height: 64px;
  }
</style>
