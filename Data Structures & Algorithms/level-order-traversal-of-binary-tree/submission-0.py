# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = []
        h = {}
       
        def bfs(node, level):
            if node:
                if level in h:
                    h[level].append(node.val)
                else:
                    h[level] = [node.val]
                bfs(node.left, level + 1)
                bfs(node.right, level + 1)

        bfs(root, 0)
        return [ l for l in h.values() ]