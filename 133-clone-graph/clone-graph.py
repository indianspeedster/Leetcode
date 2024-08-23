"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.nodes = {}
        def dfs(node):
            if node and node not in self.nodes:
                self.nodes[node] = Node(val = node.val)
            else:
                return 
            for neigh in node.neighbors:
                dfs(neigh)
            for neigh in node.neighbors:
                self.nodes[node].neighbors.append(self.nodes[neigh])
            return 
        dfs(node)
        return self.nodes[node] if node else node
        