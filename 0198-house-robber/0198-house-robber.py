class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(n):
            if n<0:
                return 0
            sel = nums[n] + dfs(n-2)
            unsel = dfs(n-1)
            return max(sel,unsel)
        return dfs(n-1)