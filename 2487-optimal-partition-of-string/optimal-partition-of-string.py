class Solution:
    def partitionString(self, s: str) -> int:
        cur = set()
        ans = 1
        for sub in s:
            if sub in cur:
                cur = set()
                ans += 1
            cur.add(sub)
        return ans

        