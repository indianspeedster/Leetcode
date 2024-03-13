class Solution:
    def pivotInteger(self, n: int) -> int:
        sumTotal = (n*(n+1)/2)
        currSum = 0
        for num in range(1, n+1):
            currSum += num
            if currSum == (sumTotal-currSum+num):
                return num
        return -1
        