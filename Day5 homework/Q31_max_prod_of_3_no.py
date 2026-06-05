def maximumProduct(nums):
        n = len(nums)
        nums.sort()
        m1 = nums[-1] * nums[-2] * nums[-3]
        m2 = nums[0] * nums[1] * nums[-1]
        return max(m1, m2)
