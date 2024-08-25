class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        ans = 0
        hashMap = defaultdict(int)
        for right, char in enumerate(s):
            hashMap[char] += 1
            if len(hashMap) == 3:
                while len(hashMap) == 3:
                    ans += len(s)-right
                    hashMap[s[left]] -= 1
                    if hashMap[s[left]] == 0:
                        del hashMap[s[left]]
                    left += 1
        return ans





        