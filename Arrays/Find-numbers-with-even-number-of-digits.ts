const isEven = (num: number) => {
  return num % 2 === 0;
};

function findNumbers(nums: number[]): number {
  let evenDigits = 0;

  nums.forEach((num) => {
    const numLength = num.toString().length;
    if (isEven(numLength)) {
      evenDigits++;
    }
  });

  return evenDigits;
}

const nums = [12, 345, 2, 6, 7896];
const test = [555, 901, 482, 1771];

console.log("findNumbers", findNumbers(test));
