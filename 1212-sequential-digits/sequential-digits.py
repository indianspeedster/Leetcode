class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num = "123456789"
        ans = []
        window = len(str(low))
        while window <= 9:
            for i in range(9-window+1):
                if int(num[i:i+window]) in range(low,high+1):
                    ans.append(int(num[i:i+window]))
                if int(num[i:i+window])>high:
                    return ans
            window += 1
        return ans


        