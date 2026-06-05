def minimizeMax(nums, p):
        nums.sort()
        def canformpair(maxdiff):
            pair = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i-1] <= maxdiff:
                    pair += 1
                    i += 2
                else:
                    i += 1
            return pair >= p
        
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if canformpair(mid):
                right = mid
            else:
                left = mid+1
        return left
