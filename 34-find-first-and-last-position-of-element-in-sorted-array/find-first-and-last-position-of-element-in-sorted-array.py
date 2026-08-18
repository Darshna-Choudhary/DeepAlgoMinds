class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        st = 0
        end = len(nums) - 1
        i = -1
        while st <= end:
            mid = st + (end - st) // 2
            if nums[mid] == target:
                i = mid
                end = mid - 1
            elif nums[mid] < target:
                st = mid + 1
            else:
                end = mid - 1
        ans[0] = i
        i = -1
        st = 0
        end = len(nums)-1
        while st <= end:
            mid = st + (end - st) // 2
            if nums[mid] == target:
                i = mid
                st = mid + 1
            elif nums[mid] < target:
                st = mid + 1
            else:
                end = mid - 1
        ans[1] = i
        return ans