def maxProfit(prices):
        max_profit = float('-inf')
        best_buy = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-best_buy)
            if prices[i] <= best_buy:
                best_buy = prices[i]
        return max_profit if max_profit > 0 else 0
