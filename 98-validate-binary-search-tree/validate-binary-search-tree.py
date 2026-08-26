# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, st, end):
            if root is None:
                return True
            if (root.val >= end) or (root.val <= st):
                return False
            return check(root.left, st, root.val) and check(root.right, root.val, end)
        return check(root, float('-inf'), float('inf'))