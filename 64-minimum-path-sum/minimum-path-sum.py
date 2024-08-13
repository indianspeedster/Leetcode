class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        @cache
        def dfs(i,j):
            if i not in range(m) or j not in range(n):
                return float("inf")
            if i == m-1 and j == n-1:
                return grid[i][j]
            right = grid[i][j] + dfs(i, j+1)
            down = grid[i][j] + dfs(i+1, j)
            return  min(right, down)
        return dfs(0,0)

        