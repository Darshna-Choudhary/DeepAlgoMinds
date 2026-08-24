class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Brute force (O(n))
        # n = len(nums)
        # if n == 1:
        #     return 0
        # if nums[0] > nums[1]:
        #     return 0
        # if nums[n-1] > nums[n-2]:
        #     return n-1
        # for i in range(1, n-1):
        #     if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i

        # Binary search (O(log n))
        st = 0
        end = len(nums)-1
        while st < end:
            mid = st + (end - st) // 2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                st = mid + 1
        return st
