class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}
        def dfs(left, right):
            if right-left == 1:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            res = float("inf")
            for cut in cuts:
                if left<cut<right:
                    res = min(res, right-left + dfs(left, cut)+dfs(cut, right))
            res = 0 if res== float("inf") else res
            dp[(left,right)] = res
            return dp[(left, right)]
        return dfs(0, n)
            
        
        