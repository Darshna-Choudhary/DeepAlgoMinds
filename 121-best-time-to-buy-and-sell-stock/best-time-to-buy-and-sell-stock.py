class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        bestbuy = prices[0]
        profit = 0
        for i in range(1, n):
            if prices[i]-bestbuy > profit:
                profit = prices[i]-bestbuy
            elif prices[i] < bestbuy:
                bestbuy = prices[i]
        return profit