class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        perimetre = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if i+1 in range(row):
                        if grid[i+1][j] == 0:
                            perimetre += 1
                    else:
                        perimetre += 1
                    if j+1 in range(col):
                        if grid[i][j+1] == 0:
                            perimetre += 1
                    else:
                        perimetre += 1
                    if i-1 in range(row):
                        if grid[i-1][j] == 0:
                            perimetre += 1
                    else:
                        perimetre += 1
                    if j-1 in range(col):
                        if grid[i][j-1] == 0:
                            perimetre += 1
                    else:
                        perimetre += 1
        return perimetre
                


        