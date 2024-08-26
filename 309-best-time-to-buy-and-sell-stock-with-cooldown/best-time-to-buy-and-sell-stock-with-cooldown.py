class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        @cache
        def dfs(i,sell):
            if i >= n:
                return 0
            if sell:
                buy = dfs(i+1, not sell) - prices[i]
                cool = dfs(i+1, sell)
                return max(buy,cool)
            else:
                selli =  dfs(i+2, not sell) + prices[i] 
                cooldown = dfs(i+1,sell)
                return max(selli,cooldown)
        return dfs(0,True)
        