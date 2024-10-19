class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(x):
            ans = ""
            for i in x:
                if i =="1":
                    ans += "0"
                else:
                    ans += "1"
            return ans
       
        def dfs(n):
            if n == 0:
                return "0"
            l = dfs(n-1)
            return l + "1" + invert(l)[::-1]
        return dfs(n)[k-1]
        