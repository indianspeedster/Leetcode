class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for st in s:
            if not ans:
                ans.append(st)
                continue
            if ans[-1] != st and ans[-1].lower() == st.lower():
                ans.pop()
            else:
                ans.append(st)
        return "".join(ans) 
        