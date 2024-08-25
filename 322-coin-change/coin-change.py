class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(ind, change):
            if ind not in range(len(coins)):
                return float("inf")
            if change == 0:
                return 0
            elif change < 0:
                return float("inf")
            pick = 1 + dfs(ind, change-coins[ind])
            npick = dfs(ind+1, change)
            return min(pick, npick)
        ans =  dfs(0, amount)
        return ans if ans != float("inf") else -1 

        