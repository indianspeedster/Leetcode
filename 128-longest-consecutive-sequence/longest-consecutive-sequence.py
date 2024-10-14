class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        hashSet = set(nums)
        for num in nums:
            if num in hashSet:
                curr = num + 1
                total = 0
                while curr in hashSet:
                    total += 1
                    hashSet.remove(curr)
                    curr += 1
                curr = num
                while curr in hashSet:
                    total += 1
                    hashSet.remove(curr)
                    curr -= 1
                ans = max(ans, total)
        return ans
