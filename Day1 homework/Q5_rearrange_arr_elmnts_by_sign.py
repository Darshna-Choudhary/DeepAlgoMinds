def rearrangeArray(nums):
    l = len(nums)
    p, n = 0, 1
    ans = [0] * (l)
    for i in range(l):
        if nums[i] > 0:
            ans[p] = nums[i]
            p += 2
        else:
            ans[n] = nums[i]
            n += 2
    return ans

nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))
# Output: [3,-2,1,-5,2,-4]
