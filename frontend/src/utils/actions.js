export function sleep(hundredSeconds) {
  return new Promise((resolve) => setTimeout(resolve, hundredSeconds * 100));
}

export const errorSeq = [
  [0, 0, 1, 1],
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 6],
  [0, 0, 1, 2],
  [0, 0, 0, 2],
  [0, 0, 1, 2],
  [0, 0, 0, 2],
  [0, 0, 1, 2],
  [0, 0, 0, 6],
  [0, 0, 1, 1],
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 20],
];

export const trafficSeq = [
  [0, 0, 1, 15],
  [0, 1, 1, 15],
  [1, 0, 0, 50],
  [0, 1, 0, 15],
  [0, 0, 1, 20],
];

export const warningSeq = [
  [0, 1, 0, 3],
  [0, 0, 0, 3],
  [0, 1, 0, 3],
  [0, 0, 0, 10],
];
