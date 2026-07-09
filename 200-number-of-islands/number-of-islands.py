class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            grid[i][j] = "0"
            while q:
                x, y = q.popleft()
                for nx, ny in dirc:
                    nx += x
                    ny += y
                    if (0 <= nx < rows) and (0 <= ny < cols) and (grid[nx][ny] == "1"):
                        grid[nx][ny] = "0"
                        q.append((nx, ny))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1                
                    bfs(i, j)
                    
        return islands