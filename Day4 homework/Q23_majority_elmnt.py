def majorityElement(nums):
        n = len(nums)
        dct = Counter(nums)
        
        for k, v in dct.items():
            if v > (n//2):
                return k
