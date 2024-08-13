class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(ind, target, arr):
            if target == 0:
                res.append(arr.copy())
                return
            if ind >= len(candidates):
                return
            if target<0:
                return
            prev = -1
            for i in range(ind, len(candidates)):
                if candidates[i] == prev: 
                    continue
                backtrack(i+1, target - candidates[i], arr+[candidates[i]])
                prev = candidates[i]
        backtrack(0,target,[])
        return res
                
        

            

        
        