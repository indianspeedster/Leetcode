class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, cols = len(matrix), len(matrix[0])
        @cache
        def dfs(i,j):
            if i not in range(row) or j not in range(cols):
                return float("inf")
            if i == row-1:
                return matrix[i][j]
            return matrix[i][j] + min(dfs(i+1, j), dfs(i+1, j-1), dfs(i+1, j+1))
        mini = float("inf")
        for i in range(cols):
            mini = min(mini, dfs(0,i))
        return mini

        