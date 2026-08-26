# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        def inOrder(root):
            nonlocal count, ans
            if root is None or ans is not None:
                return
            inOrder(root.left)
            count += 1
            if count == k:
                ans = root.val
                return
            inOrder(root.right)
        inOrder(root)
        return ans