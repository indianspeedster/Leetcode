# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = [[root.val]]
        queue = [root]
        while queue:
            nextQueue = []
            level = []
            for node in queue:
                if node.left:
                    nextQueue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    nextQueue.append(node.right)
                    level.append(node.right.val)
            if level: 
                ans.append(level) 
            queue = nextQueue
        return ans
        
        