function duplicateZeros(arr: number[]): void {
  let amountOfZeros = arr.filter((num) => num === 0).length;
  const arrayLen = arr.length;

  for (let index: number = arrayLen - 1; index >= 0; index--) {
    if (index + amountOfZeros < arrayLen) {
      arr[index + amountOfZeros] = arr[index];
    }

    if (arr[index] === 0) {
      amountOfZeros--;
      if (index + amountOfZeros < arrayLen) {
        arr[index + amountOfZeros] = 0;
      }
    }
  }
}

const dups = [1, 5, 2, 0, 6, 8, 0, 6, 0];

duplicateZeros(dups);

console.log("dups", dups);

/**
 Do not return anything, modify arr in-place instead.
 */
// This failed based on a bug in my program
// function duplicateZeros(arr: number[]): void {
//   for (let index: number = 0; index < arr.length - 1; index++) {
//     if (arr[index] === 0) {
//       insertAtIndexOfArray(arr, 0, index + 1);
//       index++;
//     }
//   }
// }

// const insertAtIndexOfArray = <T>(arr: T[], target: T, postion: number) => {
//   const elementAtPosition: T = arr[postion];
//   const maxIndex = arr.length - 1;
//   for (let index: number = arr.length - 1; index >= postion; index--) {
//     if (index + 1 > maxIndex) {
//       continue;
//     }
//     arr[index + 1] = arr[index];

//     if (elementAtPosition === arr[index]) {
//       arr[postion] = target;
//     }
//   }
// };
