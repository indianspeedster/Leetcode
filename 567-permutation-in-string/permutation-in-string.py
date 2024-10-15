class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Dict = Counter(s1)
        total = len(s1Dict.keys())
        matches = 0
        s2Dict = defaultdict(int)
        s1len = len(s1)

        for i in range(s1len):
            char = s2[i]
            if char in s1Dict and s2Dict[char] == s1Dict[char]:
                matches -= 1
            s2Dict[char] += 1
            if char in s1Dict and s1Dict[char] == s2Dict[char]:
                matches += 1

        if matches == total:
            return True
        left = 0

        for i, char in enumerate(s2[s1len:]):
            if char in s1Dict and s2Dict[char] == s1Dict[char]:
                matches -= 1
            s2Dict[char] += 1
            if char in s1Dict and s1Dict[char] == s2Dict[char]:
                matches += 1
            prev = s2[left]
            if prev in s1Dict and s2Dict[prev] == s1Dict[prev]:
                matches -= 1
            s2Dict[prev] -= 1
            if prev in s1Dict and s2Dict[prev] == s1Dict[prev]:
                matches += 1
            left += 1
            if matches == total:
                return True
        return False

            
        
        