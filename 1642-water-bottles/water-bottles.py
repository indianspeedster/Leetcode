class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        curr = 0
        while numBottles != 0:
            curr += 1
            numBottles -=1
            if curr % numExchange == 0:
                numBottles += 1
        return curr


        