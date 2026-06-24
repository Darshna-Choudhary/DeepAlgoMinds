# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.check(p.left, q.right) and self.check(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        return self.check(root.left, root.right)