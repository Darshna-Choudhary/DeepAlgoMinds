def fit(nums, k, mid):
        count = 1
        s = 0
        for i in range(len(nums)):
            if s + nums[i] <= mid:
                s += nums[i]        
            else:
                count += 1
                s = nums[i]
        return count <= k
            
def splitArray(nums, k):
        ans = 0
        st = max(nums); end = sum(nums)
        while st <= end:
            mid = st + (end - st) // 2
            if fit(nums, k, mid):
                ans = mid
                end = mid - 1
            else:
                st = mid + 1
        return ans
