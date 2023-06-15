# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxi = [root.val, 1]
        node = root
        st = [node]
        i = 0
        while st:
            n = []
            sumi = 0
            for x in st:
                sumi += x.val
                if x.left:
                    n.append(x.left)
                if x.right:
                    n.append(x.right)
            i += 1
            if sumi > maxi[0]:
                maxi = [sumi, i]
            st = n
        return maxi[1]