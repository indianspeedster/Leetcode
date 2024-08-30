class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        maxCount = 0
        for num in nums:
            count = 0
            numb = num
            while numb in hashSet:
                hashSet.remove(numb)
                count += 1
                numb -= 1
                
            numb = num + 1
            while numb in hashSet:
                hashSet.remove(numb)
                count += 1
                numb += 1
               
            maxCount = max(maxCount, count) 
        return maxCount

        