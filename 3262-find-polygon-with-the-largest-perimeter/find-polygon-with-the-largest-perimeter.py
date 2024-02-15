class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        perimeter = nums[0] + nums[1]
        ans = -1
        for i, num in enumerate(nums[2:]):
            if perimeter > num :
                ans = perimeter + num
            perimeter += num
        return ans
            


        