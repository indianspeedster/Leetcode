from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            
            if i == len(s) and j == len(p):
                return True
            
            if j == len(p):
                return False
           
            if i == len(s):
                return all(x == '*' for x in p[j:])
            

            if p[j] == "?":
                return dfs(i + 1, j + 1)
            elif p[j] == "*":
                return dfs(i, j + 1) or dfs(i + 1, j)
            else:
                return s[i] == p[j] and dfs(i + 1, j + 1)

        return dfs(0, 0)

        
        