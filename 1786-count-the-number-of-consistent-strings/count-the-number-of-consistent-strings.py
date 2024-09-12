class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        words = [sorted("".join(list(set(list(string))))) for string in words]
        ans = 0
        for word in words:
            flag = True
            for letter in word:
                if letter not in allowed:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans

        