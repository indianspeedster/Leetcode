class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""

        cur = 0
        prev = "-1"

        for i in word:
            if i == prev and cur == 9:
                ans += str(cur) + prev
                cur = 1
                prev = i
            elif i != prev:
                ans += str(cur) + prev
                cur = 1
                prev = i
            else:
                cur += 1
        
        ans += str(cur) + prev
        return ans[3:]
            
        