class Solution:
    def maximumSwap(self, num: int) -> int:
        numList = list(str(num))

        ans = num

        for i in range(len(numList)):
            for j in range(i+1, len(numList)):
                temp = numList.copy()
                temp[i], temp[j] = temp[j], temp[i]

                val = int("".join(temp))
                ans = max(ans, val)
        return ans




        