def miniMaxSum(arr):
    min_val = float("inf")
    max_val = float("-inf")
    sum = 0
    for i in arr:
        min_val = min(min_val,i)
        max_val = max(max_val, i)
        sum += i
    print((sum-max_val), (sum-min_val))

arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)
# Output: 10 14
