object Solution {
    def bagOfTokensScore(tokens: Array[Int], power: Int): Int = {
        var res = 0
        var score = 0
        var left = 0
        var right = tokens.length - 1
        val sortedTokens = tokens.sorted 
        var currentPower = power 
        while (left <= right) {
            if (sortedTokens(left) <= currentPower) {
                currentPower -= sortedTokens(left) 
                score += 1
                left += 1
                res = math.max(score, res)
            }
            else if (score > 0) {
                currentPower += sortedTokens(right)
                right -= 1
                score -= 1
            }
            else {
                return res
            }
        }
        res 
    }
}
