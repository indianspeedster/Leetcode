class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = -1
        curr = 1
        while time != 0:
            if curr == n or curr == 1:
                direction *= -1
            time -= 1
            curr += direction
        return curr




        