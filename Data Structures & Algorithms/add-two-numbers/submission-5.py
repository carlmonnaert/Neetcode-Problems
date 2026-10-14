# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = 0
        res = ListNode(None,None)
        ptr = res
        while l1 and l2:
            x1, x2 = l1.val, l2.val
            n = ( x1 + x2 + r) % 10
            r = ( x1 + x2 + r) // 10
            
            node = ListNode(n,None)
            ptr.next = node
            ptr = ptr.next

            l1 = l1.next
            l2 = l2.next
        
        if l1 and r > 0:
            ptr.next = self.addTwoNumbers(ListNode(r, None), l1)

        elif l1 and r == 0:
            ptr.next = l1

        elif l2 and r > 0:
            ptr.next = self.addTwoNumbers(ListNode(r, None), l2)

        elif l2 and r == 0:
            ptr.next = l2
        
        elif r > 0:
            ptr.next = ListNode(r,None)

        res = res.next
        return res