class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        dic = set("a e i o u A E I O U".split())
        t = len(s)//2
        cnt1, cnt2  = 0, 0
        for letter in s[:t]:
            if letter in dic:
                cnt1 += 1
        for letter in s[t:]:
            if letter in dic:
                cnt2 += 1
        return cnt1 == cnt2

        