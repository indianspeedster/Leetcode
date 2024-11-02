class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        if sentence[0][0] != sentence[-1][-1]:
            return False
        n= len(sentence)
        for i in range(n-1):
            if sentence[i][-1] != sentence[i+1][0]:
                return False
        return True
        