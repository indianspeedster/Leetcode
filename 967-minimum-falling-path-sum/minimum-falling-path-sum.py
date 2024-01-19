class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, cols = len(matrix), len(matrix[0])
        dp = [["t" for i in range(cols)] for j in range(row)]
        def dfs(i,j):
            if i not in range(row) or j not in range(cols):
                return float("inf")
            if dp[i][j] != "t":
                return dp[i][j]
            if i == row-1:
                return matrix[i][j]
            dp[i][j] =  matrix[i][j] + min(dfs(i+1, j), dfs(i+1, j-1), dfs(i+1, j+1))
            return dp[i][j]
        mini = float("inf")
        for i in range(cols):
            mini = min(mini, dfs(0,i))
        
        return mini

        