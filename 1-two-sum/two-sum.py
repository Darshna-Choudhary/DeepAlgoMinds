class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        dct = {}
        for i in range(n):
            dct[i] = target - nums[i]
        # print(dct)
        
        for k, v in dct.items():
            if v in nums and nums.index(v) != k:
                ans[0] = k
                ans[1] = nums.index(v)
        return ans