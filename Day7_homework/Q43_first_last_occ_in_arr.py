def searchRange(nums, target):
        ans = [-1, -1]
        st = 0; end = len(nums) - 1
        idx = -1
        # 1st occ.
        while st <= end:
            mid = st + (end - st) // 2
            if nums[mid] == target:
                idx = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid -1
            else:
                st = mid + 1
        ans[0] = idx

        # 2nd occ.
        idx = -1; st = 0; end = len(nums)-1
        while st <= end:
            mid = st + (end - st) // 2
            if nums[mid] == target:
                idx = mid
                st = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                st = mid + 1
        ans[1] = idx
        return ans
