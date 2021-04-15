/**
 Do not return anything, modify arr in-place instead.
 */
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
  console.log(arr);
}

const dups = [1, 5, 2, 0, 6, 8, 0, 6, 0];

duplicateZeros(dups);

// const dups = (arr: number[]) => {
//   let countZeros = arr.filter((num) => num === 0).length;
//   const arrLen = arr.length;

//   for (let index = arrLen - 1; index >= 0; index--) {
//     if (index + countZeros < arrLen) {
//       arr[index + countZeros] = arr[index];
//     }

//     if (arr[index] === 0) {
//       countZeros--;
//       if (index + countZeros < arrLen) {
//         arr[index + countZeros] = 0;
//       }
//     }
//   }
// };
