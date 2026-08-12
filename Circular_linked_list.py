 def isCircular(head):
        if head is None:
            return True
        slow = head
        fast = head
        while slow and fast:
            if fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
