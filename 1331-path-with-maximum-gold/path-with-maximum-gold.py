class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(i, j, visited):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0 or (i,j) in visited:
                return 0
            visited.add((i, j))
            up = grid[i][j] + dfs(i-1, j, visited.copy())
            down = grid[i][j] + dfs(i+1, j, visited.copy())
            left = grid[i][j] + dfs(i, j-1, visited.copy())
            right = grid[i][j] + dfs(i, j+1, visited.copy())
            return max(up, down, left, right)
        
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    visited = set()
                    ans = max(ans, dfs(i, j, visited))
        return ans
        