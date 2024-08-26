from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] != 1:
                return True
            grid2[i][j] = 2  
            isSubIsland = grid1[i][j] == 1 
            
            # Explore all four directions
            isSubIsland &= dfs(i + 1, j)
            isSubIsland &= dfs(i - 1, j)
            isSubIsland &= dfs(i, j + 1)
            isSubIsland &= dfs(i, j - 1)
            
            return isSubIsland
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j):
                    ans += 1
                    
        return ans

                
        