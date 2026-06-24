# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root == None:
            return 0
        left_h = self.height(root.left)
        if left_h == -1:
            return -1

        right_h = self.height(root.right)
        if right_h == -1:
            return -1

        if abs(left_h - right_h) > 1:
            return -1
        return 1 + max(left_h, right_h)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.height(root) != -1