class Solution:
    def reverseParentheses(self, s: str) -> str:
        st1, st2 = [], deque()

        for char in s:
            if char != ")":
                st1.append(char)
            else:
                while st1[-1] != "(":
                    ele = st1.pop()
                    st2.append(ele)
                st1.pop()
                while st2:
                    ele = st2.popleft()
                    st1.append(ele)
        return "".join(st1)
        