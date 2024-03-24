class Solution:
    def minOperations(self, k: int) -> int:
        a = int(k**0.5)
        if a*a == k:
            return (2*a -2)
        if a*(a+1) >= k:
            return (2*a-1)
        if (a+1)*(a+1)>=k:
            return 2*a
        
        