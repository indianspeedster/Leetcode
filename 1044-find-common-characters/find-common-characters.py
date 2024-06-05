class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = defaultdict(list)
        for word in words:
            for letter, val in Counter(word).items():
                dic[letter].append(val)
        n = len(words)
        ans = []
        for ch, val in dic.items():
            if len(val) == n:
                toAdd = min(val)
                for i in range(toAdd):
                    ans.append(ch)
        return ans
        


                

        