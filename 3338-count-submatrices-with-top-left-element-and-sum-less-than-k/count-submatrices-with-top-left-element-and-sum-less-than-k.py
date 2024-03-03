
import copy
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        grid2 = [[0 for _ in range(n)] for l in range(m)]
        top = copy.deepcopy(grid)
        bottom =  copy.deepcopy(grid)
        for i in range(m):
            for j in range(1,n):
                top[i][j] += top[i][j-1]
        for i in range(1,m):
            for j in range(n):
                bottom[i][j] += bottom[i-1][j]   
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    matrix_sum = grid[i][j]
                else:
                    matrix_sum = grid[i][j] + grid2[i-1][j-1]
                
                matrix_sum += top[i][j-1] if j >=1 else 0
                matrix_sum += bottom[i-1][j] if i >= 1 else 0

                grid2[i][j] = matrix_sum
                if matrix_sum <= k:
                    count += 1
        return count
                    
        