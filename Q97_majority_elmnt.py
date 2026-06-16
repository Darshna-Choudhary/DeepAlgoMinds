def majorityElement(self, arr):
        #code here
        dct = {}
        for i in arr:
            dct[i] = dct.get(i, 0) + 1
        
        for key, val in dct.items():
            if val > len(arr) // 2:
                return key
        return -1
