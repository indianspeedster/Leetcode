class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[[-1]*n for _ in range(n)] for t in range(m)]
        
        def dfs(i,j1,j2):
            if j1 < 0 or j2 < 0 or j1 > n-1 or j2 > n-1:
                return float("-inf")
            if dp[i][j1][j2] != -1 :
                return dp[i][j1][j2]
            if i == m-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            else:
                maxi = float("-inf")
                for k in range(-1,2):
                    for l in range(-1,2):
                        if j1==j2:
                            d = grid[i][j1] + dfs(i+1,j1+k,j2+l)
                        else:
                            d = grid[i][j1] + grid[i][j2] + dfs(i+1,j1+k,j2+l)
                        maxi = max(maxi,d)
                dp[i][j1][j2] = maxi
                return maxi
        return dfs(0,0,n-1)
                
            
                
                
        
        