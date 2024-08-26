
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return
            if grid2[i][j] != 1:
                return
            visited.add((i, j))
            grid2[i][j] = 2  # Mark as visited
            # Explore all four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                visited = set()
                if grid2[i][j] == 1:
                    dfs(i, j)
                flag = True
                for x, y in visited:
                    if grid1[x][y] != 1:
                        flag = False
                        break
                if visited and flag:
                    ans += 1
        return ans

