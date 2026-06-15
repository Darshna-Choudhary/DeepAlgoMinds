mat = [[1, 2, 1, 4, 8], [3, 7, 8, 5, 1], [8, 7, 7, 3, 1], [8, 1, 2, 7, 9]]

n = len(mat)
m = len(mat[0])

dct = {}
for i in range(m):
  dct[mat[0][i]] = 1

for i in range(1, n):
  for j in range(m):
    if mat[i][j] in dct.keys() and dct[mat[i][j]] == i:
      dct[mat[i][j]] = i + 1
      if i == n-1:
        print(mat[i][j], end = " ")
