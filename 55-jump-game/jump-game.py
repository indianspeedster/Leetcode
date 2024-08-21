class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dfs(i):
            if i == len(nums) -1 :
                return True
            if i >= len(nums):
                return False
            steps = nums[i]
            final = False
            for j in range(1, steps+1):
                final = final or dfs(i+j)
                if final == True:
                    break
            return final
        return dfs(0)

        