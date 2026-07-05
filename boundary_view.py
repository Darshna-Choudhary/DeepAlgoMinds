def isleaf(self, root):
        return root.left is None and root.right is None

def left_boundary(self, root, ans):
        curr = root.left
        
        while curr:
            if not self.isleaf(curr):
                ans.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        
def leaf_nodes(self, root, ans):
        if root is None:
            return
        if self.isleaf(root):
            ans.append(root.data)
            return
        
        self.leaf_nodes(root.left, ans)
        self.leaf_nodes(root.right, ans)
    
def right_boundary(self, root, ans):
        curr = root.right
        temp = []
        
        while curr:
            if not self.isleaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        
        while temp:
            ans.append(temp.pop())
        
    def boundaryTraversal(self, root):
        # code here
        if root is None:
            return []
        if self.isleaf(root):
            return [root.data]
        
        ans = [root.data]
        self.left_boundary(root, ans)
        self.leaf_nodes(root, ans)
        self.right_boundary(root, ans)
        
        return ans
