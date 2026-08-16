def countOnes(arr):
        st = 0
        end = len(arr)-1
        while st <= end:
            mid = st + (end - st) // 2
            if arr[mid] == 1:
                st = mid + 1
            else:
                end = mid - 1
        return st
