class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        st = []
        for _ in s:
            if _ == "(":
                st.append(_)
                maxDepth = max(maxDepth, len(st))
            elif _ == ")":
                st.pop()
        return maxDepth
        