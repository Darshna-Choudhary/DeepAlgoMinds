# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root == None:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        curr = left_h + right_h + 2
        left_d = self.diameterOfBinaryTree(root.left)
        right_d = self.diameterOfBinaryTree(root.right)
        return max(curr, left_d, right_d)