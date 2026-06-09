def missingNumber(nums):
        n = len(nums)
        arr_sum = sum(nums)
        actual = n * (n+1) // 2
        return actual - arr_sum
