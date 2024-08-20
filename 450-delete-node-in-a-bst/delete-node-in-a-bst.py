# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findlastright(node):
            if not node.right:
                return node
            return findlastright(node.right)
        def helper(node):
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = node.right
            attach = findlastright(node.left)
            attach.right = temp
            return node.left
        if not root:
            return root
        if root.val == key:
            return helper(root)
        dummy = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = helper(root.left)
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = helper(root.right)
                else:
                    root = root.right
        return dummy
    

        