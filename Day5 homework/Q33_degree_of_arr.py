def findShortestSubArray(nums):
        dct = Counter(nums)
        left = {}
        right = {}
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i
        degree = max(dct.values())
        ans = float('inf')
        for i in dct.keys():
            if dct[i] == degree:
                ans = min(ans, right[i] - left[i] + 1)
        return ans
