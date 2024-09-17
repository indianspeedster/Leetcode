class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split())
        s2 = Counter(s2.split())
        ans = []
        for key, val in s1.items():
            if key not in s2 and val == 1:
                ans.append(key)
        for key, val in s2.items():
            if key not in s1 and val == 1:
                ans.append(key)
        return ans

        