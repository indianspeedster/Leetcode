class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        ans = 0
        for ind, sub in enumerate(s):
            if sub == "(":
                st.append(ind)
            else:
                st.pop()
                if not st:
                    st.append(ind)
                ans = max(ans, ind-st[-1])
        return ans
        