class Solution:
    def decodeString(self, s: str) -> str:
        n = 0
        stk = []
        temp = ""
        for i in s:
            if i.isdigit():
                n = n * 10 + int(i)
            elif i == '[':
                stk.append(temp)
                stk.append(n)
                temp = ""
                n = 0
            elif i == ']':
                prev_n = stk.pop()
                prev_temp = stk.pop()
                temp = prev_temp + prev_n * temp
            else:
                temp += i
        return temp