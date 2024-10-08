"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        def dfs(node):
            arr = []
            for nodes in node.children:
                arr =  arr + dfs(nodes)
            return arr + [node.val]
       
        return dfs(root)
        
        