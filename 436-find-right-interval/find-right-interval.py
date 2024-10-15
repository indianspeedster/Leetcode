class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startList = [(j[0], i) for i,j in enumerate(intervals)]
        startList.sort()
        ans = []
        n = len(startList)
        for start, end in intervals:
            l,r = 0, n-1
            perfect = -1
            while l <= r:
                ind = (l+r) // 2
                if startList[ind][0] >= end:
                    perfect = startList[ind][1]
                    r = ind - 1
                else:
                    l = ind + 1
            ans.append(perfect)
        return ans
            





        