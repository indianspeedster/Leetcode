class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] == "0":
                ans += (r-l)
                l += 1
        return ans
        