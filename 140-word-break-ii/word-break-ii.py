class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        self.ans = []
        def dfs(i, st):
            if i == len(s):
                self.ans.append(st[:-1])
                return
            for word in words:
                length = len(word)
                if s[i:i+length] == word:
                    dfs(i+length, st + word + " ")
            return
        dfs(0, "")
        return self.ans
        