class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        maxSubstring = 0
        strLen = len(s)
        totalCost = 0
        for right in range(strLen):
            totalCost += abs(ord(s[right]) - ord(t[right]))
            while totalCost > maxCost:
                totalCost -= (abs(ord(s[left]) - ord(t[left])))
                left += 1
            maxSubstring = max(maxSubstring,right-left+1)
        return maxSubstring
                     



        