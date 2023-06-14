# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mini = float("inf")
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        sorted_array = dfs(root)
        for i in range(1,len(sorted_array)):
            mini = min(mini, abs(sorted_array[i]-sorted_array[i-1]))
        return mini
        