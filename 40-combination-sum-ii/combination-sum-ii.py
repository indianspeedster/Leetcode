class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(n, curr, su):
            if su == target:
                res.append(curr.copy())
                return
            if n >= len(candidates) or su > target:
                return
            dfs(n+1, curr + [candidates[n]], su + candidates[n])
            while n+1 in range(len(candidates)) and candidates[n] == candidates[n+1]:
                n += 1
            dfs(n+1, curr, su)
            return
        dfs(0, [], 0)
        return res
        

            

        
        