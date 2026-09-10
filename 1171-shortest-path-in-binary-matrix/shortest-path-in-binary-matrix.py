class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
    
        path = 1
        dirc = [(0,1), (1,0), (0,-1), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
        q = deque()
        q.append((0,0))
        grid[0][0] = 1
        while q:
            p = len(q)
            for _ in range(p):
                x,y = q.popleft()
                if x == n-1 and y == n-1:
                    return path
                for nx, ny in dirc:
                    nx += x
                    ny += y
                    if (0 <= nx < n) and (0 <= ny < n) and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))
            path += 1
        return -1