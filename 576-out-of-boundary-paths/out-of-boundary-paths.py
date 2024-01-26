class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(i,j,step):
            if step < 0:
                return 0
            if step >= 0:
                if i not in range(m) or j not in range(n):
                    return 1

            return dfs(i+1, j, step -1) + dfs(i-1, j, step -1) + dfs(i, j+1, step -1) +dfs(i, j-1, step -1)
            
            
            
        mod = (10**9) + 7
        return dfs(startRow, startColumn, maxMove) % mod
        