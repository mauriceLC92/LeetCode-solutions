const findSmallest = (arr: number[]): number => {
  let smallestIndex = 0;
  let smallestElement = arr[smallestIndex];

  for (let index = 1; index < arr.length; index++) {
    if (arr[index] < smallestElement) {
      smallestIndex = index;
      smallestElement = arr[index];
    }
  }

  return smallestIndex;
};

const selectionSort = (arr: number[]): number[] => {
  let sortedArray: number[] = [];
  const arrLen = arr.length;

  for (let index = 0; index < arrLen; index++) {
    const smallestIndex = findSmallest(arr);
    sortedArray.push(arr.splice(smallestIndex, 1)[0]);
  }

  return sortedArray;
};

function sortedSquares(nums: number[]): number[] {
  const squaredNums = nums.map((num) => num * num);
  return selectionSort(squaredNums);
}

const nums = [-4, -1, 0, 3, 10];

console.log("sortedSquares", sortedSquares(nums));
