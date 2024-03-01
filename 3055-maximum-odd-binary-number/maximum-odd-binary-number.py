class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = [i for i in s]
        first, last = 0,len(s)-1
        for ind, num in enumerate(s[:-1]):
            if num == "1":
                if s[last] != "1":
                    s[last] , s[ind] = s[ind] , s[last]
                else:
                    s[first], s[ind] = s[ind], s[first]
                    first += 1
        return "".join(s)
             

        