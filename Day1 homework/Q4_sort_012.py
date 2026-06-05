def sortColors(nums):
    n = len(nums)
    st, mid, end = 0, 0, n-1
    while mid <= end:
        if nums[mid] == 0:
            nums[st], nums[mid] = nums[mid], nums[st]
            mid += 1
            st += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[end] = nums[end], nums[mid]
            end -= 1
    return nums

nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
# Output: [0, 0, 1, 1, 2, 2]
