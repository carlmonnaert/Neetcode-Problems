# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        clean_lists = []
        for l in lists:
            if l:
                clean_lists.append(l)
        
        heap = [ (l.val, i, l) for i, l in enumerate(clean_lists) ]
        heapq.heapify(heap)

        res = ListNode(None, None)
        h = res
        while heap:
            val, i, node = heapq.heappop(heap)
            new_node = ListNode(val, None)
            res.next = new_node
            res = res.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return h.next
