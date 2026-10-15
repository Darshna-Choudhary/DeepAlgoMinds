def count(coins, sum):
        n = len(coins)
        dp = [0] * (sum+1)
        dp[0] = 1
        for c in coins:
            for amount in range(c, sum+1):
                dp[amount] += dp[amount-c]
        return dp[sum]
