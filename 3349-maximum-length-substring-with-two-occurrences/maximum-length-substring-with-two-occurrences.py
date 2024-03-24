class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        n = len(s)
        maxi = 0
        for i in range(n):
            ch = [0]*26
            for j in range(i,n):
                ch[ord(s[j])-97] += 1
                if max(ch)<=2:
                    maxi = max(maxi, j-i+1)
                    
        return maxi
            
        
        