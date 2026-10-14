# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the cutting point (start of right part)
        fast, slow = head, head
        while fast:
            fast = fast.next
            slow = slow.next

            if fast:
                fast = fast.next

        start_right = slow
        left = head
        right = slow

        # Reverse the right part
        rev = None
        to_rev = right
        while to_rev:
            ptr = to_rev
            tail = ptr.next
            ptr.next = rev
            rev = ptr
            to_rev = tail

        # Separating the two lists:
        while left.next != right:
            left = left.next
        left.next = None

        # Alternating reconstruction
        left = head
        right = rev
        while left:
            tail = left.next
            left.next = right
            left = left.next
            right = tail
            