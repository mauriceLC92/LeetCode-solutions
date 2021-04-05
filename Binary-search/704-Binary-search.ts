/**
 *
 * @param list - Ordered list of items.
 * @param item - The item whose position is to be found.
 * @returns The position of the item.
 */

const binarySearch = <T>(list: T[], item: T): number | null => {
  let lowPosition: number = 0;
  let highPosition: number = list.length - 1;

  while (lowPosition <= highPosition) {
    let middlePosition: number = Math.floor((lowPosition + highPosition) / 2);
    let itemGuessed = list[middlePosition];
    if (itemGuessed === item) {
      return middlePosition;
    }
    if (itemGuessed > item) {
      highPosition = middlePosition - 1;
    } else {
      lowPosition = middlePosition + 1;
    }
  }
  return null;
};

// For binary search with massive numbers
// use the following to avoid integer overflow
// mid = lo + (hi - lo) / 2

const orderedList = [2, 5, 10, 17, 33, 36, 44, 99];
const targetItem = 10;

binarySearch(orderedList, targetItem);
console.log("Found at postion", binarySearch(orderedList, targetItem));

const binarySearchForLoop = <T>(list: T[], item: T): number | null => {
  let lowPostion = 0;
  let highPostion = list.length - 1;

  for (let i = 0; lowPostion <= highPostion; i++) {
    let middlePosition = Math.floor((lowPostion + highPostion) / 2);
    let itemGuessed = list[middlePosition];

    if (itemGuessed === item) {
      return middlePosition;
    }

    if (itemGuessed < item) {
      lowPostion = middlePosition + 1;
    } else {
      highPostion = middlePosition - 1;
    }
  }

  return null;
};

const myOrderedList = [2, 5, 10, 17, 33, 36, 44, 99];
const target = 4;

console.log("Found at position", binarySearchForLoop(myOrderedList, target));
