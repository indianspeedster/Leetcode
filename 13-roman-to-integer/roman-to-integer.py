class Solution:
    def romanToInt(self, s: str) -> int:
        mapDict = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900, "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        ans = 0
        revS = s[::-1]
        i = 0

        while i < len(s):
            print(ans)
            if  s[i:i+2] in mapDict:
                ans += mapDict[s[i:i+2]]
                i += 2
            else:
                ans += mapDict[s[i:i+1]]
                i += 1
        return ans
        