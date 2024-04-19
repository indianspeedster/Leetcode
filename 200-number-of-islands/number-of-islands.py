class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        row, col = len(grid), len(grid[0])
        def dfs(i,j):
            if i not in range(row) or j not in range(col) or (i,j) in visited or grid[i][j] == "0":
                return 
            visited.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        ans = 0
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        return ans

        