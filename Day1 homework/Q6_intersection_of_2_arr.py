def intersection(nums1, nums2):
    seen = set(nums2)
    ans = []
    for i in nums1:
        if i in seen:
            ans.append(i)
    return list(set(ans))

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))
# Output: [2]
