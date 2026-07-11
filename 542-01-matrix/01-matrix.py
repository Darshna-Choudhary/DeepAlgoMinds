class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1
        while q:
            x, y = q.popleft()
            for nx, ny in dirc:
                nx += x
                ny += y
                if (0 <= nx < m) and (0 <= ny < n) and (mat[nx][ny] == -1):
                    mat[nx][ny] = mat[x][y]+1
                    q.append((nx, ny))
        return mat