class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirc = [(0,1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0
        rot = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rot.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while rot and fresh > 0:
            minutes += 1 
            for _ in range(len(rot)):
                x, y = rot.popleft()
                for nx, ny in dirc:
                    nx += x
                    ny += y
                    if (0 <= nx < rows) and (0 <= ny < cols) and (grid[nx][ny] == 1):
                        fresh -= 1
                        grid[nx][ny] = 2
                        rot.append((nx, ny))
        return minutes if fresh == 0 else -1