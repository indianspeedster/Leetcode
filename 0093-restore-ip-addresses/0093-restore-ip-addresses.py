class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s)>12:
            return res
        def dfs(i,dot,ip):
            if dot==4 and i == len(s):
                res.append(ip[:-1])
            if dot>4:
                return
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1])<=255 and(i==j or s[i]!="0"):
                    dfs(j+1,dot+1,ip+s[i:j+1]+".")
        dfs(0,0,"")
        return res
        