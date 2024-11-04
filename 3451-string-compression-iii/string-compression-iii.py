class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        cur = 0
        prev = word[0]
        for i in word:
            if (i == prev and cur == 9) or (i != prev):
                ans += str(cur) + prev
                cur = 1
                prev = i
            else:
                cur += 1
        ans += str(cur) + prev
        return ans
            
        