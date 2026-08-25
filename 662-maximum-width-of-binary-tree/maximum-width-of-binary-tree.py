# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque()
        q.append([root, 0])
        width = 0
        while q:
            n = len(q)
            n1, first_idx = q[0]
            for _ in range(n):
                node, idx = q.popleft()
                if node.left:
                    q.append([node.left, 2*idx])
                if node.right:
                    q.append([node.right, 2*idx+1])
                width = max(width, idx - first_idx + 1)
        return width