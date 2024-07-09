class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr = 0
        waitTime = 0
        for start, end in customers:
            if start > curr:
                curr = start
            curr += end
            waitTime += curr - start
        return waitTime / (len(customers))

        