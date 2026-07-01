def lcs(self, s1, s2):
    m = len(s1)
    n = len(s2)
    def subseq(s1, s2, m, n):
        if m < 0 or n < 0:
            return 0
        if s1[m] == s2[n]:
            return 1 + subseq(s1, s2, m-1, n-1)
        return max(subseq(s1, s2, m-1, n), subseq(s1, s2, m, n-1))
    return subseq(s1, s2, m-1, n-1)

def lcs(self, s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * n for _ in range(m)]
        
    def subseq(i, j):
        if i == m or j == n:
            return 0
        if dp[i][j] != 0:
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] = 1 + subseq(i+1, j+1)
        else:
            dp[i][j] = max(subseq(i, j+1), subseq(i+1, j))
        return dp[i][j]
    return subseq(0, 0)
