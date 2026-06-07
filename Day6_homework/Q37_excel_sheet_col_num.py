def titleToNumber(columnTitle):
        ans = 0
        for i in columnTitle:
            ans = ans * 26 + (ord(i) - ord('A') + 1)
        return ans
