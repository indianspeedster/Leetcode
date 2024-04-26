class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        prev = grid[0]
        row, col = len(grid), len(grid[0])
        
        for i in range(1, row):
            curr = [0 for i in range(col)]
            for j in range(col):
                mini = float("inf")
                for k in range(col):
                    if k == j:
                        continue
                    mini = min(mini, grid[i][j] + prev[k])
                curr[j] = mini
            prev = curr
           
            
        return min(prev)
        