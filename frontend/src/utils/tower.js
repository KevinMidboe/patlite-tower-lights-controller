let BASE_URL, BASE_PATH;

export function setupApi(url, path) {
  BASE_URL = url;
  BASE_PATH = path;
}

export async function getState() {
  const url = `${BASE_URL}${BASE_PATH}state`;

  return fetch(url).then((resp) => resp.json());
}

export async function toggle(color) {
  const url = `${BASE_URL}${BASE_PATH}toggle/${color}`;
  const options = { method: "POST" };

  return fetch(url, options);
}

export async function setTower(colorStates) {
  const url = `${BASE_URL}${BASE_PATH}state/set`;
  const options = {
    method: "POST",
    header: {
      "Content-Type": "plain/text",
    },
    body: colorStates.join(","),
  };

  return fetch(url, options);
}
