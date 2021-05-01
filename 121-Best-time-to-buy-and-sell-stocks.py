# Brute force initial solution
# times out on a massive prices input on LeetCode but passes all other test cases
def maxProfit(prices) -> int:
    highest_profit = 0
    prices_len = len(prices)

    if prices_len == 1:
        return 0

    for index, value in enumerate(prices):
        for index2 in range(index + 1, prices_len):
            profit = prices[index2] - value

            if profit > highest_profit:
                highest_profit = profit

    return highest_profit


prices = [7, 1, 5, 3, 6, 4]
# maxProfit(prices)


# One loop solution O(n)
prices = [7, 1, 5, 3, 6, 4]

# solution accepted with no timeout
def maxProfitOptimized(prices) -> int:
    max_profit = 0
    prices_len = len(prices)
    if len(prices) == 1:
        return 0

    lowest_buy_price = prices[0]
    for index in range(prices_len - 1):
        if prices[index] < lowest_buy_price:
            lowest_buy_price = prices[index]

        profit = prices[index + 1] - lowest_buy_price
        if profit > max_profit:
            max_profit = profit

    return max_profit


maxProfitOptimized(prices)