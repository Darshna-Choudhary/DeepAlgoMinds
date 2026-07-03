def findAllPossiblePaths(self, n : int, m : int, mat : List[List[int]]) -> List[List[int]]:
        # code here
        ans = []
        def find_path(i, j, path):
            if i >= n or j >= m:
                return
            
            path.append(mat[i][j])
            
            if i == n-1 and j == m-1:
                ans.append(path.copy())
                path.pop()
                return
        
            find_path(i+1, j, path)
            find_path(i, j+1, path)
            path.pop()
        
        find_path(0, 0, [])
        return ans
