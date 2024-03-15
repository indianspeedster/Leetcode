class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = []
        for num in nums:
            ans.append(product)
            product *= num
        #print(ans)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= product
            product *= nums[i]
        return ans

        
        