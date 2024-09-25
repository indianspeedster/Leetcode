class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hashMap = defaultdict(int)
        for word in words:
            n = len(word)
            for i in range(n):
                hashMap[word[:i+1]] += 1
        ans = []
        for word in words:
            n = len(word)
            k = 0
            for i in range(n):
                k += hashMap[word[:i+1]]
            ans.append(k)
        return ans

        