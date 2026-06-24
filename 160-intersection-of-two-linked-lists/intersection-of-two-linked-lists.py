# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return "No intersection"

        len1 = len2 = 0
        a = headA
        b = headB
        while a:
            len1 += 1
            a = a.next
        
        while b:
            len2 += 1
            b = b.next
        
        diff = abs(len1 - len2)
        temp1 = headA
        temp2 = headB
        if len1 > len2:
            for i in range(diff):
                temp1 = temp1.next
            while temp1 != temp2:
                temp1 = temp1.next
                temp2 = temp2.next
            return temp1
        else:
            for i in range(diff):
                temp2 = temp2.next
            while temp1 != temp2:
                temp1 = temp1.next
                temp2 = temp2.next
            return temp2
        return headA