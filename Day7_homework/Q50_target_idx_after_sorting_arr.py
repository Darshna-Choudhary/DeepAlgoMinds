def targetIndices(nums, target):
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                ans.append(i)
        return ans


def targetIndices(nums, target):
        ans = []
        less_count = 0
        total_count = 0
        for i in nums:
            if i < target:
                less_count += 1
            elif i == target:
                total_count += 1
        for i in range(total_count):
            ans.append(less_count)
            less_count += 1
        return ans
