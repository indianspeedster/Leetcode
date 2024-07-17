# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = [root]
        dummy = TreeNode(0)
        dummy.left = root
        self.delete = []
        def dfs(node):
            if not node:
                return 
            if node.left and node.left.val in to_delete:
                self.delete.append((node, node.left))
            if node.right and node.right.val in to_delete:
                self.delete.append((node, node.right))
            dfs(node.left)
            dfs(node.right)
        dfs(dummy)
        for node, child in self.delete:
            if child in ans:
                ans.remove(child)
                
            if node.left == child:
                node.left = None
            elif node.right == child:
                node.right = None
            if child.left:
                ans.append(child.left)
                child.left = None
            if child.right:
                ans.append(child.right)
                child.right = None
        return ans
            
        