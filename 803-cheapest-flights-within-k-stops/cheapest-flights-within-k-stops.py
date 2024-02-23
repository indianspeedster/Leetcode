class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        @cache
        def dfs(n, k):
            if n == dst:
                return 0
            if k == -1 :
                return float("inf")
            if n not in dic:
                return float("inf")
            maxi = float("inf")
            for nodes in dic[n]:
                #print(nodes)
                maxi = min(maxi, nodes[1] + dfs(nodes[0], k-1))
            return maxi
        dic = {}
        for source, dest, charge in flights:
            if source not in dic:
                dic[source] = [(dest, charge)]
            else:
                dic[source].append((dest, charge))
        print(dic)
        ans =  dfs(src, k) if src in dic else -1
        
        return ans if ans != float("inf") else -1

