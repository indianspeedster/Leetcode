class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def dfs(i,j,s):
            if i==j==n:
                ans.append(s)
                return
            if i==j:
                dfs(i+1,j,s+"(")
            elif i>j and i!=n:
                dfs(i+1,j,s+"(")
                dfs(i,j+1,s+")")
            elif i>j and i==n:
                dfs(i,j+1,s+")")
            return
        dfs(0,0,"")
        return ans
            
                
        