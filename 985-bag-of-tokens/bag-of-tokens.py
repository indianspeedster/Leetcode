class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        low = 0
        high = len(tokens) - 1
        res, score = 0, 0
        tokens.sort()

        while low <= high:
            if power >= tokens[low]:
                score += 1
                power -= tokens[low]
                low += 1
                res = max(res, score)
            elif score > 0:
                score -= 1
                power += tokens[high]
                high -= 1
            else:
                return res

        return res       