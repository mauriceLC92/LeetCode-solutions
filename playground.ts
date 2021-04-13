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

console.log("insertStartOfArray", insertAtIndexOfArray(myArray, 12345, 3));
