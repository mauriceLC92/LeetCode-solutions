function countNegativesNumbers(grids: number[][]): number {
  let negativeNumberCount = 0;
  grids.forEach((grid) => {
    // case for all negative numbers
    if (grid[0] < 0) {
      negativeNumberCount = negativeNumberCount + grid.length;
      // first number is 0 then the rest must be negative
    } else if (grid[grid.length - 1] >= 0) {
      negativeNumberCount += 0;
    } else {
      negativeNumberCount += binarySearch(grid);
    }
  });
  return negativeNumberCount;
}

const binarySearch = (list: number[], targetNumber?: number): number => {
  let low = 0;
  let high = list.length - 1;
  let negativeNumberCount = 0;

  let middle: number;
  while (low <= high) {
    middle = low + Math.floor((high - low) / 2);
    let guess = list[middle];

    // is the guess positive?
    if (guess >= 0) {
      low = middle + 1;
    } else {
      negativeNumberCount += high - middle + 1;
      high = middle - 1;
    }
  }

  return negativeNumberCount;
};

// solution that does not use binary search

// function countNegatives(grids: number[][]) {
//   let negativeCounts = 0;
//   grids.forEach((grid) => {
//     const negatives = grid.filter((item) => item < 0).length;
//     negativeCounts += negatives;
//   });
//   return negativeCounts;
// }
