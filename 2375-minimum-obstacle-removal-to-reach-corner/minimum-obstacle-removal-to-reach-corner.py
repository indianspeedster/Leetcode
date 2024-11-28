class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        heap = [(0,0,0)]

        m,n = len(grid), len(grid[0])

        visited = set((0,0))
        while heap:
            dist, x,y = heapq.heappop(heap)

            if x == m-1 and y == n-1:
                return dist
            
            

            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            for i,j in directions:
                xi , yj = x+i, y+j
                if (xi, yj) in visited:
                    continue
                if xi in range(m) and yj in range(n):
                    visited.add((xi,yj))
                    heapq.heappush(heap, (dist + grid[xi][yj], xi, yj))
        return -1
        