const findSmallestPosition = <T>(arr: T[]): number => {
  let smallestIndex = 0;
  let smallestElement = arr[smallestIndex];

  for (let index: number = 1; index < arr.length; index++) {
    if (arr[index] < smallestElement) {
      smallestElement = arr[index];
      smallestIndex = index;
    }
  }

  return smallestIndex;
};

const selectionSort = <T>(arr: T[]): T[] => {
  let sortedArray: T[] = [];
  const arrayLength: number = arr.length;

  for (let index: number = 0; index < arrayLength; index++) {
    const smallestPosition = findSmallestPosition(arr);
    sortedArray.push(arr.splice(smallestPosition, 1)[0]);
  }

  return sortedArray;
};

const testArr = [5, 3, 6, 2, 10];

console.log("selectionSort", selectionSort(testArr));
