class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        ans = 0
        for i in s:
            if i == ")":
                if not st:
                    ans += 1
                else:
                    st.pop()
            else:
                st.append("(")
        return ans + len(st)
        