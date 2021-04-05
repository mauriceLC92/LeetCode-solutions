interface Soliders {
  row: number;
  count: number;
}
function kWeakestRows(mat: number[][], k: number): number[] {
  let solidersPerRow: Soliders[] = [];

  mat.forEach((matrix, index) => {
    const solidiersCount = matrix.filter((el) => el === 1).length;
    solidersPerRow.push({
      row: index,
      count: solidiersCount,
    });
  });

  solidersPerRow.sort((a, b) => {
    if (a.count < b.count) {
      return -1;
    } else if (a.count === b.count && a.row < b.row) {
      return -1;
    } else {
      return 1;
    }
  });

  let weakestRows: number[] = [];
  solidersPerRow.slice(0, k).forEach((row) => weakestRows.push(row.row));
  return weakestRows;
}

const mat = [
  [1, 1, 0, 0, 0],
  [1, 1, 1, 1, 0],
  [1, 0, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [1, 1, 1, 1, 1],
];

const k = 3;

kWeakestRows(mat, 3);
