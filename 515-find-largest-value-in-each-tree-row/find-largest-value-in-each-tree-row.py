# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        levels = {}

        def dfs(level, node):
            if not node:
                return
            if level not in levels:
                levels[level] = float("-inf")
            levels[level] = max(node.val, levels[level])

            dfs(level+1, node.left)
            dfs(level+1, node.right)
        dfs(0, root)
        return list(levels.values())
        