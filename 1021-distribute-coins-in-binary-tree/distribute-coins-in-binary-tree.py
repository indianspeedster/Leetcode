# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return [0,0]

            leftsize, leftcoins = dfs(node.left)
            rightsize, rightcoins = dfs(node.right)
            size = 1 + leftsize + rightsize
            coins = node.val + leftcoins + rightcoins
            self.ans += abs(size-coins)
            return (size, coins)
        dfs(root)
        return self.ans

        