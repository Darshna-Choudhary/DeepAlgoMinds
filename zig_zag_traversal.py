def zigZagTraversal(self, root):
        # code here
        q = deque([root])
        ans = []
        count = 0
        while q:
            size = len(q)
            level = []
            count += 1
            stk = []
            for _ in range(size):
                node = q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if count%2 == 0:
                level.reverse()
            ans.extend(level)
        
        return ans
