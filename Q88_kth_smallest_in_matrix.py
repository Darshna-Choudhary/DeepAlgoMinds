def kthSmallest(self, mat, k):
        # code here
        n = len(mat)
        st = mat[0][0]
        end = mat[n-1][n-1]
        while st < end:
            mid = st + (end - st) // 2
            row = n-1
            col = 0
            count = 0
            while row >= 0 and col < n:
                if mat[row][col] <= mid:
                    count += (row + 1)
                    col += 1
                else:
                    row -= 1
            if count < k:
                st = mid + 1
            else:
                end = mid
        return st
