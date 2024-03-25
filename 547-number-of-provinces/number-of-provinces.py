class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = {i:[] for i in range(len(isConnected))}
        for ind, val in enumerate(isConnected):
            for ind2, val2 in enumerate(val):
                if val2 == 1 and ind2 != ind:
                    adjList[ind].append(ind2)
        
        provinces = 0
        visited = set()
        def dfs(city):
            if city in visited:
                return
            visited.add(city)
            for cities in adjList[city]:
                dfs(cities)
            return
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                dfs(i)
        return provinces
        