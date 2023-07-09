class Solution:
    def countAndSay(self, n: int) -> str:
        def count(k):
            k = str(k)
            ans = ""
            c = 0
            last = k[0]
            for i in k:
                if i == last:
                    c += 1
                else:
                    ans += str(c)+last
                    last = i
                    c = 1
            ans += str(c) + last
            return ans
        
        if n == 1:
            return str(1)
        return count(self.countAndSay(n-1))
        