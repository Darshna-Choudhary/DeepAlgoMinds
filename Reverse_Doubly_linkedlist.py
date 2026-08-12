def reverse(head):
        curr = head
        p = curr.prev
        while curr:
            nxt = curr.next
            curr.next = p
            curr.prev = nxt
            p = curr
            curr = nxt
        return p
