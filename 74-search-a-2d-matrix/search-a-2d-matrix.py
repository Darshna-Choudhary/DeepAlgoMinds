class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        st = 0; end = row * col - 1
        while st <= end:
            mid = st + (end - st) // 2
            if matrix[mid // col][mid % col] == target:
                return True
            elif matrix[mid // col][mid % col] > target:
                end = mid - 1
            else:
                st = mid + 1
        return False