def rowWithMax1s(self, arr):
        # code here
        n = len(arr)
        idx = -1
        prev = 0
        s = 0
        for i in range(n):
            s = sum(arr[i])
            if s > prev:
                idx = i
                prev = s
        return idx
