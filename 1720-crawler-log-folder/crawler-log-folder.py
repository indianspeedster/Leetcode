class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == "../" :
                ans -= 1
            elif log == "./":
                ans += 0
            else:
                ans += 1
            if ans == -1:
                ans = 0
        return ans if ans > 0 else 0
        