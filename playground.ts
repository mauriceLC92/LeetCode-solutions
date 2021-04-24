let myArray = [1, 2, 3, 4, 5, 6];

const insertStartOfArray = <T>(arr: T[], target: T): T[] => {
  const startOfArray: T = arr[0];
  for (let index: number = arr.length - 1; index >= 0; index--) {
    arr[index + 1] = arr[index];

    if (startOfArray === arr[index]) {
      arr[0] = target;
    }
  }
  return arr;
};

const insertAtIndexOfArray = <T>(arr: T[], target: T, postion: number): T[] => {
  const elementAtPosition: T = arr[postion];
  for (let index: number = arr.length - 1; index >= postion; index--) {
    arr[index + 1] = arr[index];

    if (elementAtPosition === arr[index]) {
      arr[postion] = target;
    }
  }

  return arr;
};

// console.log("insertStartOfArray", insertAtIndexOfArray(myArray, 12345, 3));

type MyMap = {
  func: (...args) => void;
  arr: any[];
};

const map = ({ func, arr }: MyMap): any[] => {
  const arrLen = arr.length;
  const newArr = [];

  for (let index: number = 0; index < arrLen; index++) {
    const functionResult = func(arr[index]);
    newArr.push(functionResult);
  }

  return newArr;
};

const incrementOne = (num: number) => num + 1;

const lottoNumbers = [1, 3, 6, 7, 10];

const insertionSort = (arr: number[], val: number): number[] => {
  arr.push(val);

  for (let index = arr.length - 1; index >= 0; index--) {
    let currentX = arr[index];
    let swap = arr[index - 1];
    if (currentX < swap) {
      swap = currentX;
      currentX = arr[index - 1];
    }
    if (arr[index] >= arr[index - 1]) {
      return;
    }
  }
  console.log("arr", arr);
  return arr;
};

console.log("", insertionSort(lottoNumbers, 4));
