def powerSet(s):
        # Code here
        ans = []
        n = len(s)
        for i in range(2**n):
            temp = ""
            pos = 0
            idx = i
            while idx > 0:
                if idx & 1:
                    temp += s[pos]
                idx = idx >> 1
                pos += 1
            ans.append(temp)
        ans.sort()
        return ans
