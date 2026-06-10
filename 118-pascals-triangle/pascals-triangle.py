class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        arr = [[1], [1,1]]
        prev = arr[-1]
        for i in range(2, numRows):
            ans = [1]
            for j in range(len(prev)-1):
                ans.append(prev[j] + prev[j+1])
            ans.append(1)
            arr.append(ans)
            prev = ans
        return arr