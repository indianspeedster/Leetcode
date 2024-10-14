class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        minLen = len(s)
        left = 0
        def match(c1, c2):
            for key in c2.keys():
                if key not in c1:
                    return False
                if c1[key] < c2[key]:
                    return False
            return True
        tDict = Counter(t)
        sDict = {}
        for i, char in enumerate(s):
            if char not in sDict:
                sDict[char] = 0
            sDict[char] += 1
            while match(sDict, tDict):
                curLen = i-left+1
                if curLen <= minLen:
                    minLen = min(minLen, curLen)
                    ans = s[left:i+1]
                sDict[s[left]] -= 1
                left += 1
        return ans

        