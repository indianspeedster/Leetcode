class Trie:
    def __init__(self):
        self.children = {}
        self.islast = False

class WordDictionary:

    def __init__(self):
        self.dictionary = Trie()

    def addWord(self, word: str) -> None:
        cur = self.dictionary
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = Trie()
            cur = cur.children[letter]
        cur.islast = True
        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root
            for j in range(i, len(word)):
                if word[j] == ".":
                    for nodes in cur.children.values():
                        if dfs(j+1, nodes):
                            return True
                    
                    return False
                else:
                    if word[j] not in cur.children:
                        return False
                    cur = cur.children[word[j]]
            return cur.islast
        return dfs(0, self.dictionary)

                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)