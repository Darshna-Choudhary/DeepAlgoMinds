def commonElements(a, b, c):
        i = j = k =0
        ans = []
        prev = None
        while i < len(a) and j < len(b) and k < len(c):
            if a[i] == b[j] == c[k]:
                if prev != a[i]:
                    ans.append(a[i])
                    prev = a[i]
                i += 1; j += 1; k += 1
            else:
                if a[i] < b[j]:
                    i += 1
                elif b[j] < c[k]:
                    j += 1
                else:
                    k += 1
        return ans
