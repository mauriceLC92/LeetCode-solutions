interface Solidiers {
  row: number;
  count: number;
}

function kWeakestRows(mat: number[][], k: number): number[] {
  let soldiersPerRow: Solidiers[] = [];
  mat.forEach((matrix, index) => {
    const solidersInRow = soldierCounter(mat[index]);
    soldiersPerRow.push({
      row: index,
      count: solidersInRow,
    });
  });

  const weakestSoldersPerRow = sortByWeakestSoliders(soldiersPerRow);
  return weakestSoldersPerRow.slice(0, k);
}

const sortByWeakestSoliders = (soldiersArray: Solidiers[]) => {
  return soldiersArray
    .sort((a, b) => {
      if (a.count < b.count) {
        return -1;
      } else if (a.count === b.count && a.row < b.row) {
        return -1;
      } else {
        return 1;
      }
    })
    .map((soldiers) => soldiers.row);
};

const soldierCounter = (soldierList: number[]): number => {
  let soldierCounter = 0;

  let lowPosition = 0;
  let highPosition = soldierList.length - 1;

  // Only soldiers present in the row
  if (soldierList[highPosition] === 1) {
    return soldierList.length;
  }
  // No soldiers in the row
  if (soldierList[0] === 0) {
    return 0;
  }

  while (lowPosition <= highPosition) {
    let middlePosition: number =
      lowPosition + Math.floor((highPosition - lowPosition) / 2);
    let guess = soldierList[middlePosition];

    if (guess === 0) {
      highPosition = middlePosition - 1;
    } else {
      soldierCounter += middlePosition - lowPosition + 1;
      lowPosition = middlePosition + 1;
    }
  }
  return soldierCounter;
};

const matrix = [
  [1, 0],
  [1, 0],
  [1, 0],
  [1, 1],
];

const kRows = 4;

kWeakestRows(matrix, kRows);
