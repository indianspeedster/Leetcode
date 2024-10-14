class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        curr = 1
        for num in nums:
            ans.append(curr)
            curr *= num
        curr = 1
        n = len(nums)
        for i in range(n-1, -1, -1):
            ans[i] *= curr
            curr *= nums[i]
        return ans


        
        