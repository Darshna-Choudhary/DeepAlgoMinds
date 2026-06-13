N = int(input())
frequencies = list(map(int, input().split()))
K = int(input())
keySizes = list(map(int, input().split()))

frequencies.sort(reverse=True)
freq = []
for i in range(K):
    for j in range(1, keySizes[i]+1):
        freq.append(j)
freq.sort()
ans = 0
if len(freq) < len(frequencies):
    print(-1)
else:
    for f, c in zip(frequencies, freq):
        ans += f * c
    print(ans)
