def findMaxAverage(nums, k):
        n = len(nums)
        ans = float('-inf')
        sum_k = sum(nums[:k])
        max_sum = sum_k
        for i in range(k, n):
            sum_k += nums[i] - nums[i-k]
            max_sum = max(max_sum, sum_k)
        return (max_sum) / k
