class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, total):
            
            if i == len(nums) and total == target:
                return 1
            if i >= len(nums):
                return 0
            plus = dfs(i + 1, total + nums[i])
            minus = dfs(i+1, total - nums[i])
            return plus + minus
        return dfs(0, 0)
            
        