class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        @cache
        def dfs(x,y):
            if x== n1 or y==n2:
                return 0
            if text1[x] == text2[y]:
                return 1 + dfs(x+1, y+1)
            else:
                return max(dfs(x+1, y), dfs(x, y+1))
            
        return dfs(0,0)


        