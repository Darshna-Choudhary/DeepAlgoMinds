def binarySearch(arr, k):
        st = 0
        end = len(arr)-1
        while st <= end:
            mid = st + (end-st) // 2
            if arr[mid] == k:
                return True
            elif arr[mid] < k:
                st = mid + 1
            else:
                end = mid - 1
        return False
