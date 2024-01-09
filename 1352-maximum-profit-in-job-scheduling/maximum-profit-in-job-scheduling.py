class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        interval = sorted(zip(startTime, endTime, profit))
        @cache
        def dfs(ind):
            if ind == len(profit):
                return 0
            res = dfs(ind+1)
            j = bisect.bisect(interval, (interval[ind][1], -1, -1))
            res = max(res, interval[ind][2] + dfs(j))
            
            return res
        return dfs(0)