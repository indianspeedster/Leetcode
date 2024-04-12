class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [height[0]]
        maxRight = [height[-1]]
        for h in height[1:]:
            maxLeft.append(max(h, maxLeft[-1]))
        for h in height[::-1][1:]:
            maxRight.append(max(h, maxRight[-1]))
        maxRight = maxRight[::-1]
        ans  = 0
        for index, h in enumerate(height):
            ans += max(0, min(maxLeft[index], maxRight[index])- h)
        return ans
        