class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        for i, c in enumerate(word):
            if c == ch:
                ans = ans + word[:i+1][::-1]
                if (i + 1) in range(len(word)):
                    ans = ans + word[i+1:]
                return ans
        return word
        