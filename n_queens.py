def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        mat = [["."] * n for _ in range(n)]
        def valid(i, j, mat):
            # left
            row = i
            while row >= 0:
                if mat[row][j] == "Q":
                    return False
                row -= 1
            
            # left uper diagonal
            row, col = i, j
            while row >= 0 and col >= 0:
                if mat[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            # right uper diagonal
            row, col = i, j
            while row >= 0 and col < n:
                if mat[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True

        def recursion(row):
            if row == n:
                ans.append(["".join(r) for r in mat])
                return
            for j in range(n):
                if valid(row, j, mat):
                    mat[row][j] = "Q"
                    recursion(row+1)
                    mat[row][j] = "."

        recursion(0)
        return ans
