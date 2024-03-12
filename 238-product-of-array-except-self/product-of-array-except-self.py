class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [], []
        cur = 1
        for num in nums:
            cur = cur*num
            pre.append(cur)
        cur = 1
        for num in reversed(nums):
            cur = cur*num
            post.append(cur)
        post = post[::-1]
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(post[i+1])
            elif i == len(nums)-1:
                ans.append(pre[i-1])
            else:
                ans.append(pre[i-1]*post[i+1])
        return ans
        