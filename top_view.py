def topView(self, root):
        # code here
        if root is None:
            return []

        ans = []
    
        q = deque([(root, 0)])
        dct = {}
        
        while q:
            node, hd = q.popleft()
            if not hd in dct:
                dct[hd] = node.data
            if node.left:
                q.append((node.left, hd-1))
            if node.right:
                q.append((node.right, hd+1))
        
        for key in sorted(dct.keys()):
            ans.append(dct[key])
        return ans
