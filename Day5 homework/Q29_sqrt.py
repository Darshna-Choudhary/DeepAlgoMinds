def mySqrt(x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        st = 1
        end = x
        mid = -1
        while st <= end:
            mid = st + (end - st) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                st = mid + 1
            else:
                end = mid - 1
        return round(end)
