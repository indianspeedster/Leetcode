class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgemap = defaultdict(int)
        for u,v in edges:
            edgemap[u] += 1
            edgemap[v] += 1
        n = len(edgemap.keys()) 

        for edge, connection in edgemap.items():
            if connection == n-1:
                return edge
        