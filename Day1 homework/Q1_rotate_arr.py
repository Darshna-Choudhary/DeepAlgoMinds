def rotate(nums, k):
    k = k % len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums,k))
# Output: [5, 6, 7, 1, 2, 3, 4]
