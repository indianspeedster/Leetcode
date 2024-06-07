class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []
        sentence = sentence.split()
        for word in sentence:
            toAdd = [word]
            n = len(word)
            for dicword in dictionary:
                k = len(dicword)
                if n >= k and word[:k] == dicword:
                    toAdd.append(dicword)
            toAdd.sort()
            ans.append(toAdd[0])
        return " ".join(ans)
                
        