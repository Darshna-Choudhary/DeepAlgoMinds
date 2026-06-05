def singleNumber(nums):
        k = 0
        for i in nums:
            k = k^i
        return k
