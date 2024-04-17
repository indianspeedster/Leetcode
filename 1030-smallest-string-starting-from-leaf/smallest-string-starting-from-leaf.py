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
                an = st + chr(97+node.val)
                self.strdict.add(an[::-1])
            dfs(node.left, st + chr(97+node.val))
            dfs(node.right, st + chr(97+node.val))
        dfs(root, "")
        self.strdict = list(self.strdict)
        self.strdict.sort()
        print(self.strdict)
        for string in self.strdict:
            if len(string) > 1:
                return string
        return self.strdict[0]
        

        