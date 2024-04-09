class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        curr = tickets[k]
        ans = 0
        for i in range(curr):
            for j in range(len(tickets)):
                if tickets[j] >= 1:
                    tickets[j] -= 1
                    ans += 1
                if tickets[k] == 0:
                    return ans 

        