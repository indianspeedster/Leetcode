class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        def add(num):
            carry = 1
            ans = ""
            for ele in num[::-1]:
                toAdd = int(ele) + carry
                if toAdd == 2:
                    carry = 1
                    ans += str(0)
                else:
                    carry = 0
                    ans += str(toAdd)
            if carry == 1:
                ans += "1"
            return ans[::-1]
        while s != "1":
            if s[-1] == "1":
                s = add(s)
            elif s[-1] == "0":
                s = s[:-1]
            count += 1
        return count
        
        