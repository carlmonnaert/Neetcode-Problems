# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        a, b = root, subRoot
        
        if b is None:
            return True
        
        elif a is None:
            return False

        return self.equal(a,b) or self.isSubtree(a.right, subRoot) or self.isSubtree(a.left, subRoot)
    
    def equal(self, l, r):
            if l is None and r is None:
                return True

            elif l is not None and r is not None:
                return (l.val == r.val) and self.equal(r.right, l.right) and self.equal(r.left, l.left)
            
            else:
                return False
        