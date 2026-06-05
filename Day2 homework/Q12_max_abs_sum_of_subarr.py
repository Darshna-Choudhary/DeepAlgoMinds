def maxAbsoluteSum(nums):
    min_prefix_sum = 0
    max_prefix_sum = 0
    prefix_sum = 0
    for i in nums:
        prefix_sum += i
        max_prefix_sum = max(max_prefix_sum, prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefix_sum)
    return max_prefix_sum - min_prefix_sum

nums = [1,-3,2,3,-4]
print(maxAbsoluteSum(nums))
# Output: 5
