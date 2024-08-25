class Solution:
    def numDecodings(self, s: str) -> int:
        hashMap = {f"{i}" : chr(i + 64) for i in range(1, 27)}
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == "0":
                return 0
            left =  dfs(i+1)
            if s[i:i+2] not in hashMap:
                right = 0
            else:
                right = dfs(i+2)
            return left + right
        return dfs(0)
       
        