class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = 10**9

        dp = [[inf]*(n) for i in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for i,j,t in times:
            dp[i-1][j-1] = t
       
        for l in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j] ,dp[i][l] + dp[l][j])
        
        #seen = [False]*n
        print(dp[k-1])
        """def dfs(node, seen):
            if all(seen):
                return 0
            best = inf
            for i in range(n):
                if seen[i] ==  False and dp[node][i] != inf:
                    seen[i] = True
                    best = min(best, dfs(i, seen) + dp[node][i])
                    seen[i] = False
            return best
        seen[k-1] = True
        return dfs(k-1, seen)"""

        ans = max(dp[k-1])

        if ans == inf:
            return -1
        return ans


        