def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        s = 0
        for i in range(1, n+1):
            s += i
            if s > n:
                return i - 1
        return i - 1


def arrangeCoins(self, n: int) -> int:
        st = 1; end = n
        while st <= end:
            mid = st + (end - st) // 2
            coins_needed = mid * (mid + 1) // 2
            if coins_needed == n:
                return mid
            elif coins_needed < n:
                st = mid + 1
            else:
                end = mid - 1
        return end
