class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        dic = set("a e i o u A E I O U".split())
        t = len(s)//2
        l1, l2 = s[:t], s[t:]
        cnt1, cnt2,i = 0,0,0
        while i < t:
            if l1[i] in dic:
                cnt1 += 1
            if l2[i] in dic:
                cnt2 += 1
            i += 1
        
        return cnt1 == cnt2

        