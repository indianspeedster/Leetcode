class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurence = defaultdict(lambda:0)
        for i, string in enumerate(s):
            lastOccurence[string] = max(i, lastOccurence[string])
        maxi = 0
        ans = []
        for ind, string in enumerate(s):
            maxi = max(maxi, lastOccurence[string])
            if maxi == ind:
                ans.append(ind+1)
        n = len(ans)
        for i in range(n-1, 0, -1):
            ans[i] -= ans[i-1]
        return ans

        