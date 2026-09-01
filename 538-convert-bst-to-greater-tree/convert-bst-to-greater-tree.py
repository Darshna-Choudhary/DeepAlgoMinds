# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        if not root.left and not root.right:
            return root
        stk =[]
        curr = root
        curr_sum = 0
        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.right
            curr = stk.pop()
            curr_sum += curr.val
            curr.val = curr_sum
            curr = curr.left
        return root