def pairwiseSwap(head):
    if head is None or head.next is None:
        return head
    first = head
    second = temp = head.next
    nxt = head.next.next
    prev = Node(None)
    while first:
        if second is None:
            prev.next = first
            return temp
        prev.next = second
        second.next = first
        first.next = nxt
        prev = first
        first = nxt
        if first is None:
            return temp
        second = first.next
        if second is None:
            prev.next = first
            return temp
        nxt = second.next
        return temp
