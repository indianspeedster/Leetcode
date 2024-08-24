class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for i, j in prerequisites:
            adjList[i].append(j)
        self.visited = set()
        @cache
        def dfs(node):
            if node in self.visited :
                return False
            if adjList[node] == []:
                return True
            self.visited.add(node)
            for nodes in adjList[node]:
                if not dfs(nodes):
                    return False
            self.visited.remove(node)
            #adjList[node] = []
            return True
        ans = True
        for i in range(numCourses):
            ans = ans and dfs(i)
        return ans
            
                