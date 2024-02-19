class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n ^ n-1 == (n*2)-1 if n !=0 else False
        