def missingNumber(nums):
        arr_sum = sum(nums)
        n = len(nums)
        actual_sum = 0
        for i in range(1, n+1):
            actual_sum += i
        return actual_sum - arr_sum
