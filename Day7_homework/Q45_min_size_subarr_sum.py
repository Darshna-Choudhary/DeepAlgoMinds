def minSubArrayLen(target, nums):
        n = len(nums)
        l = float('inf')
        left = 0
        s = 0
        for i in range(n):
            s += nums[i]
            while s >= target:
                l = min(l, i - left + 1)
                s = s - nums[left]
                left += 1
        return l if l != float('inf') else 0
