class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m,n = len(matrix), len(matrix[0])
        for num in matrix:
            mini = (-1, 1e9)
            for i, n in enumerate(num):
                if n < mini[1]:
                    mini = (i, n)
            maxi = 0
            for l in range(m):
                maxi = max(maxi, matrix[l][mini[0]])
            if maxi == mini[1]:
                ans.append(maxi)
        return ans

        