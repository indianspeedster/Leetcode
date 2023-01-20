class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(i,sub):
            if len(sub)>1:
                res.add(tuple(sub))
            if i >= len(nums):
                return
            if not sub or nums[i]>=sub[-1]:
                dfs(i+1,sub+[nums[i]])
            dfs(i+1,sub)
            return
        dfs(0,[])
        return res
            

        