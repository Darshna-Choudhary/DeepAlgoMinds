class Solution:
    def isValid(self, s: str) -> bool:
        dct = {'(' : ')', '{' : '}', '[' : ']'}
        stk = []
        for i in s:
            if i in dct.keys():
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    if dct[stk[-1]] == i:
                        stk.pop()
                    else:
                        return False
        return True if not stk else False