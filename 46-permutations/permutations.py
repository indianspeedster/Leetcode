class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(nums, perm):
            if not nums:
                self.ans.append(perm)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], perm + [nums[i]])
            return 
        dfs(nums, [])
        return self.ans
        