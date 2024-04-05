class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digit="123456789"
        ans = []
        for i in range(len(digits)):
            for j in range(i+1,len(digits) ):
                num = int(digit[i:j])
                if num in range(low, high+1):
                    ans.append(num)
        return sorted(ans)

        