class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        minimumSum = float("inf")
        m = len(triangle)
        @cache
        def dfs(i,j):
            if i not in range(m):
                return float("inf")
            rowLen = len(triangle[i])
            if j not in range(rowLen):
                return float("inf")
            if i == m-1:
                return triangle[i][j]
            return triangle[i][j] + min(dfs(i+1,j), dfs(i+1, j+1))
        return dfs(0,0) 

        