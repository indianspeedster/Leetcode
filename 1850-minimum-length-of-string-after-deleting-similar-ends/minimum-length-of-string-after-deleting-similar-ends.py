class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return right - left + 1
            cur = s[left]
            while left <= right and s[left] == cur:
                left += 1
            while left < right and s[right] == cur:
                right -= 1


        return right-left+1
        