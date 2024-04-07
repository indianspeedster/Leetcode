class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(n, st):
            if n == len(s):
                return True if st == "" else False
            if s[n] == "(":
                return dfs(n+1, st + "(")
            elif s[n] == ")":
                if st:
                    return dfs(n+1, st[:-1])
                else:
                    return False
            else:
                return dfs(n+1, st+"(") or dfs(n+1, st) or dfs(n+1, st[:-1])
        return dfs(0, "")
        