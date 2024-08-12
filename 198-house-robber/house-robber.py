class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(n):
            if n >= len(nums):
                return 0
            pick = nums[n] + dfs(n+2)
            npick = dfs(n+1)
            return max(pick, npick)
        return dfs(0)
        