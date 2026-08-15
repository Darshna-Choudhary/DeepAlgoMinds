def floorSqrt(n):
        st = 0
        end = n
        while st <= end:
            mid = st + (end-st) // 2
            if mid * mid == n:
                return mid
            elif mid * mid < n:
                st = mid + 1
            else:
                end = mid - 1
        return round(end)
