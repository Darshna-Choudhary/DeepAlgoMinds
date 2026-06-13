def countSetBits(self, n):
        ans = 0
        i = 0
        while (1 << i) <= n:
            cycle = 1 << (i + 1)
            complete_cycles = (n + 1) // cycle
            ans += complete_cycles * (1 << i)
            
            remainder = (n + 1) % cycle
            ans += max(0, remainder - (1 << i))
            
            i += 1
        return ans
