class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for start, end, charge in flights:
            adjList[start].append((end, charge))
        @cache
        def dfs(node, stop):
            if node == dst:
                return 0
            if stop == -1:
                return float("inf")
            maxi = float("inf")
            for child in adjList[node]:
                nextnode, charge = child
                maxi = min(maxi, charge + dfs(nextnode, stop-1))
            return maxi
        
        ans = dfs(src, k)
        return -1 if ans == float("inf") else ans

        