class Solution:
    def solve(self, board: list[list[str]]) -> None:
        row = len(board)
        col = len(board[0])
        dirc = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()

        for i in range(row):
            if board[i][0] == "O":
                board[i][0] = "1"
                q.append((i, 0))
            if board[i][col-1] == "O":
                board[i][col-1] = "1"
                q.append((i, col-1))
            for j in range(col):
                if board[0][j] == "O":
                    board[0][j] = "1"
                    q.append((0, j))
                if board[row-1][j] == "O":
                    board[row-1][j] = "1"
                    q.append((row-1, j))
        
        while q:
            x,y = q.popleft()
            for nx, ny in dirc:
                nx += x
                ny += y
                if (0 <= nx < row) and (0 <= ny < col) and board[nx][ny] == "O":
                    board[nx][ny] = "1"
                    q.append((nx, ny))
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "1":
                    board[i][j] = "O"
        return board