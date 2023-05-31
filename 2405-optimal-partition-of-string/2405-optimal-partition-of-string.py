class Solution:
    def partitionString(self, s: str) -> int:
        k = set()
        c = 0
        i=0
        while i <len(s):
            if s[i] not in k:
                k.add(s[i])
                i += 1
            else:
                c+=1
                k = set()
            
        return c +1