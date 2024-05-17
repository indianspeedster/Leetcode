# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            if node and node.left:
                if not node.left.left and not node.left.right and node.left.val == target:
                    self.flag = True
                    node.left=None
            if node and  node.right:
                if not node.right.right and not node.right.left and node.right.val == target:
                    self.flag = True 
                    node.right = None
            dfs(node.left)
            dfs(node.right)
        self.flag = True
        for i in range(50):
            if not root.left and not root.right and root.val == target:
                return None
            dfs(root)
            if self.flag == False:
                break
            self.flag = False
        return root
            
            
        