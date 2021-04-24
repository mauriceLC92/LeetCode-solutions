/**
    Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  const totalLength = m + n;
  const newArray = [];
  for (let index: number = 0; index < m; index++) {
    if (nums1[index] < nums2[index]) {
      newArray.push(nums1[index]);
    } else {
      newArray.push(nums2[index]);
    }
  }

  console.log("new", newArray);
}

const m = 3;
const n = 3;

const nums1 = [1, 2, 3, 0, 0, 0];
const nums2 = [2, 5, 6];

// merge(nums1, m, nums2, n);

for (let index1 = 0; index1 < nums1.length)