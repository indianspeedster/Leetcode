class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        maxArr = [0]*n
        i = n-1
        prevMax = 0
        for num in reversed(nums):
            prevMax = max(num, prevMax)
            maxArr[i] = prevMax
            i -= 1
        ans = 0
        left = 0

        for i, num in enumerate(nums):
            if nums[left] <= maxArr[i]:
                ans = max(ans, i-left)
            else:
                while nums[left]>maxArr[i]:
                    left += 1
            ans = max(ans, i-left)
        return ans

        