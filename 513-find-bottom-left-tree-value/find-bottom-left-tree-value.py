# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        st = [root]
        ans = root
        while st:
            curr = []
            for node in st:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            if curr:
                ans = curr[0]
            st = curr
        return ans.val
        