class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return ""
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        n = len(digits)
        ans=[]
        def dfs(i,st):
            if i>=n:
                ans.append(st)
                return 
            for k in dic[digits[i]]:
                st = st + k
                dfs(i+1,st)
                st = st[:-1]
        dfs(0,"")
        return ans