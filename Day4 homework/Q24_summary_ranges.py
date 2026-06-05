def summaryRanges(nums):
        if not nums:
            return []
        ans = []
        st = end = 0
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                end += 1
            else:
                if st != end:
                    s = str(nums[st]) + "->" + str(nums[end])
                    ans.append(s)
                    st = i+1
                    end = i+1
                else:
                    ans.append(str(nums[st]))
                    st = i+1
                    end = i+1
        if st != end:
            s = str(nums[st]) + "->" + str(nums[end])
            ans.append(s)
        else:
            ans.append(str(nums[st]))
        return ans
