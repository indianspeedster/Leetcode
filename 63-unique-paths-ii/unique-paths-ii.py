class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dfs(i,j):
            if i not in range(m) or j not in range(n):
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0,0)

        