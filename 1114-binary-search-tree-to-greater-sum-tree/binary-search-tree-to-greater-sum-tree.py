# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.l1 = []
        def dfs(node):
            if not node:
                return
            self.l1.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        self.l2 = sorted(self.l1, reverse=True)
        dic = {}
        pre = 0
        for num in self.l2:
            pre += num
            if num not in dic:
                dic[num] = pre
        def dfs(node):
            if not node:
                return
            node.val = dic[node.val]
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root