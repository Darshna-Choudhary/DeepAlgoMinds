class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []
        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                val = stk.pop()
                ans[val] = i - val
            stk.append(i)
        return ans