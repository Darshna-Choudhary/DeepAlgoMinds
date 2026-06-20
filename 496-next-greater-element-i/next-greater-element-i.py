class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stk = []
        dct = {}
        n = len(nums2)
        for i in range(n):
            while stk and nums2[stk[-1]] < nums2[i]:
                dct[nums2[stk[-1]]] = nums2[i]
                stk.pop()
            else:
                dct[nums2[i]] = -1
            stk.append(i)
        
        for i in nums1:
            ans.append(dct[i])
        return ans