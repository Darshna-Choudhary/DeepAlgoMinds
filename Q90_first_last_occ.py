def find(self, arr, target):
        # code here
        n = len(arr)
        ans = [-1, -1]
        st = 0
        end = n-1
        
        while st <= end:
            mid = st + (end - st) // 2
            if arr[mid] == target:
                ans[0] = mid
                end = mid - 1
            elif arr[mid] > target:
                end = mid - 1
            else:
                st = mid + 1
        
        st = 0; end = n-1
        while st <= end:
            mid = st + (end - st) // 2
            if arr[mid] == target:
                ans[1] = mid
                st = mid + 1
            elif target < arr[mid]:
                end = mid - 1
            else:
                st = mid + 1
        return ans
