class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr = sum(cardPoints[:k])
        maxi = curr
        ind = 1
        for num in range(k):
            curr -= cardPoints[k-ind]
            curr += cardPoints[-1*ind]
            ind += 1
            maxi = max(maxi, curr)
        return maxi


        