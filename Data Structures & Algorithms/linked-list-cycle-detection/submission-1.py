# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        p1 = head
        p2 = head.next
        while p1 != p2 and p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if p2 is None:
                break
            p2 = p2.next
        
        if p1 == p2:
            return True
        
        elif p1 is None or p2 is None:
            return False