class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(i, arr):
            if i == len(nums):
                if arr not in self.ans:
                    self.ans.append(arr)
                return
            dfs(i+1, arr + [nums[i]])
            dfs(i+1, arr)
            return
        dfs(0, [])
        return self.ans
        

        