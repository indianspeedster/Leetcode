class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        left = 0
        ans = 0
        for ind, char in enumerate(s):
            if char not in hashMap or hashMap[char] < left:
                hashMap[char] = ind
                ans = max(ans, ind-left+1)
            else:
                left = hashMap[char] + 1
                hashMap[char] = ind   
        return ans

        