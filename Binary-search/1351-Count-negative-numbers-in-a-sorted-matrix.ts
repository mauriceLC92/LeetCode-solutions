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

function countNegatives(grids: number[][]) {
  let negativeCounts = 0;
  grids.forEach((grid) => {
    const negatives = grid.filter((item) => item < 0).length;
    negativeCounts += negatives;
  });
  return negativeCounts;
}

/**
 * Java answers using a different method
 */

// const countNegatives(int[][] grid) {
//     let n = grid.length;
//     let m = grid[0].length - 1;

//     let row = 0;
//     let col = m;

//     let count = 0;
//     while (row < n && col >= 0) {
//         if (grid[row][col] >= 0) {
//             row++;
//         } else {
//             count += (n - row);
//             col--;
//         }
//     }
//     return count;
// }

// class Solution {
//   public int countNegatives(int[][] grid) {
//       int m = grid.length;
//       int n = grid[0].length;

//       int count = 0;

//       for (int i = 0; i < m; i++) {
//           if (grid[i][n - 1] < 0) {
//               int index = smallestPositiveIndex(grid[i]);
//               count += n - index - 1;
//           }
//       }

//       return count;
//   }

//   private int smallestPositiveIndex(int[] arr) {
//       int lo = 0;
//       int hi = arr.length - 1;
//       int target = -1;
//       int mid = 0;

//       while (lo <= hi) {
//           mid = lo + (hi - lo) / 2;

//           if (arr[mid] > target) {
//               lo = mid + 1;
//               continue;
//           } else if (arr[mid] < target) {
//               hi = mid - 1;
//               continue;
//           }

//           while (mid >= 0 && arr[mid] == target) {
//               mid--;
//           }

//           return mid;
//       }

//       return lo - 1;
//   }
// }
