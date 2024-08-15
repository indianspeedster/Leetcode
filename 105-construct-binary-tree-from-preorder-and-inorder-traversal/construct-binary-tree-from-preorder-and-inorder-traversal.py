# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder):
            if not preorder:
                return None
            node = TreeNode(preorder[0])
            bisec = 0
            for i, j in enumerate(inorder):
                if j == preorder[0]:
                    bisec = i
                    break
            node.left = build(preorder[1:bisec+1], inorder[:bisec])
            node.right = build(preorder[bisec+1:], inorder[bisec+1:])
            return node
        root = build(preorder, inorder)
        return root
        