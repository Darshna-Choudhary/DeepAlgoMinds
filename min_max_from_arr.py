def getMinMax(self, arr):
        # code here
        maxn = float('-inf')
        minn = float('inf')
        n = len(arr)
        def get_num(i):
            nonlocal maxn, minn
            if i >= n:
                return [minn, maxn]
            if arr[i] > maxn:
                maxn = arr[i]
            if arr[i] < minn:
                minn = arr[i]
            return get_num(i+1)
        return get_num(0)
