def isPerfectSquare(num):
        if num == 0: return True
        if num == 1 or num == 2: return True
        
        st = 2; end = num-1
        while st <= end:
            mid = st + (end - st) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                end = mid - 1
            else:
                st = mid + 1
        return False
