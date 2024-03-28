class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        right = 0
        maxi = 0
        for i, num in enumerate(nums):
            hashMap[num] += 1
            if hashMap[num] > k:
                while num != nums[right]:
                    hashMap[nums[right]] -= 1
                    right += 1
                hashMap[nums[right]] -= 1
                right += 1
            maxi = max(maxi , i-right+1)
        return maxi
                

        