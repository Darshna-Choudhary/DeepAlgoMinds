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
# ------------------------------------------------------------------------
def pairwiseSwap(head):
    if head is None or head.next is None:
        return head
    node = Node(Node)
    node.next = head
    prev = node
        
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
    return node.next
