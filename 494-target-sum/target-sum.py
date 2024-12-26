class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, curr):
            if i == len(nums):
                if curr == target:
                    return 1
                return 0
            left = dfs(i+1, curr + nums[i])
            right = dfs(i+1, curr - nums[i])
            return left+right
        
        return dfs(0,0)
        