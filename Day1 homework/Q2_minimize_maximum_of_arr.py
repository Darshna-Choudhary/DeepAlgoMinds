def minimizeArrayValue(nums):
    prefix_sum = 0
    ans = 0
    for i, num in enumerate(nums):
        prefix_sum += num
        ans = max(ans, ceil(prefix_sum / (i+1)))
    return ans

nums = [3,7,1,6]
print(minimizeArrayValue(nums))
# Output: 5 ([5,5,2,5])
