# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            root1 = TreeNode(val)
            root1.left = root
            return root1
        def dfs(node, level):
            if not node:
                return
            if level == depth-1:
                temp1 = node.left
                temp2 = node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = temp1
                node.right.right = temp2
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return root
        
        