class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        k = len(s3)
        if n + m != k:
            return False
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for i in range(m+1):
            for j in range(n+1):
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[-1][-1]