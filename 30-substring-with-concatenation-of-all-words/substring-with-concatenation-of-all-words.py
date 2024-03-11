class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_set = Counter(words)
        total_words = len(words)
        window = len(words[0])
        ans = []
        start = 0
        end = len(s)
        reoccuring = False
        while start<end-window+1:
            word = s[start:start+window]
            if word in word_set and word_set[word]>0:
                new_set = {key:val for key,val in word_set.items()}
                n_start=start
                if start + total_words*window < end+1:
                    while start < end:
                        if s[start:start+window] in new_set and new_set[s[start:start+window]]>0:
                            new_set[s[start:start+window]] -= 1
                            start += window
                        else:
                            
                            break
                    if sum(new_set.values()) == 0:
                        ans.append(n_start)
                    start = n_start +1
                else:
                    break
                
            else:
                start += 1
                
        return ans
        