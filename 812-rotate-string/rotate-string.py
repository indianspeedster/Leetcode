class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i , char in enumerate(s):
            ns = s[i+1:] + s[:i+1] 
            if  ns == goal:
                return True
        return False
        