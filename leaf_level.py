def check(self, root):
        # code here
        leaf_level = -1
        def dfs(root, level):
            nonlocal leaf_level
            if root == None:
                return True
            if root.left == None and root.right == None:
                if leaf_level == -1:
                    leaf_level = level
                return leaf_level == level
            return dfs(root.left, level+1) and dfs(root.right, level+1)
        return dfs(root, 0)
