# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, res):
            if not node:
                return res
            if not node.left and not node.right:
                res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)
            return res
        return dfs(root1,[]) == dfs(root2,[])

        