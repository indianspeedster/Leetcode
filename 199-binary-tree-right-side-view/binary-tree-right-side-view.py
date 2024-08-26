# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st = [root]
        ans = []
        while st:
            curr = []
            for node in st:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            ans.append(st[-1].val)
            st = curr
        return ans
        