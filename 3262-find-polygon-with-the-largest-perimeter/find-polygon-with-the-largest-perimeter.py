class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        perimeter = 0
        ans = -1
        for num in nums:
            if perimeter > num :
                ans = perimeter + num
            perimeter += num
        return ans
            


        