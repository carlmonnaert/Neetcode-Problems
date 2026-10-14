# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            return self.lowestCommonAncestor(root, q, p)

        if p.val < root.val < q.val:
            return root
        
        elif p.val < q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif root.val < p.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        elif q.val == root.val:
            return q
        
        else:
            return p