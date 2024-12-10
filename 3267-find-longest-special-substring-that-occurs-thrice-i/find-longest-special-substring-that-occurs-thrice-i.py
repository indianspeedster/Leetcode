class Solution:
    def maximumLength(self, s: str) -> int:
        hashMap = defaultdict(int)

        n = len(s)
        
        for i in range(n):
            for j in range(i, n):
                hashMap[s[i:j+1]] += 1

        ans = -1

        for key, val in hashMap.items():
            if val >= 3 and len(set(list(key))) == 1:
            
                ans = max(ans, len(key))

        return ans
        