def sortedListToBST(self, head):
        #code here
        if head == None:
            return None
        if head.next == None:
            return TNode(head.data)
        
        slow = head
        fast = head
        prev = LNode(None)
        prev.next = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev = prev.next
        prev.next = None
        
        node = TNode(slow.data)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        
        return node
