class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-4] - nums[0], nums[-1]-nums[3], nums[-2] - nums[2], nums[-3]-nums[1]) if len(nums)>4 else 0
        