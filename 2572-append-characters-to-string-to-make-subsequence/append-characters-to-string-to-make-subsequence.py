class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0,0

        ls, lt = len(s), len(t)
        while i<ls and j<lt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return lt-j
        