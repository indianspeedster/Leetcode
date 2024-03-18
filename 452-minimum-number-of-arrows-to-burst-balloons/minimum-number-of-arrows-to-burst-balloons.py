class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key =  lambda x: x[1])
        arr = points[0][1]
        count = 1
        for l,r in points:
            if arr >= l:
                continue
            
            else:
                arr = r
                count += 1
        return count 
