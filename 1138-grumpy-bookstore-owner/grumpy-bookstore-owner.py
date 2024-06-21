class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        window, maxWin = 0, 0
        satisfied = 0
        for i in range(len(customers)):
            if grumpy[i]:
                window += customers[i]
            else:
                satisfied += customers[i]
            
            if i-l+1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            maxWin = max(window, maxWin)
        return satisfied + maxWin
        