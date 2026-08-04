class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        bestbuy = prices[0]
        profit = 0
        for i in range(1, n):
            profit = max(profit, prices[i]-bestbuy)
            bestbuy = min(bestbuy, prices[i])
        return profit