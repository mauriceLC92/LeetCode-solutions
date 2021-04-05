// https://leetcode.com/problems/search-insert-position/

function searchInsert(nums: number[], target: number) {
  let lowPosition = 0;
  let highPosition = nums.length - 1;
  let middleTracker: number;

  if (nums.length === 1) {
    if (nums[0] >= target) {
      return 0;
    } else {
      return 1;
    }
  }

  if (target === 0) {
    return 0;
  }

  while (lowPosition <= highPosition) {
    let middlePosition = Math.floor((lowPosition + highPosition) / 2);
    let itemGuessed = nums[middlePosition];

    middleTracker = middlePosition;

    if (itemGuessed === target) {
      return middlePosition;
    }

    if (itemGuessed > target) {
      highPosition = middlePosition - 1;
    } else {
      lowPosition = middlePosition + 1;
    }
  }

  // solution 1
  if (nums[middleTracker] > target) {
    return middleTracker;
  } else {
    return middleTracker + 1;
  }

  // solution 2
  //   nums.push(target);
  //   nums.sort((a, b) => a - b);
  //   return nums.findIndex((el) => el === target);
}

// const list = [1, 3, 5, 6];
const list = [3, 5, 7, 9, 10];
const target1 = 8;

const list2 = [2, 5, 10, 17, 33, 36, 44, 99];
const target2 = 15;

console.log("", searchInsert(list, target1));
