class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        length = len(nums)
        ans = length * (length + 1) // 2 
        start = 0
        count = 0
        curr = 0
        for i, num in enumerate(nums):
            if num == maxElement:
                curr += 1
            if curr == k:
                while nums[start] != maxElement:
                    start += 1
                start += 1
                curr -= 1
            count += i - start + 1
        return ans - count
        
