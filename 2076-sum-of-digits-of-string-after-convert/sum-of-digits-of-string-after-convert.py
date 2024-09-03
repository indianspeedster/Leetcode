class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(s):
            su = 0
            for i in s:
                su += int(i)
            return str(su)
        s = "".join([str(ord(i) - 96) for i in s])
        for i in range(k):
            s = transform(s)
        return int(s)
            
            
        