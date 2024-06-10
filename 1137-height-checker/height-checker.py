class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)

        ans  = 0
        for i, j in zip(heights, sortedHeights):
            if i!=j:
                ans += 1
        return ans
        