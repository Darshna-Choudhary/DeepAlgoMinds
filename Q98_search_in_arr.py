def findStepKeyIndex(self, arr, k, x):
        # code here
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
