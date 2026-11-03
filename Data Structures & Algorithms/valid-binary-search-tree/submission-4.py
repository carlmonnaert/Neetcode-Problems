# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def listify(t,s):
            if t:
                v, l, r = t.val, t.left, t.right
                listify(l,s)
                s.append(v) 
                listify(r,s)
            return s
        l = listify(root,[])
        for i in range(len(l)-1):
            if l[i] >= l[i+1]:
                return False
        return True
