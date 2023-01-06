class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        ans = 0
        for i in costs:
            if i<=coins :
                ans += 1
                coins -= i
            elif coins==0:
                break
        return ans
        