# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(m,n):
            if not m and not n:
                return True
            if not m or not n or m.val!=n.val :
                return False
            return dfs(m.left,n.left) and dfs(m.right,n.right)
        return dfs(p,q)
            
        