class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(n, last):
            if n >= len(nums):
                return 0
            if last:
                pick = nums[n] + dfs(n+1, False)
            else: 
                pick = 0
            npick = dfs(n+1, True)
            return max(pick, npick)
        return dfs(0, True)
        
            

        