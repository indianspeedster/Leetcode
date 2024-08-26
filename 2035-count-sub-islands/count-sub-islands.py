class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid2), len(grid2[0])
        def dfs(i,j):
            if i not in range(m) or j not in range(n):
                return
            if grid2[i][j] != 1:
                return
            visited.add((i,j))
            grid2[i][j] = 2
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        ans = 0
        for i in range(m):
            for j in range(n):
                visited = set()
                if grid2[i][j] == 1:
                    dfs(i,j)
                Flag = True
                for x,y in visited:
                    if grid1[x][y] != 1:
                        Flag = False
                        break
                if visited and Flag:
                    ans += 1
        return ans
                
        

