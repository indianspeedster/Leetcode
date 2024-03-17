class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        intervals.append(newInterval)
        intervals.sort()
        for left, right in intervals:
            if not ans:
                ans.append([left, right])
                continue
            if ans[-1][1] >= left:
                l,r = ans.pop()
                l = min(l, left)
                r = max(r, right)
                ans.append([l,r])
            else:
                ans.append([left, right])
        return ans
        

        