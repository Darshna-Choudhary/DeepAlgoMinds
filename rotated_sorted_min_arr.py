def findMin(arr):
        st = 0
        end = len(arr)-1
        while st < end:
            mid = st + (end - st) // 2
            if arr[mid] > arr[end]:
                st = mid + 1
            else:
                end = mid
        return arr[st]
