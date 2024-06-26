# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.nodeVals = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.nodeVals.append(node.val)
            dfs(node.right)
        dfs(root)
        
        def build(vals):
            if not vals:
                return None
            k = len(vals)
            mid = k//2
            
            node = TreeNode(vals[mid])
            node.left = build(vals[:mid])
            node.right = build(vals[mid+1:])
            return node
        ans = build(self.nodeVals)
        return ans

        