class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = (m+n) * mean
        toAchieve = total - sum(rolls)
        ans = []
        k = toAchieve / n
        
    
        if k > 6 or k < 1:
          
            return []
        while n > 0:
            ans.append(ceil(toAchieve/n))
            toAchieve -= ceil(toAchieve/n)
            n -= 1
        return ans

        