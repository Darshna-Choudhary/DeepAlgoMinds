# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, st, end):
            if root == None:
                return True
            if root.val < st or root.val > end:
                return False
            a = check(root.left, st, root.val -1)
            b = check(root.right, root.val+1, end)
            return a and b
        return check(root, float('-inf'), float('inf'))