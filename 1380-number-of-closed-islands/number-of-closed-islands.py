class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dirc = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()
        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j))
                    grid[i][j] = 1
                    boundary = False
                    while q:
                        x,y = q.popleft()
                        if (x == 0) or (x == row-1) or (y == 0) or (y == col-1):
                            boundary = True
                        for nx, ny in dirc:
                            nx += x
                            ny += y
                            if (0 <= nx < row) and (0 <= ny < col) and (grid[nx][ny] == 0):
                                q.append((nx, ny))
                                grid[nx][ny] = 1
                    if boundary == False:
                        count += 1
        return count