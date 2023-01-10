# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        def dfs(node,n):
            n += node.val
            if not node.left and not node.right:
                return n>=limit
           
            left = dfs(node.left,n) if node.left else False
            right = dfs(node.right,n) if node.right else False
            if not left : node.left = None
            if not right: node.right = None
            return left or right
        
        return root if dfs(root,0) else None