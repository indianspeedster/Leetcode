class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, total):
            if total == amount:
                return 1
            if i == len(coins) or total > amount:
                return 0
            pick = dfs(i, total + coins[i])
            npick = dfs(i+1, total)
            return pick + npick
        return dfs(0,0)
