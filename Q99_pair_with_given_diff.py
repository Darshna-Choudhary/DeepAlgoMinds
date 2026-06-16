def findPair(self, arr: List[int], x: int) -> int:
        # code here
        n = len(arr)
        arr.sort()
        i = 0; j = 1
        while i < n and j < n:
            diff = arr[j] - arr[i]
            if diff == x and i != j:
                return True
            elif diff < x:
                j += 1
            else:
                i += 1
        return False
