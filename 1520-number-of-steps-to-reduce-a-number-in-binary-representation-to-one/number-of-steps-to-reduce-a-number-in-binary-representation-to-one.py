class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        carry = 0
        for num in s[1:][::-1]:
            num = int(num)
            if num + carry == 2:
                carry = 1
                ans += 1
            elif num+carry == 1:
                ans += 2
                carry = 1
            else:
                ans += 1
                carry = 0
        if carry:
            return ans + 1
        else:
            return ans 