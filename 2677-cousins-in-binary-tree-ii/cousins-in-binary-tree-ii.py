# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        hashMap = defaultdict(int)
        def dfs1(node, level):
            if not node:
                return node
            hashMap[level] += node.val
            dfs1(node.left, level+1)
            dfs1(node.right, level+1)
            return node
        def dfs2(node, level):
            if not node:
                return node
            if level == 0:
                node.val = 0
            val = 0
            if node.left:
                val += node.left.val
            if node.right:
                val += node.right.val
            if node.left:
                node.left.val = hashMap[level+1] - val
            if node.right:
                node.right.val = hashMap[level+1] - val

            dfs2(node.left, level+1)
            dfs2(node.right, level+1)
            return node
        dfs1(root, 0)
        return dfs2(root, 0)
            
        