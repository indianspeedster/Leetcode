class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini, maxi = arrays[0][0], arrays[0][-1]
        m = len(arrays)
        maxDistance = 0
        for i in range(1, m):
            maxDistance = max(maxi - arrays[i][0], arrays[i][-1] - mini , maxDistance)
            mini = min(mini, arrays[i][0])
            maxi = max(maxi, arrays[i][-1])
        return maxDistance

        