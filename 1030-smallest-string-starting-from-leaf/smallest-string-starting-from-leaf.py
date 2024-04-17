# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.strdict = set()
        def dfs(node, st):
            if not node:
                return
            if not node.left and not node.right:
                self.strdict.add(chr(97+node.val)+st)
            dfs(node.left, chr(97+node.val)+st)
            dfs(node.right, chr(97+node.val)+st)
        dfs(root, "")
        self.strdict = list(self.strdict)
        self.strdict.sort()
        return self.strdict[0]
        

        