class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapper = set()
        i, j = 0,0
        ans = 0
        while i < len(s):
            while s[i] in mapper:
                mapper.remove(s[j])
                j += 1
            mapper.add(s[i])

            ans = max(ans, i-j+1) 
            i += 1
        return ans
        