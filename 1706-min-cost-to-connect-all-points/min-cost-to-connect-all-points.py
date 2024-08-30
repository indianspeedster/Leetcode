class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                distance = abs(x2-x1) + abs(y2-y1)
                adjList[i].append((distance, j))
                adjList[j].append((distance, i))
        res = 0
        visited = set()
        minH = [[0, 0]]

        while len(visited) < n:
            distance, node = heapq.heappop(minH)
            if node in visited:
                continue
            visited.add(node)
            res += distance
            for dist, nodes in adjList[node]:
                if nodes not in visited:
                    heapq.heappush(minH, [dist, nodes])
        return res

        