class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for left, right in intervals:
            if not ans:
                ans.append([left, right])
                continue
            if ans[-1][1] >= left:
                l, r = ans.pop()
                mini = min(l, left)
                maxi = max(r, right)
                ans.append([mini, maxi])
            else:
                ans.append([left, right])
        return ans 
        