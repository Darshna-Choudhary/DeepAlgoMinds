def migratoryBirds(arr):
    dct = {}
    for i in arr:
        dct[i] = dct.get(i, 0) + 1
    ans = min(k for k,v in dct.items() if v==max(dct.values()))
    return ans

arr = [1, 1, 2, 2, 3]
migratoryBirds(arr)
# Output: 1
