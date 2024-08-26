class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        hashSet = set()
        bfs = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hashSet.add((i,j))
                elif grid[i][j] == 2:
                    bfs.append((i,j))
        
        ans = 0
        while hashSet and bfs:
            st = []
            for i,j in bfs:
                if (i+1, j) in hashSet:
                    hashSet.remove((i+1,j))
                    st.append((i+1, j))
                if (i-1, j) in hashSet:
                    hashSet.remove((i-1,j))
                    st.append((i-1, j))
                if (i, j+1) in hashSet:
                    hashSet.remove((i,j+1))
                    st.append((i, j+1))
                if (i, j-1) in hashSet:
                    hashSet.remove((i,j-1))
                    st.append((i, j-1))
            ans += 1
            bfs = st
        if hashSet:
            return -1
        if bfs:
            return ans
        return 0



        