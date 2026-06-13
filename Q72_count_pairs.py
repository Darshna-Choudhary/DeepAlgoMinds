from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())    # no. of integers
    arr = list(map(int, input().split()))
    total = (n*(n-1))//2

    freq = defaultdict(int)
    for i in arr:
        if i != 0:
            freq[i.bit_length() - 1] += 1
    
    bad = 0
    for val in freq.values():
        bad += val*(val-1) // 2
    print(total - bad)
