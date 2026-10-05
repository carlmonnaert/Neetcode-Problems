# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        head = ListNode(min(l1.val, l2.val), None)
        
        if l1.val == head.val:
            l1 = l1.next
        else:
            l2 = l2.next

        ptr = head
        while l1 and l2:
            v1, v2 = l1.val, l2.val
            if v1 <= v2:
                ptr.next = ListNode(v1,None)
                l1 = l1.next
            else:
                ptr.next = ListNode(v2,None)
                l2 = l2.next
            ptr = ptr.next
        if l1 is None:
            ptr.next = l2
        else:
            ptr.next = l1
        return head