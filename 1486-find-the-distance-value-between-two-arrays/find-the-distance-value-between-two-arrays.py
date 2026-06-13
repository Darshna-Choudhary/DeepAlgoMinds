class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n = len(arr1)
        m = len(arr2)
        count = 0
        flag = False
        for i in range(n):
            for j in range(m):
                if abs(arr1[i] - arr2[j]) > d:
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                count += 1
        return count