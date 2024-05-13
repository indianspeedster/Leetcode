class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols= len(grid), len(grid[0])
        ans = rows * 2 ** (cols-1)

        for c in range(1,cols):
            cnt = 0
            for r in range(rows):
                if grid[r][c] != grid[r][0]:
                    cnt += 1
            cnt = max(cnt, rows-cnt)
            ans += cnt * (2**(cols-c-1))
        return ans
        