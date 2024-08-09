class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magic(square):
            mset = set()
            for i in range(3):
                for j in range(3):
                    if square[i][j] not in range(1, 10):
                        return False
                    if square[i][j] in mset:
                        return False
                    mset.add(square[i][j])
                        
            rows = [0,0,0]
            col = [0,0,0]
            diag = [0,0,0]
            for i in range(3):
                rows[i] = sum(square[i])
                col[i] = sum([square[k][i] for k in range(3)])
            diag[0] = square[0][0] + square[1][1] +square[2][2]
            diag[1] = square[2][0] + square[1][1] + square[0][2]
            diag[2] = diag[1]
            
            if rows == col == diag:
                return True
            return False
        ans = 0
        m,n = len(grid), len(grid[0])
        for i in range(m-3+1):
            for j in range(n-3+1):
                square = []
                for k in range(3):
                    inner = []
                    for l in range(3):
                        inner.append(grid[i+k][j+l])
                    square.append(inner)
                
                ans += int(magic(square))
        return ans
        