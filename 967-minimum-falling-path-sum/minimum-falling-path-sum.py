class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        minimumSum = float("inf")
        m,n = len(matrix), len(matrix[0])
        @cache
        def dfs(i,j):
            if i not in range(m) or j not in range(n):
                return float("inf")
            if i == m-1:
                return matrix[i][j]
            return matrix[i][j] + min(dfs(i+1,j), dfs(i+1, j-1), dfs(i+1, j+1))
        for i in range(n):
            minimumSum = min(minimumSum, dfs(0, i))
        return minimumSum
            


