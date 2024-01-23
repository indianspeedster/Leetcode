class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        dic = {chr(97+i):i+1 for i in range(26)}
        for i, val in enumerate(vals):
            dic[chars[i]] = val

        maxi, cur  = 0, 0

        for ind, st in enumerate(s):
            cur += dic[st]
            if cur < 0:
                cur = 0
            else:
                maxi = max(maxi, cur)
        return maxi



        