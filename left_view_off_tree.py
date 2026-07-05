def leftView(self, root):
        # code here
        ans = []
        def view(root, ans, level):
            if root == None:
                return
            if level == len(ans):
                ans.append(root.data)
            
            view(root.left, ans, level+1)
            view(root.right, ans, level+1)
        
        view(root, ans, 0)
        return ans
