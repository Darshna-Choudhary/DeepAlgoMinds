class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp = [[0] * col for _ in range(row)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        return dp[row-1][col-1]