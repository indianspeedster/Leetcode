class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = float("-inf")
        t = 0
        for i in gain:
            maxi = max(t, maxi)
            t += i
        maxi = max(t, maxi)   
        return maxi
        