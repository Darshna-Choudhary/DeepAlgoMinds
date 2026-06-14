def median(self, mat):
        # code here 
        rows = len(mat)
        cols = len(mat[0])
        count = 0
        ans = -1
        minheap = []
        for i in range(rows):
            heapq.heappush(minheap, [mat[i][0], i, 0])
        
        mid_idx = (rows * cols) // 2
        while count <= mid_idx:
            val, row, col = heapq.heappop(minheap)
            ans = val
            count += 1
            if col + 1 < cols:
                heapq.heappush(minheap, [mat[row][col+1], row, col+1])
        return ans
