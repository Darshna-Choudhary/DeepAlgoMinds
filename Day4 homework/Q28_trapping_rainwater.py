def trap(height):
        n = len(height)
        left = [0] * n
        left[0] = height[0]
        right = [0] * n
        right[-1] = height[-1]
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])
        
        for i in range(n-2, -1, -1):
            right[i] = max(height[i], right[i+1])
        
        ans = 0
        for i in range(n):
            water = abs(height[i] - min(left[i], right[i]))
            ans += water
        return ans
