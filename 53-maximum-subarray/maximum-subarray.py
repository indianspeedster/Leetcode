class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxi = float("-inf")
        for num in nums:
            curr += num
            maxi = max(maxi, curr)
            curr = max(0, curr)
        return maxi

        