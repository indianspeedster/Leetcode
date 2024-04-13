class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        newMatrix = [[0 for i in range(len(matrix[0]))] for _ in range(len(matrix))]
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                newMatrix[i][j] = int(matrix[i][j])
        for i in range(1, row):
            for j in range(col):
                if newMatrix[i-1][j] != 0 and newMatrix[i][j] !=0 :
                    newMatrix[i][j] += newMatrix[i-1][j]
        def bestArea(heights):
            maxArea = 0
            for i, h in enumerate(heights):
                area = h
                ind = i-1
                while ind >= 0 and heights[ind] >=h:
                    area += h
                    ind -= 1
                ind = i+1
                while ind <= len(heights)-1 and heights[ind] >= h:
                    area += h
                    ind += 1
                maxArea = max(area, maxArea)
            return maxArea
        maxi = 0
        for row in newMatrix:
            maxi = max(maxi, bestArea(row))
        return maxi
          