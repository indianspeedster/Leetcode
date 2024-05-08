class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = [(sc, i) for i,sc in enumerate(score)]
        arr = sorted(arr, reverse=True)
        ans = [0 for i in score]

        for i, ele in enumerate(arr):
            if i == 0:
                ans[ele[1]] = "Gold Medal"
            elif i == 1:
                ans[ele[1]] = "Silver Medal"
            elif i == 2:
                ans[ele[1]] = "Bronze Medal"
            else:
                ans[ele[1]] = str(i+1)
        return ans

        