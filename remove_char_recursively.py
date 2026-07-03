def removeUtil (self, s):
        #code here
        n = len(s)
        if n < 2:
            return s
        ans = []
        final_ans = ""
        i = 0
        while i < n:
            if i < n-1 and s[i] == s[i+1]:
                curr = s[i]
                while i < n and s[i] == curr:
                    i += 1
            else:
                ans.append(s[i])
                i += 1
            final_ans = "".join(ans)
            if len(final_ans) == len(s):
                return final_ans
        return self.removeUtil(final_ans)
