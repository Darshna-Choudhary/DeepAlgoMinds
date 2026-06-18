mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ans = []
row = len(mat)
col = len(mat[0])
for j in range(col):
  for i in range(row-1, -1, -1):
    ans.append(mat[i][j])

p = 0
for i in range(row):
  for j in range(col):
    mat[i][j] = ans[p]
    p += 1
mat
