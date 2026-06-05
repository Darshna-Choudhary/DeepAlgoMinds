def subarraySum(nums, k):
        prefix_sum = 0
        count = 0
        dct = {}
        dct[0] = 1
        for i in nums:
            prefix_sum += i
            if prefix_sum-k in dct.keys():
                count += dct[prefix_sum-k]
            dct[prefix_sum] = dct.get(prefix_sum, 0) + 1
        return count
