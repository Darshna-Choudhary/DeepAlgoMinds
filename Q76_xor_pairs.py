import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	freq = {}
	for i in range(1, n+1):
		val = arr[i-1] ^ i
		freq[val] = freq.get(val, 0) + 1
	ans = 0
	for i in freq.values():
		ans += (i * (i - 1)) // 2
	print(ans)
