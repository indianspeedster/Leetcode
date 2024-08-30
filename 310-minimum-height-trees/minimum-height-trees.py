class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(n)}
        if not edges:
            return [i for i in range(n)]
        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)
        degree = [0] * n
        leaves = []
        for node, edges in adjList.items():
            degree[node] = len(edges)
            if degree[node] == 1:
                leaves.append(node)
                degree[node] = 0
        count = len(leaves)
        while count < n :
            new_leaves = []
            for node in leaves:
                for neighbour in adjList[node]:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        new_leaves.append(neighbour)
                degree[node] = 0
            count += len(new_leaves)
            leaves = new_leaves
        return leaves
        