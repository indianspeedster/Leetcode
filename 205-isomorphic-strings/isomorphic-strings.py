class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(list(s))) != len(set(list(t))):
            return False
        d = {}
        for i in range(len(s)):
            if t[i] not in d.keys():
                d[t[i]] = s[i]
        return s == ''.join([d[i] for i in t])