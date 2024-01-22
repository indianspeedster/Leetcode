class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for i, num in enumerate(num1[::-1]):
            num = int(num)
            ans1 = 0
            carry = 0
            for j, mul in enumerate(num2[::-1]):
                mul = int(mul)
                number = mul * num + carry 
                carry, number = divmod(number, 10)
                ans1 += number * 10 ** j
            ans1 += carry * 10 ** (j +1) 
            ans = ans + ans1 * (10**i)
        return str(ans)

        