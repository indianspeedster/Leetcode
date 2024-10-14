class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        minLen = len(s)
        tDict = Counter(t)
        need = len(tDict.keys())
        have = 0
        left = 0
        sDict = {}
        for i, char in enumerate(s):
            if char not in sDict:
                sDict[char] = 0
            sDict[char] += 1
            if sDict[char] == tDict[char]:
                have += 1
            while have == need:
                curLen = i-left+1
                if curLen <= minLen:
                    minLen = curLen
                    ans = s[left:i+1]
                sDict[s[left]] -= 1
                if s[left] in tDict and sDict[s[left]] < tDict[s[left]]:
                    have -= 1
                left += 1
        return ans
            
        