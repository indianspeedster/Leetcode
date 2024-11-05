class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        pq = [(grid[0][0],0,0)]

        minTime = {(0,0): grid[0][0]}

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while pq:
            dist, x,y = heapq.heappop(pq)
            if (x,y) == (m-1, n-1): return dist
            for i,j in directions:
                xi, yj = x+i, y+j
                if xi in range(m) and yj in range(n):
                    newDist = max(dist, grid[xi][yj])

                    if (xi,yj) not in minTime or minTime[(xi,yj)] > newDist:
                        heapq.heappush(pq, (newDist, xi, yj))
                        minTime[(xi,yj)] = newDist
        return -1

        