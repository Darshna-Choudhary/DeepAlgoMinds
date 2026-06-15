class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        st = 0
        end = n-1
        while st <= end:
            mid = st + (end - st) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[st]:
                if nums[st] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    st = mid + 1
                else:
                     end = mid - 1
        return -1