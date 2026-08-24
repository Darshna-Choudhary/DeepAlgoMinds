# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        return 1 + max(left_h, right_h)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        lefth = self.height(root.left)
        righth = self.height(root.right)
        if abs(lefth - righth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)