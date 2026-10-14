"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h_old_new = {None: None}
        node = head

        while node:
            new_node = Node(node.val, None, None)
            h_old_new[node] = new_node            
            node = node.next

        node = head
        while node:
            h_old_new[node].next = h_old_new[node.next]
            h_old_new[node].random = h_old_new[node.random]
            node = node.next
        return h_old_new[head]