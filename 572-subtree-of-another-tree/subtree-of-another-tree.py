# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, root, subroot):
        if root == None and subroot == None:
            return True
        elif root == None or subroot == None:
            return False
        elif root.val != subroot.val:
            return False
        return self.same(root.left, subroot.left) and self.same(root.right, subroot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if self.same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)