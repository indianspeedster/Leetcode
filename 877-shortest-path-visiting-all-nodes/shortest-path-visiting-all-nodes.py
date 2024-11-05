class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        N = len(graph)
        inf = 10**20

        d = [[inf]*N for _ in range(N)]

        for i in range(N):
            d[i][i] = 0
            for v in graph[i]:
                d[i][v] = 1

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        dp = {}
        def listToBin(arr):
            arr = reversed(arr)
            ans = 0
            for i , val in enumerate(arr):
                if val:
                    ans += 2**i
            return ans

        def calc(current, seen):
            if all(seen):
                return 0
            deci = listToBin(seen)
            if (current, deci) in dp:
                return dp[(current, deci)]
            best = inf
            for v in range(N):
                if not seen[v]:
                    seen[v] = True
                    best = min(best, calc(v, seen) + d[current][v])
                    seen[v] = False
            dp[(current, deci)] = best

            return dp[(current, deci)]

        best = inf

        for start in range(N):
            seen = [False]*N
            best = min(best, calc(start, seen))
        return best