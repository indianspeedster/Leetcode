class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        def dfs(n):
            if n == 1:
                return True
            ans = False
            for i in [2,3,5]:
                if n%i == 0:
                    ans = ans or dfs(n//i)
            return ans
        return dfs(n)
        