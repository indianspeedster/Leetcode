class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        roots = {}
        def find(x):
            if x not in roots:
                roots[x] = x
            while (x != roots[x]):
                x = roots[x]
            return x
        def union(x,y):
            roots[find(x)] = find(y)
        length = len(grid)
        for i in range(length):
            for j in range(length):
                if grid[i][j] == '/':
                    union((i,j,'N'), (i,j,'W'))
                    union((i,j,'S'), (i,j,'E'))
                elif grid[i][j] == '\\':
                    union((i,j,'N'), (i,j,'E'))
                    union((i,j,'S'), (i,j,'W'))
                elif grid[i][j] == ' ':
                    union((i,j,'N'), (i,j,'E'))
                    union((i,j,'S'), (i,j,'W'))
                    union((i,j,'N'), (i,j,'W'))
                if j > 0:
                    union((i, j-1, 'E'), (i, j, 'W'))
                if i > 0:
                    union((i-1, j, 'S'), (i, j, 'N'))
        return len(set(map(find, roots)))
                    
        