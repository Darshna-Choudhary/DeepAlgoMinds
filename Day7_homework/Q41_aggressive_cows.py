def checkcow(mid, stalls, k):
        prev = stalls[0]
        k -= 1
        for i in range(1, len(stalls)):
            if (stalls[i] - prev) >= mid:
                k -= 1
                prev = stalls[i]
            if k == 0:
                return True
        return False

def aggressiveCows(stalls, k):
        stalls.sort()
        ans = []
        st = 1; end = stalls[-1] - stalls[0]
        while st <= end:
            mid = st + (end - st) // 2
            if checkcow(mid, stalls, k) == True:
                ans.append(mid)
                st = mid + 1
            else:
                end = mid - 1
        return max(ans)
