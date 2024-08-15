# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        def dfs(node):
            if not node:
                return -1
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            if abs(left-right) > 1:
                self.result=False
            return max(left, right)
        dfs(root)
        return self.result

        