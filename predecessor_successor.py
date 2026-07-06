def findPreSuc(self, root, key):
        # code here
        ans = [None, None]
        def inorder(root):
            if root is None:
                return
            
            inorder(root.left)
            if root.data < key:
                if ans[0] is None or ans[0].data < root.data:
                    ans[0] = root
            elif root.data > key:
                if ans[1] is None or ans[1].data > root.data:
                    ans[1] = root
            
            inorder(root.right)
        inorder(root)
        return ans
