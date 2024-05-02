class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxi = -1
        for i in nums:
            if i > 0 and -1*i in nums_set:
                maxi = max(i, maxi)
        return maxi

        