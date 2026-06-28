# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None
        ans = []
        curr_count = 0
        max_count = 0
        def inorder(root):
            nonlocal prev, ans, curr_count, max_count
            if root == None:
                return
            inorder(root.left)
            if prev != None and root.val == prev.val:
                curr_count += 1
            else: 
                curr_count = 1
            if curr_count > max_count:
                ans = [root.val]
                max_count = curr_count
            elif curr_count == max_count:
                ans.append(root.val)
            prev = root
            inorder(root.right)
        inorder(root)
        return ans