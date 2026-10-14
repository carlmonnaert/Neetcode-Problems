# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        left = head
        prev = ListNode(None, head)
        count = 0
        
        for i in range(n):
            right = right.next
        
        while right:
            right = right.next
            left = left.next
            prev = prev.next        
        
        if prev.val:
            prev.next = left.next
            return head
            
        return left.next