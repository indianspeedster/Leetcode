class Solution:
    def minimumPushes(self, word: str) -> int:
        distinct = 0
        ans = 0
        countDict = Counter(word)
      
        for key, val in sorted(countDict.items(), reverse=True, key = lambda x:x[1]):
            
            ans += val * (1 + distinct // 8)
            distinct += 1
            
        return ans

        