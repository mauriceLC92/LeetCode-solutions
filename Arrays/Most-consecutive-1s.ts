function findMaxConsecutiveOnes(nums: number[]): number {
  let mostConsecutiveOnes = 0;
  let currentCount = 0;

  nums.forEach((num) => {
    if (num === 0) {
      if (currentCount <= mostConsecutiveOnes) {
        currentCount = 0;
      } else {
        mostConsecutiveOnes = currentCount;
        currentCount = 0;
      }
    } else {
      currentCount++;
    }
  });

  if (currentCount >= mostConsecutiveOnes) {
    return currentCount;
  }
  return mostConsecutiveOnes;
}

const nums = [1, 1, 0, 1, 1, 1];

findMaxConsecutiveOnes(nums);
