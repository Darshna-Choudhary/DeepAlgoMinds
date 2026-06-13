t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count0 = 0
    count1 = 0
    for i in arr:
        if i % 2 == 0:
            count0 += 1
        else:
            count1 += 1

    if count0 % 2 == 1 and count1 % 2 == 1:
        print(0)
    else:
        print(1)
