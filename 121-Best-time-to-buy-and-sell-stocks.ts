function maxProfit(prices: number[]): number {
  const pricesLen = prices.length;
  let maxProfit = 0;
  if (pricesLen === 1) {
    return 0;
  }
  // Brute force solution
  //   for (let index: number = 0; index < pricesLen; index++) {
  //     for (let i = index + 1; i < pricesLen; i++) {
  //       if (prices[i] - prices[index] > maxProfit) {
  //         maxProfit = prices[i] - prices[index];
  //       }
  //     }
  //   }

  let lowestPurchasePrice = prices[0];
  for (let index: number = 0; index < pricesLen; index++) {
    if (prices[index] < lowestPurchasePrice) {
      lowestPurchasePrice = prices[index];
    }
    let calculatedProfit = prices[index + 1] - lowestPurchasePrice;
    if (calculatedProfit > maxProfit) {
      maxProfit = calculatedProfit;
    }
  }

  return maxProfit;
}

const prices = [7, 6, 4, 3, 1];
maxProfit(prices);
