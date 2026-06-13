def countSwaps(a):
    # Write your code here
    count = 0
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                count += 1
    print(f"Array is sorted in {count} swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
