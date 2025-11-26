"""class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        self.total = 0

        mod=10**(+7)
        dp = {}
        def dfs(i,j, val):
            if (i,j,val) in dp:
                return dp[(i,j,val)]
            if i not in range(m) or j not in range(n):
                return 0
            cur = val + grid[i][j]
            if i==m-1 and j==n-1:
                if cur%k==0:
                    return 1
                return 0
            val2 = (dfs(i+1,j, cur) + dfs(i,j+1, cur) ) % mod
            dp[(i,j,val)] = val2
            return val2
        return dfs(0,0,0)%mod"""
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])

        mod = 10**9 + 7

        dp = {}
        def dfs(i,j, cur):

            if (i,j,cur) in dp:
                return dp[(i,j,cur)]
            val = cur + grid[i][j]

            current = val%k
            if i == m-1 and j == n-1:
                if current == 0:
                    return 1
                else:
                    return 0

            total = 0
            if i+1 < m:
                total += dfs(i+1, j, current)
            
            if j+1 < n:
                total += dfs(i, j+1, current)

            dp[(i,j,cur)] = total % mod
            return dp[(i,j,cur)]

        return dfs(0,0,0) % mod
        
        
        
            
        