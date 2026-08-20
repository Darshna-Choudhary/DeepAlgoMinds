# Brute force
def countTriplets(arr, l, r):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                s = arr[i] + arr[j] + arr[k]
                if s >= l and s <= r:
                    count += 1
    return count
# Optimized
def countTriplets(arr, l, r):
    arr.sort()
    def count_sum(x):
        n = len(arr)
        count = 0
        for k in range(n-2):
            i = k+1
            j = n-1
            while i < j:
                s = arr[k] + arr[i] + arr[j]
                if s <= x:
                    count += j-i
                    i += 1
                else:
                    j -= 1
        return count
    return count_sum(r) - count_sum(l-1)
