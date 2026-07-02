def count(coins, sum):
        # code here 
        n = len(coins)
        def ways(sum, i):
            if i >= n:
                return 0
            if sum == 0:
                return 1
            return ways(sum-coins[i], i) + ways(sum, i+1)
        return ways(sum, 0)
