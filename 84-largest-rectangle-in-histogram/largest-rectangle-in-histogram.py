class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = [-1]
        heights.append(0)
        n = len(heights)
        for i in range(n):
            while stk[-1] != -1 and heights[stk[-1]] > heights[i]:
                h = heights[stk.pop()]
                w = i - stk[-1] - 1
                area = h * w
                if area > ans:
                    ans = area
            stk.append(i)
        heights.pop()
        return ans