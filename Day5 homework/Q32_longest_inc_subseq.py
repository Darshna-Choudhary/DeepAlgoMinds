def findLengthOfLCIS(nums):
        n = len(nums)
        l = 1
        ans = 1
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                l += 1
                ans = max(ans, l)
            else:
                l = 1
        return ans
