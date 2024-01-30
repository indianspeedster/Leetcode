class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["+", "*", "/", "-"]
        st = []
        for element in tokens:
           
            if element in op:
                num_2 = st.pop()
                num_1 = st.pop()
                if element == "+":
                    st.append(num_1 + num_2)
                elif element == "*":
                    st.append(num_1 * num_2)
                elif element == "/":
                    st.append(int(num_1 / num_2))
                else:
                    st.append(num_1-num_2)
            else:
                st.append(int(element))
        return st[-1]
        