class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dfs(num):
            if n == 1:
                return 1
            maxi = 0 if num is n else num 
            for i in range(1,num):
                maxi = max(maxi, dfs(i)*dfs(num-i))
            return maxi
        return dfs(n)
        