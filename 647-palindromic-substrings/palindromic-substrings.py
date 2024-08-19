class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        s_len = len(s)

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < s_len:
                if s[left] == s[right]:
                    total += 1
                    left -= 1
                    right += 1
                else:
                    break
        for i in range(len(s) - 1):
            left, right = i, i + 1
            while left >= 0 and right < s_len:
                if s[left] == s[right]:
                    total += 1
                    left -= 1
                    right += 1
                else:
                    break
        return total
            
        