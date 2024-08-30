class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        n = len(nums)
        product = 1
        for i in range(n):
            ans[i] = product
            product *= nums[i]
        product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= product
            product *= nums[i]
        return ans
        