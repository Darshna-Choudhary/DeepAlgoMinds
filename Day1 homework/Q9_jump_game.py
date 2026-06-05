def canJump(nums):
    n = len(nums)
    max_reach = 0
    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, nums[i]+i)
    return True

nums = [2,3,1,1,4]
print(canJump(nums))
# Output: true
