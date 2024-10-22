# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelDict = defaultdict(int)

        def dfs(node, level):
            if not node:
                return
            levelDict[level] += node.val
            dfs(node.right, level+1)
            dfs(node.left, level+1)
            return
        
        dfs(root, 0)
        return sorted(levelDict.values(), reverse = True)[k-1] if len(levelDict) >= k else -1
            
        