class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def check(arr, x):
            for num in arr:
                if abs(num-x) == k:
                    return False
            return True
        self.ans = 0
        def dfs(i, ar):
            if i == len(nums):
                return 
            if check(ar, nums[i]):
                self.ans += 1
                dfs(i+1, ar + [nums[i]])
            dfs(i+1, ar)
        dfs(0, [])
        return self.ans
            

        