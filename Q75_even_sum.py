n, m = map(int, input().split())

mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

count = 0
for i in range(n):
    for j in range(i, n):
        for k in  range(m):
            for l in range(k, m):
                s = 0
                for p in range(i, j+1):
                    for q in range(k, l+1):
                        s += mat[p][q]
                if s % 2 == 0:
                    count += 1
print(count)
