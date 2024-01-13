class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l,r = 0,0
        ans = 0
        for sub in s:
            if sub =="(":
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, r*2)
            if r>l:
                l,r = 0,0
        l,r = 0,0
        for sub in s[::-1]:
            if sub =="(":
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, r*2)
            if r<l:
                l,r = 0,0
        return ans
        

        return ans

        