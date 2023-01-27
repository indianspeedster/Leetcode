class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        worddict = set(words)
        def check(w,d):
            if w in d:
                return True
            for i in range(len(w)):
                if w[:i] in d and check(w[i:],d):
                    return True
            return False
        for w in words:
            worddict.remove(w)
            if check(w,worddict):
                res.append(w)
            worddict.add(w)
        return res