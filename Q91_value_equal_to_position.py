def valEqualToPos(self, arr):
        # code here
        n = len(arr)
        ans = []
        for i in range(n):
            if arr[i] == i+1:
                ans.append(arr[i])
        return ans
