class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        k = 0
        for _ in s:
            if _ == "(":
                k += 1
                maxDepth = max(maxDepth, k)
            elif _ == ")":
                k -= 1
        return maxDepth
        