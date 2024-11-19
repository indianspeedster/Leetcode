class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        hashSet = set()

        left = 0
        ans = 0
        curr = 0
        for i, num in enumerate(nums):
            if num in hashSet:
                while num in hashSet:
                    hashSet.remove(nums[left])
                    curr -= nums[left]
                    left += 1
            curr += num
            hashSet.add(num)
            if i-left+1 == k:
                ans = max(ans, curr)
                hashSet.remove(nums[left])
                curr -= nums[left]
                left += 1
        return ans
        