class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start^goal
        return len([i for i in bin(ans)[2:] if i == "1"])

        