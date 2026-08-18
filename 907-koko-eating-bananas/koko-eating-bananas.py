class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        st = 1
        end = max(piles)
        while st < end:
            hrs = 0
            mid = st + (end - st) // 2
            for p in piles:
                hrs += (p + mid - 1) // mid
            if hrs <= h:
                end = mid
            else:
                st = mid + 1
        return st