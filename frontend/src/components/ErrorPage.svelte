<script>
  let { error, title = "Whoops! A error occured" } = $props();

  const importantEnvironmentVariables = {
    VITE_DEVICE_URL: "",
    VITE_DEVICE_PATH: "",
  };

  const env = { ...importantEnvironmentVariables, ...import.meta.env };
</script>

<article>
  <h1>{title}</h1>
  <p>
    it is sad when the application does not work, but below is a stack trace and
    current environment variables for deugging.
  </p>

  <div>
    <label>Stack trace</label>
    <code>
      <p>Error occured and returned message: "{error}"</p>

      <p>{error?.stack}</p>
    </code>

    <label>Environment variables</label>
    <code>
      {#each Object.entries(env) as [key, value] (key)}
        <span>{key}: {value}<br /></span>
      {/each}
    </code>
  </div>
</article>

<style style="scss">
  article {
    display: flex;
    flex-direction: column;
    justify-content: center;
    --margin: 1rem;
    width: calc(100% - var(--margin) * 4);
    max-width: 800px;
    margin: var(--margin);
    padding: var(--margin);
    border: 4px dashed #ff8800;
    border-radius: 0.5rem;

    @media screen and (max-width: 750px) {
      width: unset;
      border: none;
      margin: 0;
      padding: 0.5rem;
    }

    > div {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      width: 100%;
    }

    > p {
      font-size: 1.2rem;
    }
  }

  label {
    font-weight: bold;
    margin-bottom: 0.5rem;
    margin-top: 2rem;
  }

  code {
    overflow: scroll;
    max-width: 90vw;
    background-color: #1c1819;
    max-height: calc(90vh - 10rem);
    color: #fff;
    border-radius: 0.75rem;
    padding: 1rem;
    line-height: 1.4;
  }
</style>
