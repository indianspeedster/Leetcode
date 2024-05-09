class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse = True)
        ans = 0
        for ind, child in enumerate(happiness):
            if ind == k:
                return ans
            if child - ind >= 0:
                ans += child
                ans -= ind
            else:
                return ans
        return ans
            
            
            
        