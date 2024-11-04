class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        inf = 10**12
        track = [[inf]*n for i in range(m)]
        track[0][0] = 0
        pq = [(1, 0, 0)]
        directions = [(1,0), (0,1), (-1,0), (0, -1), (1,1), (1,-1), (-1, 1), (-1,-1)]

        while pq:
            dist, x, y = heapq.heappop(pq)
            if grid[x][y] == 1:
                continue
            if (x,y) == (m-1,n-1):
                return dist
            for i,j in directions:
                xi, yj = x+i, y+j

                if xi in range(m) and yj in range(n):
                    if track[xi][yj] > dist +1 and grid[xi][yj] == 0:
                        track[xi][yj] = dist+1
                        heapq.heappush(pq,(dist+1, xi,yj))
        return -1




        