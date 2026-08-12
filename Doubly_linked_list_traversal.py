def displayList(head):
        f = []
        b = []
        curr = head
        while curr:
            f.append(curr.data)
            if curr.next is None:
                break
            curr = curr.next
            
        while curr:
            b.append(curr.data)
            curr = curr.prev
            
        return [f, b]
