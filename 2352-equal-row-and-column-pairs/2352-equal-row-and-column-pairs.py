class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = {i:[] for i in range(n)}
        column = {j:[] for j in range(n)}
        for i in range(n):
            for j in range(n):
                row[i].append(grid[i][j])
                column[j].append(grid[i][j])
        count = 0
        for i in range(n):
            for j in range(n):
                if row[i]==column[j]:
                    count +=1
        return count
        