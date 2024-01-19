class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        win_len = len(needle)
        hay_len = len(haystack)
        for i, s in enumerate(haystack):
            if i > hay_len - win_len:
                break
            if haystack[i:i+win_len] == needle:
                return i
        return -1

        