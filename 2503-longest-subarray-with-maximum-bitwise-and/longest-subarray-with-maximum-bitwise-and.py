class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = max(nums)
        start = 0
        ans = 0
        while start < len(nums):
            if nums[start] == n:
                k = start
                while k < len(nums) and nums[k] == n:
                    k += 1
                ans = max(ans, k-start)
                start = k
            else:
                start += 1


        return ans

        