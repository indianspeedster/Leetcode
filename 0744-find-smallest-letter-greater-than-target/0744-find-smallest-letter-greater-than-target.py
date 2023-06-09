class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        tar = ord(target)
        ans = 200
        for i in letters:
            if tar<ord(i):
                if ans> ord(i):
                    ans = ord(i)
        return chr(ans) if ans != 200 else letters[0]
                
            
        