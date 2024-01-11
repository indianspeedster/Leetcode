# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result = 0
        def dfs(node, cur_min, cur_max):
            if not node:
                return
            self.result = max(self.result, abs(node.val-cur_max), abs(node.val-cur_min))
            cur_min = min(node.val, cur_min)
            cur_max = max(node.val, cur_max)

            dfs(node.left, cur_min, cur_max)
            dfs(node.right, cur_min, cur_max)
        
        dfs(root, root.val, root.val)
        return self.result

        