class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def goals(x):
            if x < 0:
                return 0
            cur, l, res = 0,0,0
            for ind, num in enumerate(nums):
                cur += num
                while cur > x:
                    cur -= nums[l]
                    l += 1
                res += (ind-l+1)
            return res
        return goals(goal) - goals(goal-1)

