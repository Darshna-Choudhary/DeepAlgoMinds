class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dirc = [(0,1), (1,0), (0,-1), (-1,0)]
        island = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    q = deque()
                    island += 1
                    q.append((i,j))
                    grid[i][j] = "0"
                    while q:
                        x, y = q.popleft()
                        for nx, ny in dirc:
                            nx += x
                            ny += y
                            if (0 <= nx < row) and (0 <= ny < col) and grid[nx][ny] == "1":
                                grid[nx][ny] = "0"
                                q.append((nx,ny))
        return island