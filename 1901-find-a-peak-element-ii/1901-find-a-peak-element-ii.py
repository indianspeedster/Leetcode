class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(mat)-1
        while bottom > top:
            mid = (top + bottom) // 2
            if max(mat[mid]) > max(mat[mid+1]):
                bottom = mid
            else:
                top = mid+1
        return [bottom,mat[bottom].index(max(mat[bottom]))]
                    
        