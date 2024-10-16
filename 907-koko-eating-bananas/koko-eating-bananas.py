class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def func(ban):
            total = sum(piles)
            curr = 0
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/ban)
            if hour <= h:
                return True
            return False

        start = max(piles)

        left, right = 1, start
        ans = start
        while left <= right:
            mid = (left+right)//2
            if func(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans
        


        