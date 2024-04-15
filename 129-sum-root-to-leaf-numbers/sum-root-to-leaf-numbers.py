# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(node,su):
            if not node:
                return
            if not node.left and not node.right:
                
                self.sum += int(su+str(node.val))
            dfs(node.left, su + str(node.val))
            dfs(node.right, su + str(node.val))
        dfs(root, "")
        return self.sum
        