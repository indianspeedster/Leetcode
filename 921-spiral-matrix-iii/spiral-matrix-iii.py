class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direction = [[0,1], [1, 0], [0, -1], [-1, 0]]
        step = 1
        i = 0
        res = []
        while len(res) < rows * cols:
            
            for _ in range(2):
                dr, dc = direction[i]
                for _ in range(step):
                    if rStart in range(rows) and cStart in range(cols):
                        res.append([rStart, cStart])
                    rStart += dr
                    cStart += dc
                i = (i+1) % 4
            step += 1
        return res


        