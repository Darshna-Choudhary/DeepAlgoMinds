class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        dct = {'(' : ')', '[' : ']', '{' : '}'}
        for b in s:
            if b in dct.keys():
                stk.append(b)
            else:
                if stk and dct[stk[-1]] == b:
                    stk.pop()
                else:
                    return False
        return False if stk else True