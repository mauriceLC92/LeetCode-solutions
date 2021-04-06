function peakIndexInMountainArray(arr: number[]): number {
  let lowPosition = 0;
  let highPosition = arr.length - 1;

  if (arr[0] === 0) {
    return 1;
  }

  while (lowPosition <= highPosition) {
    let middlePostion =
      lowPosition + Math.floor((highPosition - lowPosition) / 2);
    let guess = arr[middlePostion];

    if (typeof arr[middlePostion - 1] === "undefined") {
      return 1;
    }
    if (typeof arr[middlePostion + 1] === "undefined") {
      return arr.length - 1;
    }
    if (arr[middlePostion - 1] < guess && arr[middlePostion + 1] < guess) {
      return middlePostion;
    }

    if (guess > arr[middlePostion - 1]) {
      lowPosition = middlePostion + 1;
    } else {
      highPosition = middlePostion - 1;
    }
  }
}

let arr = [40, 48, 61, 75, 100, 99, 98, 39, 30, 10];
let arr2 = [3, 4, 5, 1];
let arr3 = [3, 5, 3, 2, 0];

console.log("peakIndexInMountainArray", peakIndexInMountainArray(arr3));
